import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Login from './components/Auth/Login';
import Register from './components/Auth/Register';
import ProductList from './components/Products/ProductList';
import OrderList from './components/Orders/OrderList';
import Payment from './components/Payments/Payment';
import RecommendationList from './components/Recommendations/RecommendationList';

function App() {
  const userId = 1; // Simulación de obtener el ID del usuario autenticado

  return (
    <div>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/products" element={<ProductList />} />
        <Route path="/orders" element={<OrderList userId={userId} />} />
        <Route path="/payment" element={<Payment orderId={1} />} /> {/* Simulación de obtener el ID del pedido */}
        <Route path="/recommendations" element={<RecommendationList userId={userId} />} />
      </Routes>
    </div>
  );
}

export default App;
