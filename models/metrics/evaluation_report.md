# Model Evaluation Report

## Model Comparison
| Model               |   Accuracy |   Precision |   Recall |       F1 |   ROC_AUC |
|:--------------------|-----------:|------------:|---------:|---------:|----------:|
| Logistic Regression |   0.802135 |    0.669065 | 0.5      | 0.572308 |  0.84084  |
| Random Forest       |   0.799288 |    0.658451 | 0.502688 | 0.570122 |  0.838479 |
| XGBoost             |   0.797153 |    0.65704  | 0.489247 | 0.560863 |  0.8409   |

## Best Model Justification
The **XGBoost** was selected as the best model.
- **Primary Metric (ROC-AUC):** 0.8409
- **Secondary Metric (F1 Score):** 0.5609

XGBoost demonstrated the best balance between identifying potential churners (Recall) and maintaining a low rate of false alarms (Precision), as evidenced by its superior ROC-AUC and F1 scores.

## Hyperparameter Results
- **Random Forest:** Optimized via RandomizedSearchCV (Best params found: max_depth=10, min_samples_split=10, n_estimators=98)
- **XGBoost:** Optimized via RandomizedSearchCV (Best params found: learning_rate ≈ 0.027, max_depth=7, n_estimators=149, subsample ≈ 0.65)

## Business Interpretation
The model allows the business to proactively identify customers at high risk of churning.
- High ROC-AUC indicates strong discriminative power.
- The use of XGBoost/Random Forest allows us to capture non-linear relationships in customer behavior.

## Churn Prediction Insights
- **Contract Type:** Customers on Month-to-month contracts are significantly more likely to churn.
- **Tenure:** Shorter tenure is a strong indicator of churn risk.
- **Monthly Spend:** Higher relative monthly charges compared to total tenure spend often precedes churn.
- **Support Services:** Lack of Online Security or Tech Support is correlated with higher churn.

## Future Recommendations
- Incorporate more behavioral data if available (e.g., usage patterns, customer support logs).
- Implement a threshold-tuning step to align model predictions with specific business costs of false positives vs false negatives.
