# src/model_building.py
from sklearn.linear_model import LinearRegression

def train_model(X, y):
    """Train a Linear Regression model"""
    if X is None or y is None or len(X) == 0:
        print("Invalid input for training")
        return None
    try:
        model = LinearRegression()
        model.fit(X, y)
        return model
    except Exception as e:
        print(f"Model training failed: {e}")
        return None
