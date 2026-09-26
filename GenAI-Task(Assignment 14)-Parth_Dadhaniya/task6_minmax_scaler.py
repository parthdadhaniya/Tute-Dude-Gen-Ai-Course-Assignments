import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df = pd.read_csv("employee_data.csv")
cols = ["age", "experience", "projects_completed"]

minmax = MinMaxScaler().fit_transform(df[cols])
standard = StandardScaler().fit_transform(df[cols])

print("MinMax scaled (0 to 1):\n", minmax[:3].round(2))
print("\nStandard scaled:\n", standard[:3].round(2))
