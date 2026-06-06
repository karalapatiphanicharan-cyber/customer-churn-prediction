import React from 'react';
import { usePrediction } from '../hooks/usePrediction';
import CustomerForm from '../components/CustomerForm';
import PredictionCard from '../components/PredictionCard';
import RiskGauge from '../components/RiskGauge';
import FeatureImportance from '../components/FeatureImportance';
import LoadingSpinner from '../components/LoadingSpinner';
import ErrorMessage from '../components/ErrorMessage';
import { LayoutDashboard, Users, Info } from 'lucide-react';

const Dashboard = () => {
  const { prediction, loading, error, getPrediction, resetPrediction } = usePrediction();

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white border-b border-gray-200 sticky top-0 z-10">
        <div className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
          <div className="flex items-center">
            <div className="bg-primary-600 p-2 rounded-lg mr-3">
              <LayoutDashboard className="h-6 w-6 text-white" />
            </div>
            <div>
              <h1 className="text-2xl font-bold text-gray-900 leading-tight">ChurnGuard AI</h1>
              <p className="text-sm text-gray-500 font-medium">Predictive Customer Retention Dashboard</p>
            </div>
          </div>
          <div className="flex items-center px-3 py-1 bg-green-50 text-green-700 rounded-full text-xs font-bold border border-green-200">
            Model: XGBoost v1.0.0
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 py-8 grid grid-cols-1 lg:grid-cols-12 gap-8">
        <div className="lg:col-span-7 xl:col-span-8">
          <CustomerForm onSubmit={getPrediction} isLoading={loading} />
        </div>

        <div className="lg:col-span-5 xl:col-span-4 space-y-8">
          {!prediction && !loading && !error && (
            <div className="bg-white rounded-xl border-2 border-dashed border-gray-200 p-12 text-center text-gray-500">
              <Users className="h-8 w-8 mx-auto mb-4" />
              <h3 className="text-lg font-bold text-gray-900 mb-2">Ready to Analyze</h3>
              <p className="text-sm">Enter customer details to generate prediction.</p>
            </div>
          )}
          {loading && <div className="bg-white rounded-xl shadow-sm p-8"><LoadingSpinner /></div>}
          {error && <ErrorMessage message={error} onRetry={() => resetPrediction()} />}
          {prediction && !loading && (
            <>
              <PredictionCard prediction={prediction} />
              <RiskGauge probability={prediction.probability} riskLevel={prediction.risk_level} />
              <FeatureImportance prediction={prediction} />
              <div className="bg-primary-50 rounded-xl p-6 border border-primary-100 flex items-start">
                <Info className="h-5 w-5 text-primary-600 mr-3" />
                <div>
                  <h4 className="text-sm font-bold text-primary-900">Next Best Action</h4>
                  <p className="text-xs text-primary-700 mt-1 leading-relaxed">
                    {prediction.risk_level === 'High'
                      ? "Recommend immediate outreach with a loyalty discount."
                      : prediction.risk_level === 'Medium'
                      ? "Suggest upgrading to premium support."
                      : "Maintain current engagement."}
                  </p>
                </div>
              </div>
            </>
          )}
        </div>
      </main>

      <footer className="bg-white border-t border-gray-200 mt-12 py-8 text-center text-gray-400 text-xs">
        &copy; 2026 ChurnGuard AI.
      </footer>
    </div>
  );
};

export default Dashboard;
