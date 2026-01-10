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
    df = df.drop_duplicates()
    
    if "Time to Recurrence (months)" in df.columns:
        df["Recurrence"] = df["Time to Recurrence (months)"].notna().astype(int)
    
    if "Recurrence Site" in df.columns:
        df["Recurrence Site"] = df["Recurrence Site"].fillna("No Recurrence")

    critical_features = ["Tumor Location", "Tumor Grade", "Tumor Type", "Treatment", "Age"]
    existing_features = [col for col in critical_features if col in df.columns]
    df = df.dropna(subset=existing_features)
    
    return df