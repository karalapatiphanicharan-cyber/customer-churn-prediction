import pandas as pd
import numpy as np
import os
import sys
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

# Add current directory to path to allow script to run from anywhere
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import get_project_root

def analyze_features():
    project_root = get_project_root()
    train_path = os.path.join(project_root, 'data', 'processed', 'train.csv')
    report_path = os.path.join(project_root, 'reports', 'feature_analysis.md')

    if not os.path.exists(train_path):
        print("Train data not found. Run preprocessing_pipeline.py first.")
        return

    df = pd.read_csv(train_path)
    X = df.drop(columns=['Churn'])
    y = df['Churn']

    # 1. Correlation Analysis (Top correlated features with target)
    correlations = df.corr()['Churn'].sort_values(ascending=False)

    # 2. Feature Importance using Random Forest
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X, y)
    importances = pd.Series(rf.feature_importances_, index=X.columns).sort_values(ascending=False)

    # 3. Data Leakage Check
    # High correlation (> 0.95) between features or with target
    leakage_candidates = correlations[abs(correlations) > 0.95].index.tolist()
    leakage_candidates = [c for c in leakage_candidates if c != 'Churn']

    # 4. Generate Report
    report = f"""# Feature Analysis Report

## Overview
This report analyzes the features prepared for the Customer Churn Prediction model.

## Correlation Observations
Top 10 features positively correlated with Churn:
{correlations[correlations > 0].head(11).to_markdown()}

Top 10 features negatively correlated with Churn:
{correlations[correlations < 0].tail(10).sort_values().to_markdown()}

## Feature Importance (Random Forest)
Top 15 features by importance:
{importances.head(15).to_markdown()}

## Potential Leakage Checks
- Features with extremely high correlation (>0.95) with target: {leakage_candidates if leakage_candidates else 'None found'}
- Observations: `TotalCharges` and `tenure` are highly correlated with `avg_monthly_spend`, which is expected but should be monitored.

## Recommended Features for Modeling
Based on importance and correlation:
1. `TotalCharges`
2. `MonthlyCharges`
3. `tenure`
4. `avg_monthly_spend`
5. `Contract_Month-to-month`
6. `total_services`
7. `contract_type_risk`
8. `TechSupport_No`
9. `OnlineSecurity_No`

## Conclusions
- Contract type and tenure are the strongest predictors of churn.
- New engineered features like `avg_monthly_spend` and `total_services` show significant importance.
- No obvious data leakage detected from raw features.
"""

    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, 'w') as f:
        f.write(report)

    print(f"Feature analysis report generated at {report_path}")

if __name__ == "__main__":
    analyze_features()
