
# Risk-Based Pricing System - Model Files

## Generated on: 2025-12-10 18:46:06

## Model Files:
1. `severity_model.pkl` - Random Forest model for predicting claim severity
2. `probability_model.pkl` - Random Forest model for predicting claim probability
3. `preprocessor.pkl` - Data preprocessing pipeline for feature transformation

## How to Use:

```python
import joblib
import pandas as pd
import numpy as np

# Load models
severity_model = joblib.load('severity_model.pkl')
probability_model = joblib.load('probability_model.pkl')
preprocessor = joblib.load('preprocessor.pkl')

# Prepare new data (must have same features as training)
new_data = pd.DataFrame(...)  # Your new policy data

# Preprocess data
X_processed = preprocessor.transform(new_data)

# Make predictions
claim_probabilities = probability_model.predict_proba(X_processed)[:, 1]
claim_severities = severity_model.predict(X_processed)

# Calculate risk-based premium
expense_loading = 0.20  # 20% for expenses
profit_margin = 0.15    # 15% profit margin

base_premium = claim_probabilities * claim_severities
risk_based_premium = base_premium * (1 + expense_loading + profit_margin)

# Apply reasonable bounds (optional)
risk_based_premium = np.clip(risk_based_premium, 500, 20000)  # Min R500, Max R20,000
```

## Model Performance Summary:
--------------------------------------------------

### Claim Severity Models:
| Model | RMSE | R² | MAE |
|-------|------|----|-----|
| Linear Regression | 0.17 | 1.0000 | 0.03 |
| Ridge Regression | 28.42 | 1.0000 | 15.47 |
| Lasso Regression | 1.65 | 1.0000 | 0.67 |
| Decision Tree | 2411.45 | 0.9964 | 1027.76 |
| Random Forest | 870.00 | 0.9995 | 131.80 |
| XGBoost | 651.41 | 0.9997 | 135.40 |

**Best Severity Model:** Linear Regression (RMSE: 0.17, R²: 1.0000)

### Claim Probability Models:
| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|-------|----------|-----------|--------|----------|---------|
| Logistic Regression | 1.0000 | 0.9946 | 0.9982 | 0.9964 | 1.0000 |
| Decision Tree | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Random Forest | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| XGBoost | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |

**Best Probability Model:** Decision Tree (ROC-AUC: 1.0000, Accuracy: 1.0000)

## Data Statistics:
--------------------------------------------------
- Original dataset shape: (1000098, 52)
- Processed dataset shape: (1000098, 64)
- Policies with claims: 2788
- Overall claim rate: 0.002787726802773328

## Top Influential Features:
--------------------------------------------------
See feature_importance.png for visualization and model_results.json for detailed feature importance data.

## Business Implementation:
--------------------------------------------------
### Risk-Based Pricing Formula:
Premium = [P(Claim) × E(Severity|Claim)] × (1 + Expense Loading + Profit Margin)

### Recommended Implementation:
1. **Pilot Phase (Month 1-3):** Test with new business only
2. **Expansion Phase (Month 4-6):** Extend to policy renewals
3. **Full Implementation (Month 7-12):** Dynamic pricing for all policies

### Key Performance Indicators:
- Model Accuracy: RMSE < [industry benchmark], ROC-AUC > 0.85
- Business Impact: Loss ratio improvement, premium adequacy
- Operational Efficiency: Underwriting cycle time reduction

## Maintenance:
--------------------------------------------------
- Monitor model performance monthly
- Retrain models quarterly with new data
- Review feature importance annually
- Update premium bounds based on market conditions

## Support:
For questions or issues, refer to the comprehensive model evaluation report in '../reports/model_results.json'
