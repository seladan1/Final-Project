import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr


def calc_spearman_gender_survival (df):
    # Calculates Spearman correlation and p-value between gender and survival time.
    
    df["Gender_num"] = df["Gender"].map({"Male": 1, "Female": 0})
    corr, p_value = spearmanr(df["Gender_num"], df["Survival Time (months)"])
    
    # Final conclusion.
    if abs(corr) < 0.2:
        strength = "very weak"
    elif abs(corr) < 0.4:
        strength = "weak"
    else:
        strength = "moderate to strong"

    significance = "statistically significant" if p_value < 0.05 else "not statistically significant"

    print(
        f"Conclusion: There is a {strength} relationship between gender and survival time, "
        f"and the result is {significance}."
    )
    
    print(f"Spearman correlation: {corr:.4f}")
    print(f"p-value: {p_value:.4f}")
    
    return corr, p_value


def plot_survival_by_gender(df):
    # Creates a box plot of survival time by gender.
    
    plt.figure(figsize=(10, 6))

    sns.boxplot(
        data=df,
        x="Gender",
        y="Survival Time (months)",
        hue="Gender",
        palette="Set2",
        legend=False
    )

    plt.title("Distribution of Survival Time by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Survival Time (months)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    manager = plt.get_current_fig_manager()
    manager.window.wm_geometry("+200+100")

    plt.show()

