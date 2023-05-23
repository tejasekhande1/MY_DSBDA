import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Boston.csv');

print(df.describe(),"\n")
print(df.info)

#split the dataset

x = df[['rm','lstat']]
y = df['medv']

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20,random_state=0)

from sklearn.linear_model import LinearRegression
model = LinearRegression().fit(x_train,y_train)
y_pred = model.predict(x_test)

from sklearn.metrics import mean_absolute_error
print("MAE : ",mean_absolute_error(y_test,y_pred))
print("Model Score : ",model.score(x_test,y_test))

features = np.array([[9,12]])
prediction = model.predict(features)
print("Prediction : ",format(prediction))
