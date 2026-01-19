import matplotlib
matplotlib.use('TkAgg')

from src.clean_data import load_data, clean_data
from src.predict_recurrence_gui import run_gui
from src.question_2 import calc_correlation, plot_result
from src.question_3 import calc_spearman_gender_survival, plot_survival_by_gender, analyze_long_survivors
from src.question_4 import outcome_distribution, summarize_probabilities, plot_histograms
from src.question_5 import get_tumor_stats, run_statistical_test, calculate_cramers_v, distribution_plot

# Define the input file path
FILE_PATH = "BrainTumor.csv"

def main():
    # Data Cleaning
    df_raw = load_data(FILE_PATH)
    dataset = clean_data(df_raw)
    
    if dataset is not None:
        # Question 1: Can we predict the chances of a tumor recurrence and the recurrence site based on its initial location?
        print("\n\n--- Can we predict the chances of a tumor recurrence and the recurrence site based on its initial location? ---\n")
        run_gui(dataset)
        
        # Question 2: Is there a correlation between the survival time and the age of the patient (at the time of diagnosis)?
        print("\n\n--- Is there a correlation between the survival time and the age of the patient (at the time of diagnosis)? ---\n")
        grouped_data = calc_correlation(dataset)
        plot_result(grouped_data)
        
        # Question 3: Is there a connection between the survival time and the patient's gender?
        print("\n\n--- Is there a connection between the survival time and the patient's gender? ---\n")
        calc_spearman_gender_survival(dataset)
        plot_survival_by_gender(dataset)
        analyze_long_survivors(dataset)
        
        # Question 4: Can we predict the treatment outcome based on the chosen treatment?
        print("\n\n--- Can we predict the treatment outcome based on the chosen treatment? ---\n")
        probabilities = outcome_distribution(dataset)
        summarize_probabilities(probabilities)
        plot_histograms(dataset)
        
        # Question 5: Can tumor type predict the tumor grade at initial diagnosis?
        contingency, percentages = get_tumor_stats(dataset)
    
        print("\n\n--- Can tumor type predict the tumor grade at initial diagnosis? ---\n")
        run_statistical_test(contingency)
        calculate_cramers_v(contingency)
        distribution_plot(dataset)
        
    else:
        print("Analysis aborted: Could not load the dataset.")

 
if __name__ == "__main__":
    main()
