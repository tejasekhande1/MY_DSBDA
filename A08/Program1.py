import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv');

print("Describe Dataset : \n",df.describe());

sns.displot(df['Fare']);
plt.show()

sns.histplot(df['Fare']);
plt.show()

fig,axes = plt.subplots(2,2)
sns.histplot(data = df , x = 'Age' , hue = 'Survived' , multiple = 'dodge' , ax = axes[0,0])
sns.histplot(data = df , x = 'Fare' , hue = 'Survived' , multiple = 'dodge' , ax = axes[0,1])
sns.histplot(data = df , x = 'Age' , hue = 'Sex' , multiple = 'dodge' , ax = axes[1,0])
sns.histplot(data = df , x = 'Fare' , hue = 'Sex' , multiple = 'dodge' , ax = axes[1,1])
plt.show()
