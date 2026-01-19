import tkinter as tk

def build_legend_frame(root, features):
    # right side legend text
    legend_frame = tk.LabelFrame(root, text="Data Availability", padx=10, pady=10)
    legend_frame.grid(row=0, column=1, padx=15, pady=15, sticky="ne")

    # features list
    legend_labels = {}

    #empty label, add on update later
    for i, col in enumerate(features):
        lbl = tk.Label(legend_frame, text="")
        lbl.grid(row=i, column=0, sticky="w", pady=4)
        legend_labels[col] = lbl

    #display message
    match_label = tk.Label(legend_frame, text="", font=("Arial", 10, "bold"))
    match_label.grid(row=len(features), column=0, pady=10, sticky="w")

    return legend_frame, legend_labels, match_label

#build for selecting
def build_input_frame(root, features, gui_vars, options):
    input_frame = tk.LabelFrame(root, text="Patient Selection", padx=10, pady=10)
    input_frame.grid(row=0, column=0, padx=15, pady=15, sticky="nw")

    for i, col in enumerate(features):
        tk.Label(input_frame, text=col).grid(
            row=i, column=0, padx=10, pady=10, sticky="w"
        )
        #drop down
        menu = tk.OptionMenu(input_frame, gui_vars[col], *options[col])
        menu.grid(row=i, column=1, padx=10, pady=10)

        gui_vars[col].set(options[col][0])

    return input_frame
