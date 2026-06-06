# Feature Analysis Report

## Overview
This report analyzes the features prepared for the Customer Churn Prediction model.

## Correlation Observations
Top 10 features positively correlated with Churn:
|                                |    Churn |
|:-------------------------------|---------:|
| Churn                          | 1        |
| Contract_Month-to-month        | 0.404901 |
| contract_type_risk             | 0.395851 |
| OnlineSecurity_No              | 0.344374 |
| TechSupport_No                 | 0.337472 |
| InternetService_Fiber optic    | 0.318983 |
| tenure_group_0-12              | 0.315865 |
| PaymentMethod_Electronic check | 0.304681 |
| OnlineBackup_No                | 0.266778 |
| DeviceProtection_No            | 0.247672 |
| MonthlyCharges                 | 0.204177 |

Top 10 features negatively correlated with Churn:
|                                      |     Churn |
|:-------------------------------------|----------:|
| tenure                               | -0.344457 |
| Contract_Two year                    | -0.300531 |
| OnlineSecurity_No internet service   | -0.234432 |
| StreamingTV_No internet service      | -0.234432 |
| TechSupport_No internet service      | -0.234432 |
| DeviceProtection_No internet service | -0.234432 |
| OnlineBackup_No internet service     | -0.234432 |
| InternetService_No                   | -0.234432 |
| StreamingMovies_No internet service  | -0.234432 |
| tenure_group_60-72                   | -0.221251 |

## Feature Importance (Random Forest)
Top 15 features by importance:
|                                |         0 |
|:-------------------------------|----------:|
| TotalCharges                   | 0.115962  |
| tenure                         | 0.10273   |
| MonthlyCharges                 | 0.0999761 |
| avg_monthly_spend              | 0.0994502 |
| contract_type_risk             | 0.0348211 |
| Contract_Month-to-month        | 0.034376  |
| TechSupport_No                 | 0.0281134 |
| total_services                 | 0.0255567 |
| OnlineSecurity_No              | 0.0245909 |
| tenure_group_0-12              | 0.0227023 |
| PaymentMethod_Electronic check | 0.022011  |
| InternetService_Fiber optic    | 0.0211568 |
| OnlineBackup_No                | 0.015198  |
| gender_Female                  | 0.0149543 |
| gender_Male                    | 0.014247  |

## Potential Leakage Checks
- Features with extremely high correlation (>0.95) with target: None found
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
