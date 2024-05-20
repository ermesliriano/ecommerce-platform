import React, { useState } from 'react';
import api from '../../services/api';

const Payment = ({ orderId }) => {
  const [status, setStatus] = useState('');

  const handlePayment = async () => {
    try {
      const response = await api.post('/pay', { order_id: orderId });
      setStatus(response.data.message);
    } catch (error) {
      setStatus('Payment Failed');
    }
  };

  return (
    <div>
      <h1>Payment</h1>
      <button onClick={handlePayment}>Pay Now</button>
      <p>Status: {status}</p>
    </div>
  );
};

export default Payment;
