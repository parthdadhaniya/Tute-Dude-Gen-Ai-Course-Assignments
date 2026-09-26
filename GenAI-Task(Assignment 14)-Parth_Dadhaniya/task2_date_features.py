import pandas as pd

df = pd.read_csv("employee_data.csv")

# extract year, month, and day from date
df["joining_date"] = pd.to_datetime(df["joining_date"])

df["year"] = df["joining_date"].dt.year
df["month"] = df["joining_date"].dt.month
df["day"] = df["joining_date"].dt.day

print(df[["joining_date", "year", "month", "day"]].head())
