import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class FeatureEngineer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        df = X.copy()

        # 1. tenure_group
        bins = [0, 12, 24, 36, 48, 60, 72]
        labels = ['0-12', '12-24', '24-36', '36-48', '48-60', '60-72']
        df['tenure_group'] = pd.cut(df['tenure'], bins=bins, labels=labels, include_lowest=True)
        df['tenure_group'] = df['tenure_group'].astype(object)

        # 2. avg_monthly_spend
        df['avg_monthly_spend'] = df['TotalCharges'] / (df['tenure'].replace(0, 1))

        # 3. total_services
        service_cols = ['PhoneService', 'MultipleLines', 'OnlineSecurity', 'OnlineBackup',
                        'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']
        existing_service_cols = [c for c in service_cols if c in df.columns]
        df['total_services'] = (df[existing_service_cols] == 'Yes').sum(axis=1)

        # 4. contract_type_risk
        contract_risk_map = {'Month-to-month': 2, 'One year': 1, 'Two year': 0}
        if 'Contract' in df.columns:
            df['contract_type_risk'] = df['Contract'].map(contract_risk_map).fillna(1)
        else:
            df['contract_type_risk'] = 1

        # 5. customer_value_segment
        if hasattr(self, 'monthly_charges_bins'):
             df['customer_value_segment'] = pd.cut(df['MonthlyCharges'], bins=self.monthly_charges_bins, labels=['Low', 'Medium', 'High'], include_lowest=True)
        else:
             df['customer_value_segment'] = 'Medium'

        df['customer_value_segment'] = df['customer_value_segment'].astype(object)

        return df

    def fit_transform(self, X, y=None):
        _, self.monthly_charges_bins = pd.qcut(X['MonthlyCharges'], q=3, retbins=True, labels=['Low', 'Medium', 'High'])
        self.monthly_charges_bins[0] = -np.inf
        self.monthly_charges_bins[-1] = np.inf
        return self.transform(X)
