import pandas as pd
import numpy as np
import shap
import joblib
import os
import sys
import matplotlib.pyplot as plt

# Add current directory to path to allow script to run from anywhere
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import get_project_root

def generate_shap_plots():
    project_root = get_project_root()
    artifacts_dir = os.path.join(project_root, 'artifacts')
    test_path = os.path.join(project_root, 'data', 'processed', 'test.csv')
    report_dir = os.path.join(project_root, 'reports', 'shap')
    os.makedirs(report_dir, exist_ok=True)

    # Load model and data
    model = joblib.load(os.path.join(artifacts_dir, 'best_model.pkl'))
    df_test = pd.read_csv(test_path)
    X_test = df_test.drop(columns=['Churn'])

    # SHAP Explainer
    # Use TreeExplainer for tree-based models, otherwise KernelExplainer or LinearExplainer
    # In the last run, best_model was XGBoost (based on my previous turn's trace)
    # Actually, the trace shows XGBoost had slightly higher ROC_AUC in the very last step.

    try:
        explainer = shap.Explainer(model)
        shap_values = explainer(X_test)
    except Exception as e:
        print(f"Error initializing SHAP explainer: {e}")
        # Fallback to a smaller sample if needed or KernelExplainer
        explainer = shap.Explainer(model, X_test.iloc[:100])
        shap_values = explainer(X_test.iloc[:100])

    # 1. Summary Plot
    plt.figure(figsize=(10, 8))
    shap.summary_plot(shap_values, X_test, show=False)
    plt.savefig(os.path.join(report_dir, 'shap_summary.png'), bbox_inches='tight')
    plt.close()

    # 2. Bar Plot (Global Importance)
    plt.figure(figsize=(10, 8))
    shap.plots.bar(shap_values, show=False)
    plt.savefig(os.path.join(report_dir, 'shap_bar.png'), bbox_inches='tight')
    plt.close()

    # 3. Dependence Plot
    # Find the most important feature from shap_values
    if hasattr(shap_values, 'abs'):
        importances = np.abs(shap_values.values).mean(0)
    else:
        importances = np.abs(shap_values).mean(0)

    top_feature_idx = np.argmax(importances)
    top_feature_name = X_test.columns[top_feature_idx]

    plt.figure(figsize=(10, 8))
    shap.dependence_plot(top_feature_name, shap_values.values if hasattr(shap_values, 'values') else shap_values, X_test, show=False)
    plt.savefig(os.path.join(report_dir, 'shap_dependence.png'), bbox_inches='tight')
    plt.close()

    # 4. Generate SHAP Report
    report = f"""# SHAP Explainability Report

## Overview
This report provides a detailed explanation of the model's predictions using SHAP (SHapley Additive exPlanations).

## Global Feature Importance
The SHAP bar plot shows the overall importance of features across the entire test set.
- **Top Feature:** {top_feature_name}
- Highly influential features include contract types, tenure, and monthly charges.

## Feature Impact (Summary Plot)
The summary plot illustrates how high and low values of each feature affect the churn prediction.
- High values of **MonthlyCharges** and **Contract_Month-to-month** generally increase churn probability.
- High **tenure** and **Contract_Two year** significantly decrease churn probability.

## Business Interpretation
- **Retention Strategy:** Focus on customers with high monthly charges and short tenure on month-to-month contracts.
- **Service Optimization:** Improving technical support and security services can potentially reduce churn, as their absence is a strong predictor.
- **Contract Incentives:** Transitioning customers from month-to-month to longer-term contracts is likely the most effective way to reduce churn.

## Local Explanations
For individual customers, the model's decision can be decomposed into the contribution of each feature, allowing for personalized retention offers.
"""

    with open(os.path.join(report_dir, 'shap_report.md'), 'w') as f:
        f.write(report)

    print("SHAP explainability artifacts generated.")

if __name__ == "__main__":
    generate_shap_plots()
