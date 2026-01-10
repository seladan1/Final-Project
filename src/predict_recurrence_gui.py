from src.gui_graphic_utils import *
from tkinter import messagebox

# Defining global variables.
df = None
# Columns used. why was age not used? age = machine learning, we can't treat age as a drop-down select variable.
features = ["Tumor Location", "Tumor Grade", "Tumor Type", "Treatment"]
gui_vars = {}
legend_labels = {}
match_label = None
legend_frame = None

def predict_recurrence(): # Predicting tumor recurrence! (predicting in quotes because there is no usage of ml)
    global df, gui_vars, features
    df_copy = df.copy() # Lets not ruin the original df
    for col in features:
        df_copy = df_copy[df_copy[col] == gui_vars[col].get()] # Change df[copy] to be the selected var in gui

    if len(df_copy) < 5: # Decide not to analyze if data is too small
        messagebox.showinfo("Result",f"Only {len(df_copy)} cases found.\nNot reliable for prediction")
        return None

    probability = df_copy["Recurrence"].mean() * 100 # Basic probability calculation
    messagebox.showinfo("Result",f"Predicted recurrence probability: {probability:.1f}%\n"
        f"Based on {len(df_copy)} similar patients") # Messagebox pop
    
    return probability

def update_legend(*args): # Updating (dynamic) legend when selecting a new gui string var
    global df, gui_vars, features, legend_labels, match_label
    for col in features:
        value = gui_vars[col].get() # Select chosen var in gui
        count = len(df[df[col] == value]) # Calculate how many patients with this value (len of selected df)
        legend_labels[col].config(text=f"{col} ({value}): {count} cases") # Update legend for selected value

    df_copy = df.copy()
    for col in features:
        df_copy = df_copy[df_copy[col] == gui_vars[col].get()] # Change df[copy] to be the selected var in gui

    match_label.config(text=f"matching all selections: {len(df_copy)} cases") # Update the intersection of all 4 vars


def run_gui(external_df):
    global df, gui_vars, legend_labels, match_label, features, legend_frame
    df = external_df.copy()
    # We defined recurrence as - time to recurrence is null 0, time to recurrence isn't null 1
    df["Recurrence"] = df["Time to Recurrence (months)"].notna().astype(int)

    root = tk.Tk()  # Constructor, creates the window
    root.title("brain tumor prediction")

    # Create the string vars for the gui using StringVar's constructor.
    for feature in features:
        gui_vars[feature] = tk.StringVar()

    # Create all the options to choose from inside the string vars
    options = {}
    for feature in features:
        options[feature] = df[feature].unique()

    build_input_frame(root, features, gui_vars, options)  # Build left side of gui
    legend_frame, legend_labels, match_label = build_legend_frame(root, features)  # Build right side of gui

    for feature in features:
        gui_vars[feature].trace_add("write", update_legend)  # Trace_add write runs a callable everytime we select stringVar

    (tk.Button(root, text="Predict Recurrence Risk", command=predict_recurrence, width=30)
     .grid(row=1, column=0, columnspan=2, pady=25))  # Build gui button

    root.mainloop()  # Run gui