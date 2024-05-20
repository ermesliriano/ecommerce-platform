# recommendation-service/recommendation_service.py
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recommendations.db'
db = SQLAlchemy(app)

class Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, nullable=False)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/recommendations/<int:user_id>', methods=['GET'])
def get_recommendations(user_id):
    recommendations = Recommendation.query.filter_by(user_id=user_id).all()
    return jsonify([{"user_id": r.user_id, "product_id": r.product_id} for r in recommendations])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
