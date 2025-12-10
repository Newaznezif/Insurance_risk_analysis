# src/data_preprocessing.py
import pandas as pd

def load_data(file_path):
    """
    Load a CSV or text dataset and return a DataFrame.

    Parameters:
        file_path (str): Path to the dataset file

    Returns:
        pd.DataFrame or None
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: File at {file_path} is empty")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
