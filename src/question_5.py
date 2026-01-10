import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
import numpy as np


def get_tumor_stats(df):
    """
    Generates frequency and normalized percentage tables for tumor analysis.
    
    param df: Input DataFrame containing 'Tumor Type' and 'Tumor Grade'.
    return: A tuple containing (contingency_table, percentage_table).
    """
    contingency = pd.crosstab(df["Tumor Type"], df["Tumor Grade"])
    percentages = (
        pd.crosstab(df["Tumor Type"], df["Tumor Grade"], normalize="index") * 100
    )
    return contingency, percentages


def run_statistical_test(contingency_table):
    """
    Performs a Chi-Square test of independence on a contingency table.
    
    param contingency_table: Table of observed frequencies.
    return: The p-value resulting from the test.
    """
    chi2, p_val, dof, expected = chi2_contingency(contingency_table)
    if p_val < 0.05:
        print(f"Conclusion: Significant relationship found (p = {p_val:.4f})")
    else:
        print(f"Conclusion: No significant relationship found (p = {p_val:.4f})")
    
    return p_val


def calculate_cramers_v(contingency_table):
    """
    Calculates Cramer's V as an effect size measure for a Chi-Square test.
    
    param contingency_table: Table of observed frequencies.
    return: Cramer's V value (float).
    """
    chi2 = chi2_contingency(contingency_table)[0]
    n = contingency_table.sum().sum()
    rows, cols = contingency_table.shape
    phi2 = chi2 / n
    # Formula for Cramer's V accounts for the dimensions of the table
    v = np.sqrt(phi2 / min(rows - 1, cols - 1))
    print(f"Cramer's V calculated: {v:.4f}")
    
    return v


def distribution_plot(df):
    """
    Generates and saves a stacked bar chart showing the predictive 
    probability of tumor grade by type, with percentage labels.
    
    param df: Input DataFrame.
    """
    plt.figure(figsize=(10, 6))
    # Normalize by index to ensure each bar represents 100%
    plot_data = (
        pd.crosstab(df["Tumor Type"], df["Tumor Grade"], normalize="index") * 100
    )
    # Create the stacked bar chart
    ax = plot_data.plot(
        kind="bar",
        stacked=True,
        color=["#4dabf7", "#3bc9db", "#38d9a9", "#69db7c"],
        rot=0,
        ax=plt.gca(),
    )
    # Iterate through segments (patches) to add percentage text labels
    for p in ax.patches:
        width, height = p.get_width(), p.get_height()
        if height > 5: # Only display text if the segment is large enough
            x, y = p.get_xy()
            ax.text(
                x + width / 2,
                y + height / 2,
                f"{height:.1f}%",
                horizontalalignment="center",
                verticalalignment="center",
                fontsize=10,
                color="white",
                fontweight="bold",
            )
    # Add chart metadata and labels
    plt.title("Predictive Probability of Tumor Grade by Type", fontsize=14, pad=20)
    plt.ylabel("Probability", fontsize=12)
    plt.xlabel("Tumor Type", fontsize=12, labelpad=10)
    plt.legend(title="Predicted Grade", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    
    # manager = plt.get_current_fig_manager()
    # manager.window.wm_geometry("+200+100")
    
    plt.show()
