import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def outcome_distribution(df):

    counts = pd.crosstab(df["Treatment"], df["Treatment Outcome"])
    probabilities = counts.div(counts.sum(axis=1), axis=0)
    return probabilities


def plot_histograms(df):

    treatments = df["Treatment"].unique()
    outcomes = df["Treatment Outcome"].unique()

    for treatment in treatments:
        subset = df[df["Treatment"] == treatment]

        counts = subset["Treatment Outcome"].value_counts()
        counts = counts.reindex(outcomes, fill_value=0)

        plt.figure(figsize=(10, 6))
        counts.plot(kind="bar")
        plt.title(f"Outcome for Treatment: {treatment}, total {counts.sum()}")
        plt.xlabel("Treatment Outcome")
        plt.ylabel("Count")
        plt.gca().yaxis.set_major_locator(MaxNLocator(integer =True))
        plt.tight_layout()

        # Fix the window position to avoid visual jumping on screen.
        manager = plt.get_current_fig_manager()
        manager.window.wm_geometry("+200+100")
    
        plt.show()


def summarize_probabilities(probabilities):

    prob_percent = (probabilities * 100).round(1)
    print("Outcome probabilities per treatment (in %):")
    print(prob_percent.to_string())

    best_treatment = prob_percent.idxmax(axis=0).iloc[0]
    best_prob = prob_percent.max().iloc[0]

    print(f"\nConclusion: The most successful treatment is '{best_treatment}' with "
          f"{best_prob}% chance of the best outcome")