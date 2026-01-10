import matplotlib.pyplot as plt
import pytest
import pandas as pd
from src.question_5 import get_tumor_stats, run_statistical_test, distribution_plot, calculate_cramers_v

def test_get_tumor_stats():
    """Test the calculation of contingency tables and row percentages."""
    data = {
        'Tumor Type': ['Meningioma', 'Meningioma', 'Glioblastoma'],
        'Tumor Grade': ['I', 'I', 'IV']
    }
    df = pd.DataFrame(data)
    contingency, percentages = get_tumor_stats(df)
    
    # Assert specific count for a specific category
    assert contingency.loc['Meningioma', 'I'] == 2
    # Assert percentage logic (Meningioma grade I is 100% of its type in this sample)
    assert percentages.loc['Meningioma', 'I'] == 100.0
    # Ensure row percentages sum to 100 using approx to handle floating point noise
    assert percentages.sum(axis=1).iloc[0] == pytest.approx(100.0)

def test_run_statistical_test_strong_relation():
    """Ensure the statistical test identifies high correlation with a low p-value."""
    table = [[100, 0], [0, 100]]
    p_val = run_statistical_test(table)
    assert p_val < 0.05
    
def test_calculate_cramers_v():
    """Validate Cramer's V for both perfect correlation and total independence."""
    # Case 1: Perfect correlation (Value should be 1.0)
    perfect_table = pd.DataFrame([[50, 0, 0],
        [0, 50, 0],
        [0, 0, 50]])
    v = calculate_cramers_v(perfect_table)
    assert v == pytest.approx(1.0)
    # Case 2: No relationship (Value should be 0.0)
    no_relation = pd.DataFrame([[25, 25], [25, 25]])
    v_zero = calculate_cramers_v(no_relation)
    # Using abs=1e-7 because floating point math often returns tiny non-zero values
    assert v_zero == pytest.approx(0.0, abs=1e-7)

def test_distribution_plot():
    """Verify that the plotting function executes and generates a figure object."""
    df = pd.DataFrame({
        "Tumor Type": ["Meningioma", "Glioblastoma"],
        "Tumor Grade": ["I", "IV"]
    })
    
    # Switch to 'Agg' backend to allow testing without a GUI (headless mode)
    plt.switch_backend('Agg')
    
    try:
        distribution_plot(df)
        fig = plt.gcf()
        # Check if the plot actually contains axes
        assert len(fig.axes) > 0 
        plt.close(fig)
    except Exception as e:
        # If the function crashes, explicitly fail the test
        pytest.fail(f"distribution_plot raised an error: {e}")