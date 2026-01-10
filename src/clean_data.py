import pandas as pd

def load_data(file_path):
    """
    Loads a dataset from a CSV file.
    
    param file_path: The string path to the CSV file.
    return: pd.DataFrame if loading is successful, None otherwise.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading file: {e}")
        return None
    

def clean_data(df):
    
    if df is None:
        return None
        
    df = df.copy()
    # Remove duplicate rows to ensure data integrity
    df = df.drop_duplicates()
    
    # Logic: If 'Time to Recurrence' exists -> Recurrence = 1. If it is NaN -> Recurrence = 0.
    # This creates our binary target variable for prediction.
    if "Time to Recurrence (months)" in df.columns:
        df["Recurrence"] = df["Time to Recurrence (months)"].notna().astype(int)
    
    # Fill missing values in 'Recurrence Site' with a placeholder instead of dropping them.
    if "Recurrence Site" in df.columns:
        df["Recurrence Site"] = df["Recurrence Site"].fillna("No Recurrence")
    
    return df