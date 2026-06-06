# SHAP Explainability Report

## Overview
This report provides a detailed explanation of the model's predictions using SHAP (SHapley Additive exPlanations).

## Global Feature Importance
The SHAP bar plot shows the overall importance of features across the entire test set.
- **Top Feature:** contract_type_risk
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
