import { useState, useCallback } from 'react';
import { predictChurn } from '../services/api';

export const usePrediction = () => {
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const getPrediction = useCallback(async (customerData) => {
    setLoading(true);
    setError(null);
    try {
      const result = await predictChurn(customerData);
      setPrediction({
        ...result,
        timestamp: new Date().toLocaleString(),
      });
      return result;
    } catch (err) {
      setError(err.message);
      setPrediction(null);
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  const resetPrediction = () => {
    setPrediction(null);
    setError(null);
  };

  return {
    prediction,
    loading,
    error,
    getPrediction,
    resetPrediction,
  };
};
