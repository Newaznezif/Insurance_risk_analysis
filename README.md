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

* Understand the insurance dataset and its structure
* Conduct Exploratory Data Analysis (EDA) to identify patterns in risk and profitability
* Perform preliminary statistical analysis and visualize trends
* Prepare for predictive modeling of TotalClaims and optimal premiums

---

## Data

**Source:** MachineLearningRating_v3.txt
**Path:** `data/raw/MachineLearningRating_v3.txt`

**Key Features:**

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

**Pending:**

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
