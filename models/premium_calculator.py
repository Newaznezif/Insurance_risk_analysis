
"""
Premium Calculator for Risk-Based Pricing System
Usage: python premium_calculator.py --data new_policies.csv --output premiums.csv
"""

import joblib
import pandas as pd
import numpy as np
import argparse
import sys

def load_models():
    """Load trained models and preprocessor"""
    try:
        severity_model = joblib.load('severity_model.pkl')
        probability_model = joblib.load('probability_model.pkl')
        preprocessor = joblib.load('preprocessor.pkl')
        return severity_model, probability_model, preprocessor
    except FileNotFoundError as e:
        print(f"Error loading models: {e}")
        print("Please ensure model files are in the current directory:")
        print("  - severity_model.pkl")
        print("  - probability_model.pkl")
        print("  - preprocessor.pkl")
        sys.exit(1)

def calculate_premiums(data, severity_model, probability_model, preprocessor,
                      expense_loading=0.20, profit_margin=0.15,
                      min_premium=500, max_premium=20000):
    """
    Calculate risk-based premiums for given policies
    
    Parameters:
    data: DataFrame with policy features
    severity_model: Trained severity prediction model
    probability_model: Trained probability prediction model
    preprocessor: Data preprocessing pipeline
    expense_loading: Expense percentage (default 20%)
    profit_margin: Profit percentage (default 15%)
    min_premium: Minimum premium amount
    max_premium: Maximum premium amount
    
    Returns:
    DataFrame with original data plus premium calculations
    """
    
    # Preprocess the data
    try:
        X_processed = preprocessor.transform(data)
    except Exception as e:
        print(f"Error preprocessing data: {e}")
        print("Ensure input data has the same features as training data")
        raise
    
    # Make predictions
    claim_probabilities = probability_model.predict_proba(X_processed)[:, 1]
    claim_severities = severity_model.predict(X_processed)
    
    # Calculate premiums
    base_premium = claim_probabilities * claim_severities
    total_loading = 1 + expense_loading + profit_margin
    risk_based_premium = base_premium * total_loading
    
    # Apply bounds
    risk_based_premium = np.clip(risk_based_premium, min_premium, max_premium)
    
    # Create results dataframe
    results = data.copy()
    results['claim_probability'] = claim_probabilities
    results['predicted_severity'] = claim_severities
    results['expected_loss'] = base_premium
    results['risk_based_premium'] = risk_based_premium
    results['risk_category'] = pd.cut(claim_probabilities, 
                                     bins=[0, 0.1, 0.3, 1.0],
                                     labels=['Low', 'Medium', 'High'])
    
    return results

def main():
    """Main function for command-line usage"""
    parser = argparse.ArgumentParser(description='Calculate risk-based premiums for insurance policies')
    parser.add_argument('--data', type=str, required=True, help='Path to input CSV file with policy data')
    parser.add_argument('--output', type=str, default='premiums_calculated.csv', help='Output CSV file path')
    parser.add_argument('--expense', type=float, default=0.20, help='Expense loading (default: 0.20)')
    parser.add_argument('--profit', type=float, default=0.15, help='Profit margin (default: 0.15)')
    parser.add_argument('--min', type=float, default=500, help='Minimum premium (default: 500)')
    parser.add_argument('--max', type=float, default=20000, help='Maximum premium (default: 20000)')
    
    args = parser.parse_args()
    
    print(f"Loading data from {args.data}...")
    try:
        data = pd.read_csv(args.data)
    except Exception as e:
        print(f"Error loading data: {e}")
        sys.exit(1)
    
    print(f"Loaded {len(data)} policies")
    print("Loading models...")
    severity_model, probability_model, preprocessor = load_models()
    
    print("Calculating premiums...")
    try:
        results = calculate_premiums(
            data, severity_model, probability_model, preprocessor,
            expense_loading=args.expense,
            profit_margin=args.profit,
            min_premium=args.min,
            max_premium=args.max
        )
    except Exception as e:
        print(f"Error calculating premiums: {e}")
        sys.exit(1)
    
    # Save results
    results.to_csv(args.output, index=False)
    print(f"Results saved to {args.output}")
    
    # Print summary
    print(f"
Premium Calculation Summary:")
    print(f"  Number of policies: {len(results)}")
    print(f"  Average premium: R{results['risk_based_premium'].mean():.2f}")
    print(f"  Premium range: R{results['risk_based_premium'].min():.2f} - R{results['risk_based_premium'].max():.2f}")
    print(f"  Risk distribution:")
    print(f"    Low risk: {(results['risk_category'] == 'Low').sum()} policies")
    print(f"    Medium risk: {(results['risk_category'] == 'Medium').sum()} policies")
    print(f"    High risk: {(results['risk_category'] == 'High').sum()} policies")

if __name__ == "__main__":
    main()
