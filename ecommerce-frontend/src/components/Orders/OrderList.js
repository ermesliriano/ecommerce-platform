import React, { useEffect, useState } from 'react';
import api from '../../services/api';

const OrderList = ({ userId }) => {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    const fetchOrders = async () => {
      const response = await api.get(`/orders/user/${userId}`);
      setOrders(response.data);
    };

    fetchOrders();
  }, [userId]);

  return (
    <div>
      <h1>Orders</h1>
      <ul>
        {orders.map(order => (
          <li key={order.id}>Order {order.id} - Quantity: {order.quantity}</li>
        ))}
      </ul>
    </div>
  );
};

export default OrderList;
