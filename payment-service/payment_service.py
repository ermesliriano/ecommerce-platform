# payment-service/payment_service.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payments.db'
db = SQLAlchemy(app)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/pay', methods=['POST'])
def make_payment():
    data = request.json
    new_payment = Payment(order_id=data['order_id'], status='paid')
    db.session.add(new_payment)
    db.session.commit()
    return jsonify({"message": "Payment successful"}), 201

@app.route('/payments/<int:order_id>', methods=['GET'])
def get_payment_status(order_id):
    payment = Payment.query.filter_by(order_id=order_id).first()
    if payment:
        return jsonify({"order_id": payment.order_id, "status": payment.status})
    return jsonify({"message": "Payment not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
