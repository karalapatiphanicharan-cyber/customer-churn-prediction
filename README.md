# Customer Churn Prediction Project - Phase 1

## Project Overview
This project aims to predict customer churn for a telecommunications company using the Telco Customer Churn dataset. Phase 1 focuses on setting up a professional project structure and performing a comprehensive Exploratory Data Analysis (EDA) to understand the factors driving customer attrition.

## Project Structure
```
.
├── data/                       # Dataset directory
├── notebooks/                  # Jupyter notebooks for experimentation
├── src/                        # Source code for scripts
│   ├── data_preprocessing.py   # Data loading and cleaning
│   ├── eda.py                  # EDA and visualization logic
│   └── utils.py                # Helper functions
│
├── reports/                    # Analysis reports
│   ├── figures/                # Saved visualizations
│   └── eda_report.md           # Detailed EDA findings
│
├── requirements.txt            # Project dependencies
├── .gitignore                  # Git ignore file
└── README.md                   # Project documentation
```

## Dataset Description
The dataset used is the **Telco Customer Churn** dataset.
- **Location:** `data/WA_Fn-UseC_-Telco-Customer-Churn.csv`
- **Rows:** 7,043
- **Columns:** 21
- **Target Variable:** `Churn` (Indicates whether the customer left within the last month)

## How to Run EDA
To run the Exploratory Data Analysis and generate visualizations:

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the EDA Script:**
   ```bash
   python3 src/eda.py
   ```
   This script will:
   - Load and clean the data.
   - Perform missing value and duplicate analysis.
   - Generate visualizations in `reports/figures/`.
   - Print status messages to the console.

## Phase 1 Deliverables
- [x] Professional project structure
- [x] Data cleaning and preprocessing logic (with duplicate analysis)
- [x] Comprehensive EDA with visualizations
- [x] Detailed EDA report
- [x] Modular and reusable Python scripts
