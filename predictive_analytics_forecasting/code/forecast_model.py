
# forecast_model.py
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('/workspaces/swiss-data-science-demos-/predictive_analytics_forecasting/data/sales_data.csv', parse_dates=['date'])

# Feature Engineering
data['month'] = data['date'].dt.month
data['day_of_week'] = data['date'].dt.dayofweek

# Encode categorical features
label_encoders = {}
for column in ['store_id', 'product_id', 'weather_condition', 'season']:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

# Define features and target
features = ['store_id', 'product_id', 'units_sold', 'discount_rate', 'holiday_flag', 'weather_condition', 'advertisement_spend', 'month', 'day_of_week', 'season']
X = data[features]
y = data['revenue']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error: {mae}')

# Plot feature importances
importances = model.feature_importances_
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(12, 8))
plt.title('Feature Importances')
plt.bar(range(X.shape[1]), importances[indices], align='center')
plt.xticks(range(X.shape[1]), np.array(features)[indices], rotation=90)
plt.xlim([-1, X.shape[1]])
plt.show()
