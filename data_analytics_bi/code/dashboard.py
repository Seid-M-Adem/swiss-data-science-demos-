import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from tabpy.tabpy_tools.client import Client

# Connect to TabPy server
client = Client('http://localhost:9004/')

# Load the dataset
df = pd.read_csv('data/customer_transactions.csv')

# Basic data cleaning
df.dropna(inplace=True)

# Example analysis: Average transaction amount per customer
avg_transaction = df.groupby('customer_id')['transaction_amount'].mean().reset_index()
avg_transaction.rename(columns={'transaction_amount': 'avg_transaction_amount'}, inplace=True)

# Example: Churn risk group distribution
df['churn_risk_group'] = pd.cut(df['churn_risk'], bins=[0, 3, 6, 10], labels=['Low', 'Medium', 'High'])

# Create visualizations
# 1. Static Visualization: Average Transaction Amount
plt.figure(figsize=(10, 6))
sns.histplot(avg_transaction['avg_transaction_amount'], bins=30, kde=True)
plt.title('Distribution of Average Transaction Amount per Customer')
plt.xlabel('Average Transaction Amount')
plt.ylabel('Frequency')
plt.savefig('data_analytics_bi/visualizations/dashboard_overview.png')
plt.close()

# 2. Interactive Visualization: Churn Risk Distribution
fig = px.pie(df, names='churn_risk_group', title='Churn Risk Group Distribution')
fig.write_html('data_analytics_bi/visualizations/dashboard_interactive.html')

# Deploy functions to TabPy
def calc_avg_transaction_amount(customer_id, transaction_amount):
    df = pd.DataFrame({'customer_id': customer_id, 'transaction_amount': transaction_amount})
    result = df.groupby('customer_id')['transaction_amount'].mean().tolist()
    return result

def assign_churn_risk_group(churn_risk):
    risk_group = pd.cut(churn_risk, bins=[0, 3, 6, 10], labels=['Low', 'Medium', 'High'])
    return risk_group.tolist()

client.deploy('CalcAvgTransactionAmount', calc_avg_transaction_amount,
              'Calculates average transaction amount per customer', override=True)

client.deploy('AssignChurnRiskGroup', assign_churn_risk_group,
              'Assigns churn risk group based on churn risk score', override=True)

print("Python functions deployed to TabPy. Visualizations saved and ready for GitHub.")

