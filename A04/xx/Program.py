import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ds1 = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv")
print(ds1.head())

print(ds1.info())

sns.boxplot(x = ds1['rm'])
plt.show()

# Scatterplot
sns.scatterplot(x = ds1['rm'], y=ds1['medv']) 
plt.show()

print(ds1.corr())
sns.heatmap(ds1.corr(), annot = True)
plt.show()


