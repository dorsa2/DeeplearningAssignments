import numpy as np
from sklearn.cluster import KMeans

# Step 1: Generate 30 random numbers between 0 and 100 (like student scores)
np.random.seed(42)  # for reproducibility
data = np.random.randint(0, 101, size=(30, 1))  # 30 numbers, each in its own array (required by sklearn)

# Step 2: Apply KMeans clustering with 2 clusters
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(data)

# Step 3: Get the cluster labels and cluster centers
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# Print the results
print("Generated Data:")
print(data.flatten())
print("\nCluster Centers:")
print(centers.flatten())
print("\nCluster Labels for each data point:")
print(labels)
