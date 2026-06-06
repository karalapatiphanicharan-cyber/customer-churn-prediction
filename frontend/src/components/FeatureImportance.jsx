import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Cell } from 'recharts';

const FeatureImportance = ({ prediction }) => {
  const data = [
    { name: 'Contract_Month-to-month', importance: 0.85, type: 'Negative' },
    { name: 'Tenure', importance: 0.72, type: 'Positive' },
    { name: 'InternetService_Fiber', importance: 0.65, type: 'Negative' },
    { name: 'MonthlyCharges', importance: 0.58, type: 'Negative' },
    { name: 'Contract_Two_year', importance: 0.52, type: 'Positive' },
    { name: 'PaymentMethod_E-Check', importance: 0.45, type: 'Negative' },
    { name: 'TechSupport_No', importance: 0.38, type: 'Negative' },
    { name: 'OnlineSecurity_No', importance: 0.32, type: 'Negative' },
  ].sort((a, b) => b.importance - a.importance);

  return (
    <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
      <h3 className="text-sm font-semibold text-gray-500 uppercase tracking-wider mb-6">Key Risk Drivers (Global)</h3>
      <div className="w-full h-80">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data} layout="vertical" margin={{ top: 5, right: 30, left: 40, bottom: 5 }}>
            <CartesianGrid strokeDasharray="3 3" horizontal={true} vertical={false} stroke="#f3f4f6" />
            <XAxis type="number" hide />
            <YAxis dataKey="name" type="category" tick={{ fontSize: 11, fill: '#4b5563' }} width={150} />
            <Tooltip cursor={{ fill: '#f9fafb' }} contentStyle={{ borderRadius: '8px', border: 'none', boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)' }} />
            <Bar dataKey="importance" radius={[0, 4, 4, 0]}>
              {data.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={entry.type === 'Positive' ? '#10b981' : '#ef4444'} />
              ))}
            </Bar>
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default FeatureImportance;
