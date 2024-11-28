import pandas as pd

# Step 1: Create a sample employee dataset
data = {
    "EmployeeID": [101, 102, 103, 104],
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "Department": ["HR", "Finance", "IT", "Marketing"],
    "Salary": [50000, 60000, 70000, 80000],
    "YearsAtCompany": [2, 5, 7, 10],
    "PromotionLastYear": [0, 1, 0, 1]
}

# Step 2: Load the data into a pandas DataFrame
df = pd.DataFrame(data)

# Step 3: Display the dataset
print("Original Employee Data:")
print(df)

# Step 4: Preprocessing (Convert categorical data to numerical if needed)
df["Department"] = df["Department"].astype("category").cat.codes

# Step 5: Feature and target separation
features = df[["Age", "Department", "Salary", "YearsAtCompany"]]
target = df["PromotionLastYear"]

print("\nFeatures (Inputs to the ML Model):")
print(features)

print("\nTarget (Output for the ML Model):")
print(target)

# Step 6: (Optional) Save the processed data to a file
df.to_csv("processed_employee_data.csv", index=False)

print("\nProcessed data has been saved to 'processed_employee_data.csv'.")
