# Brain Tumor Clinical Data Analysis Project

## **Project Documentation**

### **Project Description**
This project focuses on the statistical analysis and visualization of clinical data for patients diagnosed with brain tumors. The analysis explores correlations between patient demographics, tumor characteristics, and treatment efficacy to better understand survival and recurrence patterns.

* **Main Objectives:**
    * **Recurrence Prediction:** Analyze the probability of tumor recurrence and predict the recurrence site based on the initial tumor location.
    * **Age and Survival Correlation:** Investigate whether there is a significant correlation between patient age and total survival time.
    * **Gender and Survival Analysis:** Determine if survival time is influenced by the patient's gender using Spearman correlation.
    * **Treatment Outcome Prediction:** Assess the distribution of outcomes based on the specific treatment protocol used.
    * **Tumor Grading Analysis:** Evaluate if the tumor type can act as a predictor for the tumor grade at the time of initial diagnosis.
* **Assumptions:** **Missing**.
* **Hypothesis:** **Missing**.

---

### **Folder and Module Structure**
The project is divided into a main execution script and a source folder containing specialized modules:

* **`main.py`**: The central entry point that manages data loading, cleaning, and the sequential execution of research questions.
* **`src/`**: Contains the core analytical logic:
    * `clean_data.py`: Functions for loading raw CSV data and performing data cleaning.
    * `predict_recurrence_gui.py`: Provides a GUI for recurrence analysis (Question 1).
    * `question_2.py` - `question_5.py`: Modular scripts handling specific statistical tests and plotting for each research objective.

---

### **Key Stages**
1.  **Data Import:** Ingesting raw patient data from the `BrainTumor.csv` file.
2.  **Data Processing:** Cleaning the dataset, handling missing values (NA), and formatting data types for analysis.
3.  **Modeling & Analysis:**
    * Calculating Spearman correlation coefficients for survival analysis.
    * Conducting statistical tests and calculating Cramer's V for categorical associations.
4.  **Visualization:** Generating distribution plots, histograms, and scatter plots using `matplotlib` and `seaborn` to visualize clinical findings.

---

### **Important Definitions & Configurations**
* **`FILE_PATH`**: The dataset filename is defined as `BrainTumor.csv`.
* **Backend**: The project explicitly uses the `TkAgg` backend for `matplotlib` to ensure proper GUI rendering.
* **Dataset Integrity**: The script includes a check to abort analysis if the dataset fails to load or clean correctly.

---

## **Data Description**
The analysis is performed on a clinical dataset. The dataset includes the following key columns:

| Column Name | Description |
| :--- | :--- |
| **Patient ID** | Unique identifier for the patient. |
| **Age** | Age at diagnosis. |
| **Gender** | Patient gender (Male/Female). |
| **Tumor Type** | Pathological type (e.g., Glioblastoma, Meningioma, Astrocytoma). |
| **Tumor Grade** | Grade from I to IV. |
| **Tumor Location** | Initial site of the tumor. |
| **Treatment** | Protocols including Surgery, Radiation, and Chemotherapy. |
| **Treatment Outcome** | Results such as "Complete response" or "Progressive disease". |
| **Survival Time** | Total survival measured in months. |

**Link to the Dataset:** **Missing**.

---

## **References**
* **Papers or Articles Used:** **Missing**.

---

## **Instructions for Running the Project**

### **1. Install Prerequisites**
Ensure you have Python installed. You can install all necessary libraries using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt

```bash
python main.py
