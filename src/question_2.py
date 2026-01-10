import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


def calc_correlation(df):
    grouped = df.groupby('Age')['Survival Time (months)'].mean().reset_index()
    
    r_val, p_val = stats.pearsonr(grouped['Age'], grouped['Survival Time (months)'])
    
    if p_val < 0.05:
        print(f"Conclusion: Even after grouping, a significant trend exists. (P-value: {p_val:.4f})")
    else:
        print(f"Conclusion: No significant trend exists. Age does not predict average survival. (P-value: {p_val:.4f})")
    print(f"Correlation (r) of averages: {r_val:.4f}")
        
    return grouped


def plot_result(grouped_df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Age', y='Survival Time (months)', data=grouped_df, color='blue', s=80)
    sns.lineplot(x='Age', y='Survival Time (months)', data=grouped_df, color='gray', alpha=0.3)
    plt.title('Average Survival Time by Age')
    plt.xlabel('Age at Diagnosis')
    plt.ylabel('Mean Survival Time (months)')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

