import pytest
import pandas as pd
from src.question_2 import calc_correlation

@pytest.fixture
def sample_data():
    # Create simple mock data for testing correlation logic.
    data = {
        'Age': [20, 20, 30, 30, 40, 50],
        'Survival Time (months)': [10, 20, 30, 40, 50, 60]
    }
    return pd.DataFrame(data)

def test_calc_correlation_grouping(sample_data):
    # Test if the function correctly groups data by Age and calculates means.
    result = calc_correlation(sample_data)
    
    # Check that duplicates ages were merged.
    assert len(result) == 4
    
    # Verify the mean calculation: Age 20 has values 10 and 20 -> Mean should be 15.
    avg_20 = result.loc[result['Age'] == 20, 'Survival Time (months)'].values[0]
    assert avg_20 == 15
    
def test_calc_correlation_columns(sample_data):
    # Ensure the output DataFrame has the required columns for plotting.
    result = calc_correlation(sample_data)
    assert 'Age' in result.columns
    assert 'Survival Time (months)' in result.columns
