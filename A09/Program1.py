import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('titanic.csv');

print(df.describe());

sns.boxplot(df['Sex'],df['Age'],df['Survived']).set_title("Boxplot");
plt.show()
