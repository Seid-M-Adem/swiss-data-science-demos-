# generate_data.py
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Constants
NUM_ROWS = 5000
START_DATE = datetime(2022, 1, 1)
END_DATE = datetime(2023, 12, 31)
DATE_RANGE = (END_DATE - START_DATE).days

# Generate dates
date_range = [START_DATE + timedelta(days=i) for i in range(DATE_RANGE + 1)]
dates = [random.choice(date_range) for _ in range(NUM_ROWS)]

# Generate store IDs
store_ids = [f'ST{random.randint(1, 20)}' for _ in range(NUM_ROWS)]

# Generate product IDs
product_ids = [f'P{random.randint(1, 100)}' for _ in range(NUM_ROWS)]

# Generate units sold
units_sold = np.random.poisson(lam=30, size=NUM_ROWS)

# Generate revenue
revenue = units_sold * np.random.uniform(15, 120, size=NUM_ROWS)

# Generate discount rates
discount_rate = np.random.uniform(0, 0.4, size=NUM_ROWS)

# Generate holiday flags (1 for holiday, 0 for non-holiday)
holiday_flag = [random.choice([0, 1]) for _ in range(NUM_ROWS)]

# Generate weather conditions
weather_conditions = ['Sunny', 'Rainy', 'Snowy', 'Cloudy']
weather_condition = [random.choice(weather_conditions) for _ in range(NUM_ROWS)]

# Generate advertisement spend
advertisement_spend = np.random.uniform(200, 6000, size=NUM_ROWS)

# Generate season
seasons = ['Winter', 'Spring', 'Summer', 'Fall']
season = [seasons[(date.month % 12) // 3] for date in dates]

# Create DataFrame
df = pd.DataFrame({
    'date': dates,
    'store_id': store_ids,
    'product_id': product_ids,
    'units_sold': units_sold,
    'revenue': revenue,
    'discount_rate': discount_rate,
    'holiday_flag': holiday_flag,
    'weather_condition': weather_condition,
    'advertisement_spend': advertisement_spend,
    'season': season
})

# Save to CSV
df.to_csv('/workspaces/swiss-data-science-demos-/predictive_analytics_forecasting/data/sales_data.csv', index=False) 