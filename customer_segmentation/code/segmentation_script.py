import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('../data/customer_data.csv')

# Select features for clustering
X = data[['age', 'average_spend', 'loyalty_score', 'engagement_score']]

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-means clustering
kmeans = KMeans(n_clusters=4, random_state=42)
data['cluster'] = kmeans.fit_predict(X_scaled)

# Save the clustered data
data.to_csv('../data/segmented_customers.csv', index=False)

# Visualize clusters (age vs average spend)
plt.figure(figsize=(8, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=data['cluster'], cmap='viridis')
plt.title('Customer Segments (Age vs Average Spend)')
plt.xlabel('Age (scaled)')
plt.ylabel('Average Spend (scaled)')
plt.colorbar(label='Cluster')
plt.show()
