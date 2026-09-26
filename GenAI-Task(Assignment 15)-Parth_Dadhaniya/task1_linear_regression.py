import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("employee_data.csv")

X = df[["age", "experience", "projects_completed"]]
y = df["salary"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lr = LinearRegression()
lr.fit(X_train, y_train)

preds = lr.predict(X_test)
print("Actual:     ", y_test.values[:3])
print("Predictions:", preds[:3].round(2))

# actual vs predicted plot
plt.scatter(y_test, preds)
plt.title("Actual vs Predicted")
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.show()
