import pandas as pd

df = pd.read_csv("employee_data.csv")

# one-hot encoding using get_dummies
encoded_df = pd.get_dummies(df, columns=["department"], drop_first=True)
print(encoded_df.head())
