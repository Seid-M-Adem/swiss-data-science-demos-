import pandas as pd

# Load the dataset
df = pd.read_csv('/workspaces/swiss-data-science-demos-/data_cleaning_preprocessing/data/patient_records.csv')

# Step 1: Handle Missing Values
def handle_missing_values(df):
    # Fill missing 'gender' with 'Unknown'
    df['gender'].fillna('Unknown', inplace=True)
    
    # Drop rows where 'dob', 'diagnosis', or 'treatment' is missing
    df.dropna(subset=['dob', 'diagnosis', 'treatment'], inplace=True)
    
    # Fill missing 'cost' with the mean cost
    df['cost'].fillna(df['cost'].mean(), inplace=True)
    
    # Replace missing 'insurance_status' with 'Unknown'
    df['insurance_status'].fillna('Unknown', inplace=True)
    
    return df

# Step 2: Correct Data Types
def correct_data_types(df):
    df['dob'] = pd.to_datetime(df['dob'])
    df['visit_date'] = pd.to_datetime(df['visit_date'])
    df['cost'] = df['cost'].astype(float)
    return df

# Step 3: Add Flags for Missing Data
def add_missing_data_flags(df):
    df['missing_data_flags'] = df.isnull().any(axis=1).astype(int)
    return df

# Apply cleaning steps
df = handle_missing_values(df)
df = correct_data_types(df)
df = add_missing_data_flags(df)

# Save cleaned data
df.to_csv('/workspaces/swiss-data-science-demos-/data_cleaning_preprocessing/data/patient_records_cleaned.csv', index=False)

print("Data cleaning completed and saved to '/workspaces/swiss-data-science-demos-/data_cleaning_preprocessing/data/patient_records_cleaned.csv'.")

