import pandas as pd
import random

# Generate a sample dataset
num_rows = 7000
data = {
    'customer_id': [i for i in range(1, num_rows + 1)],
    'age': [random.randint(18, 70) for _ in range(num_rows)],
    'gender': [random.choice(['Male', 'Female']) for _ in range(num_rows)],
    'purchase_history': [random.choice(['Fashion', 'Electronics', 'Grocery', 'Travel']) for _ in range(num_rows)],
    'average_spend': [random.randint(100, 1000) for _ in range(num_rows)],
    'loyalty_score': [random.randint(0, 100) for _ in range(num_rows)],
    'preferred_channel': [random.choice(['Online', 'Store']) for _ in range(num_rows)],
    'engagement_score': [random.randint(0, 100) for _ in range(num_rows)],
    'canton': [random.choice(['Zürich', 'Geneva', 'Bern', 'Basel', 'Lausanne', 'Lugano']) for _ in range(num_rows)]
}

df = pd.DataFrame(data)
df.to_csv('/workspaces/swiss-data-science-demos-/customer_segmentation/data/customer_data.csv', index=False)
