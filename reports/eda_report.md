# Telco Customer Churn - Exploratory Data Analysis Report

## 1. Dataset Overview
The dataset contains 7,043 records of customers from a telecommunications company. Each record includes information about customer demographics, services, account information, and whether they churned (left the company).

- **Shape:** 7,043 rows, 21 columns
- **Target Variable:** `Churn` (Yes/No)
- **Key Features:** `tenure`, `MonthlyCharges`, `TotalCharges`, `Contract`, `InternetService`, `PaymentMethod`.

## 2. Data Quality Analysis
- **Missing Values:** No missing values were found in the original columns, except for `TotalCharges` which contained 11 empty strings. These were converted to numeric and filled with 0 (as they corresponded to new customers with 0 tenure).
- **Duplicate Records:** 0 duplicate records were found in the dataset.

## 3. Key Statistics
- **Churn Rate:** Approximately 26.5% of customers have churned.
- **Tenure:** The average tenure is about 32 months, with a high concentration of customers at both low (0-5 months) and high (65-72 months) tenure.
- **Monthly Charges:** Ranging from $18.25 to $118.75, with an average of $64.76.
- **Total Charges:** Ranges from $0 to $8,684.80.

## 4. Important Churn Insights
- **Contract Type:** Customers with **Month-to-month** contracts have a significantly higher churn rate compared to those with one or two-year contracts.
- **Tenure:** There is a strong negative correlation between tenure and churn; new customers are much more likely to churn.
- **Internet Service:** Fiber optic users show a higher churn rate than DSL or No-internet users, despite potentially higher speeds.
- **Payment Method:** Customers using **Electronic check** as a payment method churn more frequently than those using mailed checks or automatic payments.
- **Monthly Charges:** Higher monthly charges are generally associated with a higher likelihood of churn.

## 5. Business Observations
- The high churn rate among month-to-month customers suggests that providing incentives for longer-term contracts could improve retention.
- The high churn rate for Fiber optic users might indicate issues with service quality or pricing relative to the competition.
- New customers are vulnerable; early engagement strategies (first 6 months) are crucial.

## 6. Potential Predictive Features
Based on the EDA, the following features appear most promising for predicting churn:
1. `Contract` (especially Month-to-month)
2. `tenure`
3. `MonthlyCharges`
4. `InternetService` (Fiber optic)
5. `PaymentMethod` (Electronic check)
6. `OnlineSecurity` and `TechSupport` (customers without these services tend to churn more)

## 7. Visualizations
All generated plots can be found in the `reports/figures/` directory:
- `churn_distribution.png`: Overall churn rate.
- `numerical_distributions.png`: Distributions of tenure and charges.
- `categorical_distributions.png`: Churn breakdown by demographic and service features.
- `tenure_by_churn.png`: Density plot showing how tenure affects churn.
- `correlation_heatmap.png`: Relationships between numerical features.
