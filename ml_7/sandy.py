import pandas as pd
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = "patient_data.csv"  # Replace with your .csv file path
data = pd.read_csv(file_path)

# Preview the data
print("Data Preview:")
print(data.head())

# Preprocessing
# Assuming all columns are numeric. Select only features for clustering.
# Replace with your specific columns if needed.
features = data.select_dtypes(include=['float64', 'int64']).columns
X = data[features]

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Fit Gaussian Mixture Model (GMM)
n_clusters = 3  # Adjust based on your requirement
gmm = GaussianMixture(n_components=n_clusters, random_state=42)
gmm.fit(X_scaled)

# Predict the clusters
labels = gmm.predict(X_scaled)
data['Cluster'] = labels

# Save clustered data to a new CSV file
data.to_csv("patient_data_with_clusters.csv", index=False)
print("Clustered data saved to 'patient_data_with_clusters.csv'.")

# Visualize the clusters (assuming 2D or PCA-reduced data)
if X_scaled.shape[1] > 2:
    from sklearn.decomposition import PCA
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
else:
    X_pca = X_scaled

sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=labels, palette="viridis", style=labels)
plt.title("Cluster Visualization")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend(title="Cluster")
plt.show()
