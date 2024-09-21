# File: ai_automation/code/automation_script.py

import pandas as pd

# Load the dataset
data_path = '../data/claims_data.csv'

# Load the dataset into a pandas DataFrame
def load_data():
    df = pd.read_csv(data_path)
    return df

# Function to simulate processing claims
def process_claims(df):
    # Filter approved claims
    approved_claims = df[df['approval_status'] == 'Approved']
    
    # Summarize the approved claims
    total_amount = approved_claims['claim_amount'].sum()
    avg_processing_time = approved_claims['processing_time'].mean()
    
    print(f"Total approved claim amount: CHF {total_amount:.2f}")
    print(f"Average processing time for approved claims: {avg_processing_time:.2f} days")

def main():
    df = load_data()
    process_claims(df)

if __name__ == "__main__":
    main()

