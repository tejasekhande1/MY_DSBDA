import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Boston.csv');

#split the data into inputs and outputs
x = df[['rm','lstat']] #input
y = df['medv']  #output

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20,random_state=0)

#apply linear regression model on training data
from sklearn.linear_model import LinearRegression
model = LinearRegression().fit(x_train,y_train)
y_pred = model.predict(x_test)

#Display accuracy of the model
from sklearn.metrics import mean_absolute_error
print('Mean Absolute Error : ',mean_absolute_error(y_test,y_pred))
print('Model Score : ',model.score(x_test,y_test))

print('Predict House Price : ')
features = np.array([[9,16]])
prediction = model.predict(features)
print('Prediction : {}'.format(prediction))
