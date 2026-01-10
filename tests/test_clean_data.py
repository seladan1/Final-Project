import pytest
import pandas as pd
import numpy as np
from src.clean_data import clean_data

@pytest.fixture
def raw_data():
    """ Create a mock dataset covering various edge cases:
    - Duplicates (ID 1)
    - Missing critical values (Age in row 3)
    - Missing recurrence time (Healthy patient in row 2)
    """
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
    # Ensure that duplicate rows are removed.
    df_clean = clean_data(raw_data)
    assert len(df_clean) == 4


def test_recurrence_logic_creation(raw_data):
    """ Verify that the 'Recurrence' column is created correctly:
    1 = Recurrence occurred (Time is not NaN)
    0 = No recurrence (Time is NaN)
    """
    df_clean = clean_data(raw_data)
    
    assert 'Recurrence' in df_clean.columns

    row_with_recurrence = df_clean[df_clean['Patient ID'] == 1].iloc[0]
    row_healthy = df_clean[df_clean['Patient ID'] == 2].iloc[0]
    
    assert row_with_recurrence['Recurrence'] == 1
    assert row_healthy['Recurrence'] == 0


def test_recurrence_site_fill(raw_data):
    # Verify that NaN in 'Recurrence Site' is filled with 'No Recurrence'.
    df_clean = clean_data(raw_data)
    
    row_healthy = df_clean[df_clean['Patient ID'] == 2].iloc[0]
    assert row_healthy['Recurrence Site'] == 'No Recurrence'


def test_healthy_patients_kept(raw_data):
    # CRITICAL TEST: Ensure patients with NaN in 'Time to Recurrence' are NOT dropped.
    df_clean = clean_data(raw_data)
    
    # Patient 2 had NaN recurrence time, they must remain in the dataset.
    assert 2 in df_clean['Patient ID'].values
    assert pd.isna(df_clean[df_clean['Patient ID'] == 2]['Time to Recurrence (months)'].iloc[0])

def test_none_input():
    # Handle None input gracefully.
    assert clean_data(None) is None