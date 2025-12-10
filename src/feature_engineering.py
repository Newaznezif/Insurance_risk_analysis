# src/feature_engineering.py
def add_features(df):
    """Add new features if required columns exist"""
    if df is None or df.empty:
        print("DataFrame is empty or None, cannot add features")
        return df
    if "TotalClaims" not in df.columns or "TotalPremium" not in df.columns:
        print("Required columns missing")
        return df
    df["LossRatio"] = df["TotalClaims"] / df["TotalPremium"]
    return df
