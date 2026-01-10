import pytest
import pandas as pd
import numpy as np
from src.clean_data import clean_data

@pytest.fixture
def raw_data():
    return pd.DataFrame({
        'Patient ID': [1, 2, 3, 4, 1], 
        'Age': [50, 60, np.nan, 45, 50], 
        'Tumor Type': ['Glioblastoma', 'Meningioma', 'Astrocytoma', 'Meningioma', 'Glioblastoma'],
        'Tumor Grade': ['IV', 'I', 'II', 'I', 'IV'],
        'Tumor Location': ['Frontal', 'Parietal', 'Temporal', 'Occipital', 'Frontal'],
        'Treatment': ['Surgery', 'Surgery', 'Chemo', 'Radiation', 'Surgery'],
        'Time to Recurrence (months)': [10.0, np.nan, 15.0, np.nan, 10.0],
        'Recurrence Site': ['Temporal', np.nan, 'Frontal', np.nan, 'Temporal']
    })

def test_remove_duplicates(raw_data):
    df_clean = clean_data(raw_data)
    assert len(df_clean) == 3 

def test_recurrence_logic_creation(raw_data):
    df_clean = clean_data(raw_data)
    
    assert 'Recurrence' in df_clean.columns

    row_with_recurrence = df_clean[df_clean['Patient ID'] == 1].iloc[0]
    row_healthy = df_clean[df_clean['Patient ID'] == 2].iloc[0]
    
    assert row_with_recurrence['Recurrence'] == 1
    assert row_healthy['Recurrence'] == 0

def test_recurrence_site_fill(raw_data):
    df_clean = clean_data(raw_data)
    
    row_healthy = df_clean[df_clean['Patient ID'] == 2].iloc[0]
    assert row_healthy['Recurrence Site'] == 'No Recurrence'

def test_critical_missing_values_dropped(raw_data):
    df_clean = clean_data(raw_data)
    
    assert 3 not in df_clean['Patient ID'].values

def test_healthy_patients_kept(raw_data):
    df_clean = clean_data(raw_data)
    
    assert 2 in df_clean['Patient ID'].values
    assert pd.isna(df_clean[df_clean['Patient ID'] == 2]['Time to Recurrence (months)'].iloc[0])

def test_none_input():
    assert clean_data(None) is None