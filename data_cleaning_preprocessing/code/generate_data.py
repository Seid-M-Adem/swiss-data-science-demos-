import pandas as pd
import random
from faker import Faker

# Initialize Faker and random seed
fake = Faker()
random.seed(42)

# Generate synthetic patient data
data = {
    "patient_id": [fake.unique.random_int(min=1000, max=9999) for _ in range(6000)],
    "name": [fake.name() for _ in range(6000)],
    "dob": [fake.date_of_birth(minimum_age=0, maximum_age=90) for _ in range(6000)],
    "gender": [random.choice(['M', 'F', 'Other']) for _ in range(6000)],
    "visit_date": [fake.date_this_decade() for _ in range(6000)],
    "diagnosis": [random.choice(["Diabetes", "Flu", "Cancer", "Hypertension", "COVID-19", None]) for _ in range(6000)],
    "treatment": [random.choice(["Medication", "Surgery", "Therapy", "None", None]) for _ in range(6000)],
    "cost": [random.uniform(100, 10000) if random.random() > 0.05 else None for _ in range(6000)],
    "insurance_status": [random.choice(["Yes", "No", None]) for _ in range(6000)],
    "missing_data_flags": [None for _ in range(6000)]
}

# Create DataFrame and introduce random missing values
df = pd.DataFrame(data)

# Introduce missing values in different columns
for col in ['dob', 'gender', 'diagnosis', 'treatment', 'cost', 'insurance_status']:
    df.loc[df.sample(frac=0.1).index, col] = None

# Save to CSV
df.to_csv('/workspaces/swiss-data-science-demos-/data_cleaning_preprocessing/data/patient_records.csv', index=False)
