import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load Excel file
data = pd.read_excel("PCOS_data_without_infertility.xlsx", sheet_name="Full_new", header=0)

# Clean column names
data.columns = data.columns.map(lambda x: str(x).strip().replace('\xa0', ' '))

# Show columns found for verification
print("✅ Columns found in dataset:")
print(data.columns.tolist())

# Replace '.' with NaN to handle invalid entries
data.replace('.', np.nan, inplace=True)

# Convert all columns to numeric where possible (non-convertible become NaN)
data = data.apply(pd.to_numeric, errors='coerce')

# Drop ID columns like 'Sl. No' and 'Patient File No.'
columns_to_drop = [col for col in data.columns if 'Sl. No' in col or 'Patient' in col or 'Unnamed' in col]
data.drop(columns=columns_to_drop, inplace=True)

# Drop rows with any missing values
data.dropna(inplace=True)

# Confirm target column exists
if "PCOS (Y/N)" not in data.columns:
    raise ValueError("❌ 'PCOS (Y/N)' column not found in dataset!")

# Split into features and target
X = data.drop(columns=["PCOS (Y/N)"])
y = data["PCOS (Y/N)"]

# Train-test split (80-20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, "pcos_model.pkl")

print("✅ Model trained and saved as pcos_model.pkl")
