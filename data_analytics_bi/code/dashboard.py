
# dashboard.py

import pandas as pd
import numpy as np
from tabpy.tabpy_tools.client import Client

# Connect to TabPy server (Make sure TabPy is running locally or on your server)
client = Client('http://localhost:9004/')

# Load the generated dataset
df = pd.read_csv('data/customer_transactions.csv')

# Basic data cleaning (e.g., handling missing values, formatting)
df.dropna(inplace=True)  # Remove rows with missing values for simplicity

# Example analysis: Calculate average transaction amount per customer
avg_transaction = df.groupby('customer_id')['transaction_amount'].mean().reset_index()
avg_transaction.rename(columns={'transaction_amount': 'avg_transaction_amount'}, inplace=True)

# Another example: Calculate churn risk group based on churn risk score
df['churn_risk_group'] = pd.cut(df['churn_risk'], bins=[0, 3, 6, 10], labels=['Low', 'Medium', 'High'])

# Publish functions to Tableau via TabPy
# Function to calculate average transaction amount per customer
def calc_avg_transaction_amount(customer_id, transaction_amount):
    df = pd.DataFrame({'customer_id': customer_id, 'transaction_amount': transaction_amount})
    result = df.groupby('customer_id')['transaction_amount'].mean().tolist()
    return result

# Function to assign churn risk groups
def assign_churn_risk_group(churn_risk):
    risk_group = pd.cut(churn_risk, bins=[0, 3, 6, 10], labels=['Low', 'Medium', 'High'])
    return risk_group.tolist()

# Deploy these functions to TabPy so Tableau can call them
client.deploy('CalcAvgTransactionAmount', calc_avg_transaction_amount,
              'Calculates average transaction amount per customer', override=True)

client.deploy('AssignChurnRiskGroup', assign_churn_risk_group,
              'Assigns churn risk group based on churn risk score', override=True)

print("Python functions deployed to TabPy. Ready to use in Tableau.")
