
# Insurance Risk Analysis – Task 3: Hypothesis Testing

## Overview

This branch contains the analysis for Task 3, focused on applying hypothesis testing to identify significant factors affecting insurance risk and claims. The objective is to validate assumptions, detect relationships between key variables, and provide actionable insights for risk modeling.

## Dataset

* Customer demographic information, policy details, and claim history.
* Key features include age, policy type, claim amount, and previous claims.
* Large datasets (e.g., `MachineLearningRating_v3.txt`) are managed via DVC to maintain repository performance and avoid GitHub size limits.

## Methodology

* Hypotheses were formulated based on domain knowledge and exploratory analysis.
* Statistical tests applied:

  * t-tests for two-group comparisons
  * ANOVA for multi-group comparisons
  * Chi-square tests for categorical variables
* Significance level: α = 0.05
* Tools: Python (Pandas, NumPy, SciPy, Seaborn), Jupyter Notebook.

## Key Findings

* Age, policy type, and prior claims significantly influence insurance risk.
* Younger and older customers tend to have higher risk ratings.
* Comprehensive policies are associated with higher average claim amounts.
* Customers with previous claims are more likely to exhibit elevated risk ratings.

## Repository Structure

```
Insurance_risk_analysis/
│
├─ notebooks/
│   └─ Hypothesis_Tests.ipynb      # Task 3 Jupyter Notebook
│
├─ data/                           # Raw data folder excluded from Git (handled by DVC)
│
├─ .gitignore                      # Ignored files including DVC cache and raw data
└─ README.md                       # This file
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/Newaznezif/Insurance_risk_analysis.git
```

2. Switch to the Task 3 branch:

```bash
git checkout task-3
```

3. Open the notebook `notebooks/Hypothesis_Tests.ipynb` in Jupyter for the full analysis.
4. DVC is used to retrieve large datasets if needed.

## Recommendations

* Use identified risk factors for predictive modeling in subsequent tasks.
* Maintain DVC for large file management.
* Update notebooks and analyses for reproducibility.

## License

This project is for internal academic and professional purposes.


