# order-service/order_service.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
db = SQLAlchemy(app)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    new_order = Order(user_id=data['user_id'], product_id=data['product_id'], quantity=data['quantity'])
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"order_id": new_order.id}), 201

@app.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    order = Order.query.get(id)
    if order:
        return jsonify({"id": order.id, "user_id": order.user_id, "product_id": order.product_id, "quantity": order.quantity})
    return jsonify({"message": "Order not found"}), 404

@app.route('/orders/user/<int:user_id>', methods=['GET'])
def get_user_orders(user_id):
    user_orders = Order.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": order.id, "user_id": order.user_id, "product_id": order.product_id, "quantity": order.quantity} for order in user_orders])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
