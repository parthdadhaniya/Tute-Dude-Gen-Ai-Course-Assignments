import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance.csv")

# bivariate histogram
sns.histplot(data=df, x="math_score", y="reading_score")
plt.show()

# bivariate kde plot
sns.kdeplot(data=df, x="math_score", y="reading_score")
plt.show()
