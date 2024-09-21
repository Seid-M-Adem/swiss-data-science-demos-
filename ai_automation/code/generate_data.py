# File: ai_automation/code/generate_data.py

import pandas as pd
import numpy as np
from faker import Faker
import random
import os

# Initialize Faker to generate fake data (Switzerland locale)
fake = Faker('de_CH')

# Number of rows for the dataset
num_rows = 4000

# Define lists for options
incident_types = ['Accident', 'Theft', 'Fire', 'Natural Disaster', 'Vandalism']
document_statuses = ['Complete', 'Incomplete', 'Pending']
approval_statuses = ['Approved', 'Rejected', 'Under Review']

# Generate random data
def generate_data(num_rows):
    data = {
        'claim_id': [i for i in range(1, num_rows + 1)],
        'customer_id': [fake.unique.random_int(min=1000, max=9999) for _ in range(num_rows)],
        'claim_date': [fake.date_between(start_date='-2y', end_date='today') for _ in range(num_rows)],
        'claim_amount': [round(random.uniform(500, 20000), 2) for _ in range(num_rows)],  # Amounts between 500 and 20,000 CHF
        'incident_type': [random.choice(incident_types) for _ in range(num_rows)],
        'document_status': [random.choice(document_statuses) for _ in range(num_rows)],
        'approval_status': [random.choice(approval_statuses) for _ in range(num_rows)],
        'processing_time': [random.randint(1, 90) for _ in range(num_rows)]  # Processing time between 1 and 90 days
    }
    
    return pd.DataFrame(data)

# Main function to generate and save the dataset
def main():
    output_dir = '../data'
    os.makedirs(output_dir, exist_ok=True)  # Ensure the data directory exists
    
    claims_data = generate_data(num_rows)
    
    # Save to a CSV file
    claims_data.to_csv(f'/workspaces/swiss-data-science-demos-/ai_automation/data/claims_data.csv', index=False)
    print("Data generated and saved to data/claims_data.csv")

# Entry point for the script
if __name__ == "__main__":
    main()
