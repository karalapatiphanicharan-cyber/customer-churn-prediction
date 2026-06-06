import React from 'react';
import { PieChart, Pie, Cell, ResponsiveContainer, Label } from 'recharts';

const RiskGauge = ({ probability, riskLevel }) => {
  const data = [
    { name: 'Risk', value: probability * 100 },
    { name: 'Remaining', value: 100 - (probability * 100) },
  ];

  const getColors = (level) => {
    switch (level) {
      case 'High': return ['#ef4444', '#fee2e2'];
      case 'Medium': return ['#f59e0b', '#fef3c7'];
      case 'Low': return ['#10b981', '#d1fae5'];
      default: return ['#3b82f6', '#dbeafe'];
    }
  };

  const colors = getColors(riskLevel);

  return (
    <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100 flex flex-col items-center">
      <h3 className="text-sm font-semibold text-gray-500 uppercase tracking-wider mb-4">Risk Gauge</h3>
      <div className="w-full h-48">
        <ResponsiveContainer width="100%" height="100%">
          <PieChart>
            <Pie
              data={data}
              cx="50%"
              cy="100%"
              startAngle={180}
              endAngle={0}
              innerRadius={60}
              outerRadius={80}
              paddingAngle={0}
              dataKey="value"
            >
              <Cell fill={colors[0]} />
              <Cell fill={colors[1]} />
              <Label
                value={`${(probability * 100).toFixed(0)}%`}
                position="centerBottom"
                dy={-20}
                style={{ fontSize: '24px', fontWeight: 'bold', fill: '#111827' }}
              />
            </Pie>
          </PieChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default RiskGauge;
