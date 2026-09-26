import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("employee_data.csv")
cols = ["age", "experience", "projects_completed"]

scaler = StandardScaler()
scaled = scaler.fit_transform(df[cols])

scaled_df = pd.DataFrame(scaled, columns=cols)
print("StandardScaler Output:\n", scaled_df.head())
print("\nMean (~0):\n", scaled_df.mean().round(2))
print("\nStd (~1):\n", scaled_df.std().round(2))
