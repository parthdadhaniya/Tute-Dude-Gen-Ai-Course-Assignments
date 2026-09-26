import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance.csv")

# histogram
sns.histplot(df["math_score"])
plt.show()

# kde plot
sns.kdeplot(df["math_score"])
plt.show()

# rug plot
sns.rugplot(df["math_score"])
plt.show()

# histogram + kde combined
sns.histplot(df["math_score"], kde=True)
plt.show()
