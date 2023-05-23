
#importing required library

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#loading dataset

data = pd.read_csv('https://raw.githubusercontent.com/dphi-official/Datasets/master/titanic_data.csv')

print(data.describe());

sns.boxplot(data['Sex'], data["Age"], data["Survived"], palette = "Set2").set_title('Plot for distribution of age with respect to each gender along with the information about whether they survived or not')
plt.show()
