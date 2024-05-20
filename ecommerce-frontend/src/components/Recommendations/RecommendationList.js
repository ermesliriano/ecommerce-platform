import React, { useEffect, useState } from 'react';
import api from '../../services/api';

const RecommendationList = ({ userId }) => {
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    const fetchRecommendations = async () => {
      const response = await api.get(`/recommendations/${userId}`);
      setRecommendations(response.data);
    };

    fetchRecommendations();
  }, [userId]);

  return (
    <div>
      <h1>Recommendations</h1>
      <ul>
        {recommendations.map(recommendation => (
          <li key={recommendation.product_id}>Product ID: {recommendation.product_id}</li>
        ))}
      </ul>
    </div>
  );
};

export default RecommendationList;
