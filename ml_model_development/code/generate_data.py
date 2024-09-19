
### 5. Dataset: `data/swiss_clinical_trials.csv`

###We'll generate a synthetic dataset using the following Python code. You can run this locally or in your GitHub Codespace to generate the CSV file.

###```python
import pandas as pd
import numpy as np

# Seed for reproducibility
np.random.seed(42)

# Number of rows
num_rows = 2500

# Generate synthetic data
data = {
    'trial_id': np.arange(1, num_rows + 1),
    'patient_id': np.random.randint(10000, 99999, size=num_rows),
    'age': np.random.randint(18, 85, size=num_rows),  # Patients aged between 18 and 85
    'gender': np.random.choice(['Male', 'Female'], size=num_rows),
    'drug_dosage': np.random.uniform(10, 300, size=num_rows),  # Dosage in mg
    'side_effects': np.random.choice([0, 1], size=num_rows),  # 0: No side effects, 1: Side effects
    'success_indicator': np.random.choice([0, 1], size=num_rows),  # 0: Unsuccessful, 1: Successful trial
    'genetic_marker': np.random.choice([0, 1], size=num_rows),  # 0: Marker not present, 1: Marker present
    'baseline_health': np.random.uniform(0, 1, size=num_rows)  # Health score between 0 and 1
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('/workspaces/swiss-data-science-demos-/ml_model_development/data/drug_trial_data.csv', index=False)
