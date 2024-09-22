# Data Cleaning and Preprocessing Services

## Project Overview

This project demonstrates the cleaning and preprocessing of healthcare data, modeled similarly to real-world examples such as Switzerland's healthcare data. The dataset (`patient_records.csv`) contains 6,000 rows of patient data, including various inconsistencies and missing values. The aim of this project is to apply data cleaning techniques using Python and Pandas.

## Folder Structure

- **data/**: Contains the raw dataset (`patient_records.csv`), a messy healthcare dataset that requires cleaning.
- **code/**: Contains the `data_cleaning.py` script for programmatically cleaning the data.
- **notebooks/**: Jupyter Notebook (`preprocessing_notebook.ipynb`) providing an interactive explanation of each cleaning step.

## Dataset Description

- **patient_id**: Unique ID for each patient.
- **name**: Full name of the patient.
- **dob**: Date of birth of the patient.
- **gender**: Gender of the patient (M/F/Other).
- **visit_date**: Date of hospital visit.
- **diagnosis**: Diagnosis during the visit.
- **treatment**: Treatment administered during the visit.
- **cost**: Cost of treatment.
- **insurance_status**: Whether the patient has insurance coverage (Yes/No).
- **missing_data_flags**: Flags indicating if any data is missing in the patient's record.

## How to Run

1. **Using Python script**:
   - Install required dependencies: `pip install -r requirements.txt`
   - Run the script: `python code/data_cleaning.py`

2. **Using the Jupyter Notebook**:
   - Open `notebooks/preprocessing_notebook.ipynb` to interactively explore the data cleaning process.

## Technologies Used

- Python (Pandas, NumPy)
- Jupyter Notebook

