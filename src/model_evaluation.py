# src/model_evaluation.py
from sklearn.metrics import mean_squared_error

def evaluate_model(model, X_test, y_test):
    """Evaluate the model performance"""
    if model is None:
        print("No model provided")
        return None
    if X_test is None or y_test is None:
        print("Test data missing")
        return None
    try:
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        return mse
    except Exception as e:
        print(f"Evaluation failed: {e}")
        return None
