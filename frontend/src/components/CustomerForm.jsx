import React, { useState } from 'react';
import { User, Globe, CreditCard, Send } from 'lucide-react';

const CustomerForm = ({ onSubmit, isLoading }) => {
  const [formData, setFormData] = useState({
    gender: 'Male',
    SeniorCitizen: 'No',
    Partner: 'No',
    Dependents: 'No',
    tenure: 1,
    PhoneService: 'Yes',
    MultipleLines: 'No',
    InternetService: 'Fiber optic',
    OnlineSecurity: 'No',
    OnlineBackup: 'No',
    DeviceProtection: 'No',
    TechSupport: 'No',
    StreamingTV: 'No',
    StreamingMovies: 'No',
    Contract: 'Month-to-month',
    PaperlessBilling: 'Yes',
    PaymentMethod: 'Electronic check',
    MonthlyCharges: 70.0,
    TotalCharges: 70.0,
  });

  const [errors, setErrors] = useState({});

  const handleChange = (e) => {
    const { name, value, type } = e.target;
    setFormData({
      ...formData,
      [name]: type === 'number' ? parseFloat(value) : value,
    });
    if (errors[name]) {
      setErrors({ ...errors, [name]: null });
    }
  };

  const validate = () => {
    const newErrors = {};
    if (formData.tenure < 0) newErrors.tenure = 'Tenure must be at least 0';
    if (formData.MonthlyCharges < 0) newErrors.MonthlyCharges = 'Monthly charges must be at least 0';
    if (formData.TotalCharges < 0) newErrors.TotalCharges = 'Total charges must be at least 0';
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validate()) {
      onSubmit(formData);
    }
  };

  const inputClass = "w-full p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-primary-500 transition-all";
  const labelClass = "block text-xs font-semibold text-gray-700 uppercase tracking-wider mb-1";
  const sectionTitleClass = "flex items-center text-sm font-bold text-gray-900 border-b border-gray-200 pb-2 mb-4 mt-6";

  return (
    <form onSubmit={handleSubmit} className="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
      <div className="p-6">
        <h2 className="text-xl font-bold text-gray-900 mb-6 flex items-center">
          <User className="mr-2 text-primary-600" />
          Customer Information
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {/* Demographics */}
          <div className="space-y-4">
            <h3 className={sectionTitleClass}><User className="w-4 h-4 mr-2" /> Demographics</h3>
            <div>
              <label htmlFor="gender" className={labelClass}>Gender</label>
              <select id="gender" name="gender" value={formData.gender} onChange={handleChange} className={inputClass}>
                <option value="Male">Male</option>
                <option value="Female">Female</option>
              </select>
            </div>
            <div>
              <label htmlFor="SeniorCitizen" className={labelClass}>Senior Citizen</label>
              <select id="SeniorCitizen" name="SeniorCitizen" value={formData.SeniorCitizen} onChange={handleChange} className={inputClass}>
                <option value="No">No</option>
                <option value="Yes">Yes</option>
              </select>
            </div>
            <div>
              <label htmlFor="Partner" className={labelClass}>Partner</label>
              <select id="Partner" name="Partner" value={formData.Partner} onChange={handleChange} className={inputClass}>
                <option value="No">No</option>
                <option value="Yes">Yes</option>
              </select>
            </div>
            <div>
              <label htmlFor="Dependents" className={labelClass}>Dependents</label>
              <select id="Dependents" name="Dependents" value={formData.Dependents} onChange={handleChange} className={inputClass}>
                <option value="No">No</option>
                <option value="Yes">Yes</option>
              </select>
            </div>
          </div>
          {/* Services */}
          <div className="space-y-4">
            <h3 className={sectionTitleClass}><Globe className="w-4 h-4 mr-2" /> Services</h3>
            <div>
              <label htmlFor="PhoneService" className={labelClass}>Phone Service</label>
              <select id="PhoneService" name="PhoneService" value={formData.PhoneService} onChange={handleChange} className={inputClass}>
                <option value="No">No</option>
                <option value="Yes">Yes</option>
              </select>
            </div>
            <div>
              <label htmlFor="InternetService" className={labelClass}>Internet Service</label>
              <select id="InternetService" name="InternetService" value={formData.InternetService} onChange={handleChange} className={inputClass}>
                <option value="DSL">DSL</option>
                <option value="Fiber optic">Fiber optic</option>
                <option value="No">No</option>
              </select>
            </div>
            <div>
              <label htmlFor="MultipleLines" className={labelClass}>Multiple Lines</label>
              <select id="MultipleLines" name="MultipleLines" value={formData.MultipleLines} onChange={handleChange} className={inputClass}>
                <option value="No">No</option>
                <option value="Yes">Yes</option>
                <option value="No phone service">No phone service</option>
              </select>
            </div>
            <div>
              <label htmlFor="OnlineSecurity" className={labelClass}>Online Security</label>
              <select id="OnlineSecurity" name="OnlineSecurity" value={formData.OnlineSecurity} onChange={handleChange} className={inputClass}>
                <option value="No">No</option>
                <option value="Yes">Yes</option>
                <option value="No internet service">No internet service</option>
              </select>
            </div>
          </div>
          {/* Account & Billing */}
          <div className="space-y-4">
            <h3 className={sectionTitleClass}><CreditCard className="w-4 h-4 mr-2" /> Account & Billing</h3>
            <div>
              <label htmlFor="tenure" className={labelClass}>Tenure (Months)</label>
              <input id="tenure" type="number" name="tenure" value={formData.tenure} onChange={handleChange} className={inputClass} min="0" />
            </div>
            <div>
              <label htmlFor="Contract" className={labelClass}>Contract</label>
              <select id="Contract" name="Contract" value={formData.Contract} onChange={handleChange} className={inputClass}>
                <option value="Month-to-month">Month-to-month</option>
                <option value="One year">One year</option>
                <option value="Two year">Two year</option>
              </select>
            </div>
            <div>
              <label htmlFor="MonthlyCharges" className={labelClass}>Monthly Charges</label>
              <input id="MonthlyCharges" type="number" step="0.01" name="MonthlyCharges" value={formData.MonthlyCharges} onChange={handleChange} className={inputClass} min="0" />
            </div>
            <div>
              <label htmlFor="TotalCharges" className={labelClass}>Total Charges</label>
              <input id="TotalCharges" type="number" step="0.01" name="TotalCharges" value={formData.TotalCharges} onChange={handleChange} className={inputClass} min="0" />
            </div>
            <div>
              <label htmlFor="PaperlessBilling" className={labelClass}>Paperless Billing</label>
              <select id="PaperlessBilling" name="PaperlessBilling" value={formData.PaperlessBilling} onChange={handleChange} className={inputClass}>
                <option value="No">No</option>
                <option value="Yes">Yes</option>
              </select>
            </div>
          </div>
        </div>
        {/* Additional Services */}
        <div className="mt-8 grid grid-cols-1 md:grid-cols-4 gap-4 bg-gray-50 p-4 rounded-lg">
          <div>
            <label htmlFor="TechSupport" className={labelClass}>Tech Support</label>
            <select id="TechSupport" name="TechSupport" value={formData.TechSupport} onChange={handleChange} className={inputClass}>
              <option value="No">No</option>
              <option value="Yes">Yes</option>
              <option value="No internet service">No internet service</option>
            </select>
          </div>
          <div>
            <label htmlFor="DeviceProtection" className={labelClass}>Device Protection</label>
            <select id="DeviceProtection" name="DeviceProtection" value={formData.DeviceProtection} onChange={handleChange} className={inputClass}>
              <option value="No">No</option>
              <option value="Yes">Yes</option>
              <option value="No internet service">No internet service</option>
            </select>
          </div>
          <div>
            <label htmlFor="StreamingTV" className={labelClass}>Streaming TV</label>
            <select id="StreamingTV" name="StreamingTV" value={formData.StreamingTV} onChange={handleChange} className={inputClass}>
              <option value="No">No</option>
              <option value="Yes">Yes</option>
              <option value="No internet service">No internet service</option>
            </select>
          </div>
          <div>
            <label htmlFor="StreamingMovies" className={labelClass}>Streaming Movies</label>
            <select id="StreamingMovies" name="StreamingMovies" value={formData.StreamingMovies} onChange={handleChange} className={inputClass}>
              <option value="No">No</option>
              <option value="Yes">Yes</option>
              <option value="No internet service">No internet service</option>
            </select>
          </div>
        </div>
        <div className="mt-8 flex justify-end">
          <button type="submit" disabled={isLoading} className={`flex items-center px-6 py-3 bg-primary-600 text-white font-bold rounded-lg shadow-lg hover:bg-primary-700 transition-all ${isLoading ? 'opacity-50' : ''}`}>
            {isLoading ? 'Predicting...' : 'Analyze Churn Risk'}
          </button>
        </div>
      </div>
    </form>
  );
};

export default CustomerForm;
