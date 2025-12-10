### **Task 1 – Data Understanding & Exploratory Data Analysis**

**Project:** Insurance Risk Analysis & Predictive Modeling
**Organization:** AlphaCare Insurance Solutions (ACIS)
**Branch:** task-1
**Author:** Newaz Nezif
**Date:** 12/4/2025

**Project Overview:**
Task 1 focused on analyzing historical car insurance claims data from South Africa to uncover low-risk segments and optimize insurance premiums. The goal was to help AlphaCare Insurance Solutions target profitable clients and tailor marketing strategies effectively.

**Objectives:**

* Understand the insurance dataset and its structure
* Conduct Exploratory Data Analysis (EDA) to identify patterns in risk and profitability
* Perform preliminary statistical analysis and visualize trends
* Prepare for predictive modeling of TotalClaims and optimal premiums

**Data Source:**

* Filename: MachineLearningRating_v3.txt
* Path: data/raw/MachineLearningRating_v3.txt

**Key Features:**

* **Insurance Policy:** UnderwrittenCoverID, PolicyID, TransactionMonth
* **Client Info:** Gender, MaritalStatus, Bank, AccountType
* **Location:** Province, PostalCode, MainCrestaZone, SubCrestaZone
* **Vehicle Info:** VehicleType, Make, Model, Kilowatts, Cubiccapacity
* **Plan & Payment:** SumInsured, CalculatedPremiumPerTerm, TotalPremium, TotalClaims

**Folder Structure:**

```
Insurance_risk_analysis/
│ README.md
│ requirements.txt
│ setup.sh
├───data/
│   └───raw/
│       MachineLearningRating_v3.txt
├───notebooks/
│   EDA.ipynb
│   Hypothesis_Tests.ipynb
│   Modeling.ipynb
│   README.md
├───reports/
│   interim_report.md
│   plots/
└───src/
    data_preprocessing.py
    feature_engineering.py
    model_building.py
    model_evaluation.py
    utils.py
```

**Setup Instructions:**

1. Clone the repository:

   ```bash
   git clone https://github.com/Newaznezif/Insurance_risk_analysis.git
   cd Insurance_risk_analysis
   ```
