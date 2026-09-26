import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance.csv")

# pair plot
sns.pairplot(df)
plt.show()

# correlation heatmap
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()
