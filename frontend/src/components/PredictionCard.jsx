import React from 'react';
import { TrendingUp, TrendingDown, AlertTriangle, CheckCircle, Clock } from 'lucide-react';

const PredictionCard = ({ prediction }) => {
  if (!prediction) return null;

  const { prediction: result, probability, risk_level, timestamp } = prediction;
  const isChurn = result === 'Churn';
  const probPercentage = (probability * 100).toFixed(1);

  const getRiskColor = (level) => {
    switch (level) {
      case 'High': return 'text-red-600 bg-red-50 border-red-200';
      case 'Medium': return 'text-yellow-600 bg-yellow-50 border-yellow-200';
      case 'Low': return 'text-green-600 bg-green-50 border-green-200';
      default: return 'text-gray-600 bg-gray-50 border-gray-200';
    }
  };

  return (
    <div className="bg-white rounded-xl shadow-lg border border-gray-100 overflow-hidden">
      <div className={`p-1 ${isChurn ? 'bg-red-500' : 'bg-green-500'}`} />
      <div className="p-6">
        <div className="flex justify-between items-start mb-6">
          <div>
            <h3 className="text-sm font-semibold text-gray-500 uppercase tracking-wider">Prediction Result</h3>
            <div className="flex items-center mt-1">
              {isChurn ? (
                <>
                  <AlertTriangle className="h-8 w-8 text-red-500 mr-2" />
                  <span className="text-3xl font-extrabold text-gray-900">Churn Likely</span>
                </>
              ) : (
                <>
                  <CheckCircle className="h-8 w-8 text-green-500 mr-2" />
                  <span className="text-3xl font-extrabold text-gray-900">Retention Likely</span>
                </>
              )}
            </div>
          </div>
          <div className={`px-4 py-2 rounded-full border ${getRiskColor(risk_level)} flex items-center`}>
            <span className="font-bold">{risk_level} Risk</span>
          </div>
        </div>

        <div className="grid grid-cols-2 gap-4 mb-6">
          <div className="bg-gray-50 p-4 rounded-lg">
            <p className="text-xs font-medium text-gray-500 uppercase">Probability</p>
            <p className="text-2xl font-bold text-gray-900">{probPercentage}%</p>
          </div>
          <div className="bg-gray-50 p-4 rounded-lg">
            <p className="text-xs font-medium text-gray-500 uppercase">Confidence Score</p>
            <p className="text-2xl font-bold text-gray-900">
              {isChurn ? probPercentage : (100 - probPercentage).toFixed(1)}%
            </p>
            <div className="flex items-center mt-1 text-xs text-gray-400">
              <Clock className="w-3 h-3 mr-1" />
              {timestamp}
            </div>
          </div>
        </div>

        <div className="border-t border-gray-100 pt-4">
          <div className="flex items-center text-sm text-gray-600">
            {isChurn ? (
              <TrendingUp className="h-4 w-4 text-red-500 mr-2" />
            ) : (
              <TrendingDown className="h-4 w-4 text-green-500 mr-2" />
            )}
            <span>
              The model is { (isChurn ? probability : (1 - probability)) > 0.8 ? 'highly' : 'moderately' } confident that this customer will {isChurn ? 'discontinue' : 'continue'} their service.
            </span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default PredictionCard;