2. Create a Python virtual environment:

   ```bash
   python -m venv env
   .\env\Scripts\activate   # Windows
   source env/bin/activate  # macOS/Linux
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. (Optional) Set up DVC for large data tracking:

   ```bash
   dvc add data/raw/MachineLearningRating_v3.txt
   git add data/raw/MachineLearningRating_v3.txt.dvc
   git commit -m "Track raw dataset with DVC"
   ```

**Progress – Task 1 Completed:**

* Git repository initialized with task-based branches (`task-1`)
* Dataset added and versioned using DVC
* EDA completed with histograms, bar plots, correlation matrices, and outlier detection
* Descriptive statistics and key insights generated
* Interim report prepared and saved in `reports/interim_report.md`

**Pending:**

* CI/CD via GitHub Actions (optional)
* Task 2: modeling and hypothesis testing

**Key Insights from EDA:**

* Loss ratio (TotalClaims / TotalPremium) varies by Province, VehicleType, and Gender
* Certain postal codes and vehicle makes/models have higher claims
* Outliers detected in TotalClaims and CustomValueEstimate
* Temporal trends show variation in claims over 18 months




### **Task 2 – Predictive Modeling & Hypothesis Testing**

**Project:** Insurance Risk Analysis & Predictive Modeling
**Organization:** AlphaCare Insurance Solutions (ACIS)
**Branch:** task-2
**Author:** Newaz Nezif
**Date:** 12/5/2025

**Project Overview:**
Task 2 focused on building predictive models for insurance claims and premiums, along with conducting statistical hypothesis testing to validate risk factors identified during Task 1. This helped in estimating expected claims and optimizing premium pricing for different customer segments.

**Objectives:**

* Conduct hypothesis testing to confirm relationships between features and TotalClaims
* Engineer relevant features for predictive modeling
* Build regression and classification models for predicting claims and premium optimization
* Evaluate model performance using metrics such as RMSE, MAE, and R²

**Data Source:**

* Cleaned and preprocessed dataset from Task 1
* Relevant features selected based on EDA insights

**Progress – Task 2 Completed:**

* Hypotheses tested using statistical tests (t-tests, ANOVA, chi-square)
* Feature engineering performed: encoding categorical variables, scaling numeric features
* Regression models built to predict TotalClaims and expected premium
* Model performance evaluated, results visualized and interpreted
* Notebook `Hypothesis_Tests.ipynb` documents testing results and conclusions
* Modeling notebook `Modeling.ipynb` includes predictive analysis workflows

**Key Insights from Task 2:**

* Gender, VehicleType, and Province significantly influence TotalClaims
* Certain vehicle makes and models consistently exhibit higher risk
* Regression models show acceptable predictive performance for premium estimation
* Insights from hypothesis tests support strategic premium adjustments for low- and high-risk segments

**Pending / Next Steps:**

* Refine models for deployment (Task 3)
* Integrate insights into company dashboards for business use




# Insurance Risk Analysis & Predictive Modeling Task 4

**Project:** End-to-End Insurance Risk Analytics & Predictive Modeling
**Organization:** AlphaCare Insurance Solutions (ACIS)
**Branch for Task 1:** task-1
**Author:** Newaz Nezif
**Date:** 12/4/2025

---

## Project Overview

This project focuses on analyzing historical car insurance claims data from South Africa to identify low-risk segments and optimize insurance premiums. The goal is to enable AlphaCare Insurance Solutions to target profitable clients and tailor marketing strategies effectively.

---

## Objectives

* Customer demographic information, policy details, and claim history.
* Key features include age, policy type, claim amount, and previous claims.
* Large datasets (e.g., `MachineLearningRating_v3.txt`) are managed via DVC to maintain repository performance and avoid GitHub size limits.

---

## Data

**Source:** MachineLearningRating_v3.txt
**Path:** `data/raw/MachineLearningRating_v3.txt`

  * t-tests for two-group comparisons
  * ANOVA for multi-group comparisons
  * Chi-square tests for categorical variables
* Significance level: α = 0.05
* Tools: Python (Pandas, NumPy, SciPy, Seaborn), Jupyter Notebook.

* **Insurance Policy:** UnderwrittenCoverID, PolicyID, TransactionMonth
* **Client Info:** Gender, MaritalStatus, Bank, AccountType …
* **Location:** Province, PostalCode, MainCrestaZone, SubCrestaZone
* **Vehicle Info:** VehicleType, Make, Model, Kilowatts, Cubiccapacity …
* **Plan & Payment:** SumInsured, CalculatedPremiumPerTerm, TotalPremium, TotalClaims

---

## Folder Structure

```
Insurance_risk_analysis/
│ README.md
│ requirements.txt
│ setup.sh
├───data/
│   └───raw/
│       MachineLearningRating_v3.txt
│
├───notebooks/
│   EDA.ipynb
│   Hypothesis_Tests.ipynb
│   Modeling.ipynb
│   README.md
├───reports/
│   interim_report.md
│   plots/
└───src/
    data_preprocessing.py
    feature_engineering.py
    model_building.py
    model_evaluation.py
    utils.py
```

---

## Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/Newaznezif/Insurance_risk_analysis.git
cd Insurance_risk_analysis
```

2. **Create a Python virtual environment:**

```bash
python -m venv env
.\env\Scripts\activate    # Windows
# OR
source env/bin/activate   # macOS/Linux
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **(Optional) Set up DVC to track large data:**

```bash
dvc add data/raw/MachineLearningRating_v3.txt
git add data/raw/MachineLearningRating_v3.txt.dvc
git commit -m "Track raw dataset with DVC"
```

---

## Progress

**Task 1 – Completed:**

* Git repository initialized with branches for task-based workflow (task-1)
* Dataset added and versioned using DVC
* Exploratory Data Analysis (EDA) completed with histograms, bar plots, correlation matrices, and outlier detection
* Descriptive statistics and key insights generated
* Interim report prepared and saved in `reports/interim_report.md`

## License

* CI/CD via GitHub Actions (optional)
* Task 2 modeling and hypothesis testing

---

## Key Insights from EDA

* Loss ratio (`TotalClaims / TotalPremium`) varies by Province, VehicleType, and Gender
* Certain postal codes and vehicle makes/models have higher claims
* Outliers detected in TotalClaims and CustomValueEstimate
* Temporal trends show variation in claims over 18 months

---

## License

This project is for internal academic and professional purposes.


Do you want me to do that next?
