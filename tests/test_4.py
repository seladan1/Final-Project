import pandas as pd
import numpy as np
from src.question_4 import outcome_distribution


def test_outcome_distribution_probabilities_sum_to_one_realistic():
    df = pd.DataFrame({
        "Treatment": [
            "Surgery", "Surgery", "Surgery",
            "Chemotherapy", "Chemotherapy",
            "Radiation"
        ],
        "Treatment Outcome": [
            "Improved", "Stable", "Improved",
            "Improved", "Worsened",
            "Stable"
        ]
    })

    probs = outcome_distribution(df)

    row_sums = probs.sum(axis=1)
    assert np.allclose(row_sums.values, 1.0)


def test_outcome_distribution_shape_realistic():
    df = pd.DataFrame({
        "Treatment": [
            "Surgery", "Surgery",
            "Chemotherapy", "Chemotherapy",
            "Radiation", "Radiation"
        ],
        "Treatment Outcome": [
            "Improved", "Stable",
            "Improved", "Worsened",
            "Stable", "Worsened"
        ]
    })

    probs = outcome_distribution(df)

    assert probs.shape == (3, 3)
