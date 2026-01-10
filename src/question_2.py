import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


def calc_correlation(df):
    # Group data by age to calculate the mean survival time for each age year.
    grouped = df.groupby('Age')['Survival Time (months)'].mean().reset_index()
    
    # Calculate Pearson correlation coefficient (r) and p-value.
    r_val, p_val = stats.pearsonr(grouped['Age'], grouped['Survival Time (months)'])
    
    # Determine statistical significance (threshold: 0.05).
    if p_val < 0.05:
        print(f"Conclusion: Even after grouping, a significant trend exists. (P-value: {p_val:.4f})")
    else:
        print(f"Conclusion: No significant trend exists. Age does not predict average survival. (P-value: {p_val:.4f})")
    print(f"Correlation (r) of averages: {r_val:.4f}")
        
    return grouped


def plot_result(grouped_df):
    plt.figure(figsize=(10, 6))
    
    # Create a scatter plot for data points.
    sns.scatterplot(x='Age', y='Survival Time (months)', data=grouped_df, color='blue', s=80)
    
    # Overlay a line plot to visualize the trend.
    sns.lineplot(x='Age', y='Survival Time (months)', data=grouped_df, color='gray', alpha=0.3)
    
    plt.title('Average Survival Time by Age')
    plt.xlabel('Age at Diagnosis')
    plt.ylabel('Mean Survival Time (months)')
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # Fix the window position to avoid visual jumping on screen.
    manager = plt.get_current_fig_manager()
    manager.window.wm_geometry("+200+100")
    
    plt.show()

