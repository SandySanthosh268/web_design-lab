import pandas as pd
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Load patient data from a CSV file
file_path = "patient_data.csv"  # Change to your file path
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("Data Preview:")
print(data.head())

# Preprocessing: Handle missing values and scale data
data = data.dropna()  # Remove rows with missing values
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Apply Gaussian Mixture Model (EM algorithm)
n_clusters = 3  # Change the number of clusters as needed
gmm = GaussianMixture(n_components=n_clusters, random_state=42)
gmm.fit(scaled_data)

# Predict cluster labels
cluster_labels = gmm.predict(scaled_data)
data['Cluster'] = cluster_labels

# Save the clustered data to a new CSV file
output_file = "clustered_patient_data.csv"
data.to_csv(output_file, index=False)
print(f"Clustered data saved to {output_file}")

# Visualize clusters (using first two features)
plt.figure(figsize=(8, 6))
sns.scatterplot(x=scaled_data[:, 0], y=scaled_data[:, 1], hue=cluster_labels, palette='viridis')
plt.title("Patient Data Clustering")
plt.xlabel("Feature 1 (scaled)")
plt.ylabel("Feature 2 (scaled)")
plt.legend(title="Cluster")
plt.show()