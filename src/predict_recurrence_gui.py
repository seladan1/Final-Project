import pandas as pd
from gui_graphic_utils import *
from tkinter import messagebox

def predict_recurrence(): # predicting tumor recurrence! (predicting in quotes because there is no usage of ml)
    df_copy = df.copy() #lets not ruin the original df
    for col in features:
        df_copy = df_copy[df_copy[col] == gui_vars[col].get()] #change df[copy] to be the selected var in gui

    if len(df_copy) < 5: #decide not to analyze if data is too small
        messagebox.showinfo("Result",f"Only {len(df_copy)} cases found.\nNot reliable for prediction")
        return None

    probability = df_copy["Recurrence"].mean() * 100 #basic probability calculation
    messagebox.showinfo("Result",f"Predicted recurrence probability: {probability:.1f}%\n"
        f"Based on {len(df_copy)} similar patients") #messagebox pop
    return probability

def update_legend(*args): # updating (dynamic) legend when selecting a new gui string var
    for col in features:
        value = gui_vars[col].get() #select chosen var in gui
        count = len(df[df[col] == value]) #calculate how many patients with this value (len of selected df)
        legend_labels[col].config(text=f"{col} ({value}): {count} cases") #update legend for selected value

    df_copy = df.copy()
    for col in features:
        df_copy = df_copy[df_copy[col] == gui_vars[col].get()] #change df[copy] to be the selected var in gui

    match_label.config(text=f"matching all selections: {len(df_copy)} cases") #update the intersection of all 4 vars

##########################################################################################
if __name__ == "__main__":

    df = pd.read_csv("../BrainTumor.csv")

    # we defined recurrence as - time to recurrence is null 0, time to recurrence isn't null 1
    df["Recurrence"] = df["Time to Recurrence (months)"].notna().astype(int)

    # columns used. why was age not used? age = machine learning, we can't treat age as a drop-down select variable.
    features = ["Tumor Location", "Tumor Grade", "Tumor Type", "Treatment"]

    root = tk.Tk()  # constructor, creates the window
    root.title("brain tumor prediction")

    # create the string vars for the gui using StringVar's constructor.
    gui_vars = {}
    for feature in features:
        gui_vars[feature] = tk.StringVar()

    # create all the options to choose from inside the string vars
    options = {}
    for feature in features:
        options[feature] = df[feature].unique()

    build_input_frame(root, features, gui_vars, options)  # build left side of gui
    legend_frame, legend_labels, match_label = build_legend_frame(root, features)  # build right side of gui

    for feature in features:
        gui_vars[feature].trace_add("write", update_legend)  # trace_add write runs a callable everytime we select stringVar

    (tk.Button(root, text="Predict Recurrence Risk", command=predict_recurrence, width=30)
     .grid(row=1, column=0, columnspan=2, pady=25))  # build gui button

    root.mainloop()  # run gui

