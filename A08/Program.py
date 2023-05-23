import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('https://raw.githubusercontent.com/dphi-official/Datasets/master/titanic_data.csv')

print(data.describe())

sns.countplot(data['Survived'])
plt.show()

sns.countplot(data['Pclass'])

sns.countplot(data['Embarked'])

#sns.countplot(data['Age'])
#plt.show()

sns.countplot(data['Fare'])
plt.show()
