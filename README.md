# Brain Tumor Stage-Based Recurrence Data Analysis

## **Project Documentation**

### **Project Description**
This project provides a comprehensive clinical analysis of brain tumor patient data, focusing on survival rates, recurrence patterns, and treatment efficacy. 

* **Main Objectives:**
    * **Recurrence Prediction:** Predict the chances of tumor recurrence and the specific recurrence site based on the tumor's initial location.
    * **Age & Survival Correlation:** Analyze if a correlation exists between survival time and the age of the patient at the time of diagnosis.
    * **Gender Analysis:** Investigate potential connections between survival time and the patient's gender.
    * **Treatment Efficacy:** Predict treatment outcomes based on the specific treatment protocol used.
    * **Tumor Grading:** Determine if the tumor type can predict the tumor grade at the initial diagnosis.
* **Assumptions:** Missing.
* **Hypothesis:** Missing.

---

### **Folder/Module Structure**
The project is organized into a main execution script and a specialized source directory for modularity:

* **`main.py`**: The primary entry point that coordinates the data cleaning, analysis, and visualization workflow.
* **`src/`**: A module containing specialized scripts for different research questions:
    * `clean_data.py`: Functions for loading and cleaning the raw dataset.
    * `predict_recurrence_gui.py`: A GUI-based tool for recurrence analysis.
    * `question_2.py`: Statistical analysis of age vs. survival.
    * `question_3.py`: Spearman correlation and survival plots by gender.
    * `question_4.py`: Distribution analysis of treatment outcomes.
    * `question_5.py`: Statistical testing for tumor type and grade.

---

### **Key Stages**
1.  **Data Import:** Raw clinical data is loaded from the `BrainTumor.csv` file.
2.  **Data Processing:** The dataset is cleaned to handle missing values (NAs) and ensure proper data types for analysis.
3.  **Modeling & Statistical Analysis:**
    * Calculating Spearman correlations for survival time.
    * Conducting statistical tests and calculating Cramer's V for categorical variables.
    * Generating outcome distributions and probability summaries.
4.  **Visualization:** Creating insightful charts including histograms, scatter plots, and distribution plots using `matplotlib` and `seaborn`.

---

### **Important Definitions**
* **`FILE_PATH`**: The system is configured to look for `BrainTumor.csv` in the root directory.
* **Matplotlib Backend:** The project utilizes the `TkAgg` backend for graphical rendering.
* **Treatment Outcomes:** Includes outcomes such as "Complete response," "Partial response," "Stable disease," and "Progressive disease".

---

## **Data Description**
The analysis is based on a clinical dataset including the following key parameters:

| Column Name | Description |
| :--- | :--- |
| **Patient ID** | Unique identifier for each patient record. |
| **Age** | Age of the patient at diagnosis. |
| **Gender** | Patient's gender (Male/Female). |
| **Tumor Type** | Pathological classification (e.g., Glioblastoma, Meningioma, Astrocytoma). |
| **Tumor Grade** | Grade from I to IV. |
| **Tumor Location** | Initial site of the tumor (e.g., Frontal lobe, Temporal lobe). |
| **Treatment** | Protocols used such as Surgery, Radiation, and Chemotherapy. |
| **Treatment Outcome** | Clinical result of the chosen treatment. |
| **Survival Time** | Total survival measured in months. |

**Link to the Dataset:** [BrainTumor dataset](https://www.kaggle.com/datasets/thegoanpanda/brain-tumor-stage-based-recurrence-patterns/data)

---

## **References**
* **Papers/Articles:** Using only the Dataset.

---

## **Instructions for Running the Project**

### **1. Install Dependencies**
Ensure you have Python installed, then run the following command to install required libraries from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 2. Prepare the Data
Ensure the `BrainTumor.csv` file is located in the root directory alongside `main.py`.

### 3. Run the Analysis
Execute the main script to process the data and generate the statistical visualizations:

```bash
python main.py
```
