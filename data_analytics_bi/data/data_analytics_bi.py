
import pandas as pd
import numpy as np
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Define constants
NUM_ROWS = 10000
PRODUCT_CATEGORIES = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Sports', 'Toys', 'Health']
PAYMENT_METHODS = ['Credit Card', 'PayPal', 'Debit Card', 'Gift Card']
LOYALTY_STATUSES = ['Gold', 'Silver', 'Bronze']

# Generate data
data = {
    'customer_id': [fake.uuid4() for _ in range(NUM_ROWS)],
    'transaction_id': [fake.uuid4() for _ in range(NUM_ROWS)],
    'transaction_date': [fake.date_between(start_date='-2y', end_date='today') for _ in range(NUM_ROWS)],
    'transaction_amount': [round(random.uniform(5.0, 500.0), 2) for _ in range(NUM_ROWS)],
    'product_category': [random.choice(PRODUCT_CATEGORIES) for _ in range(NUM_ROWS)],
    'payment_method': [random.choice(PAYMENT_METHODS) for _ in range(NUM_ROWS)],
    'customer_age': [random.randint(18, 80) for _ in range(NUM_ROWS)],
    'customer_gender': [random.choice(['Male', 'Female']) for _ in range(NUM_ROWS)],
    'customer_region': [fake.city() for _ in range(NUM_ROWS)],
    'loyalty_status': [random.choice(LOYALTY_STATUSES) for _ in range(NUM_ROWS)],
    'churn_risk': [random.randint(1, 10) for _ in range(NUM_ROWS)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('customer_transactions.csv', index=False)

print("Dataset generated and saved as 'customer_transactions.csv'")
