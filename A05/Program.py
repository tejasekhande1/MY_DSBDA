import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Social_Network_Ads.csv');
print('Social Network Ads Dataset is successfully loaded')

print('Imformation of Dataset : \n',df.info)
print('Column Names : \n',df.columns);
print('First Five Rows : \n',df.head().T);
print('Last Five Rows : \n',df.tail().T);

# split the input and output data
x = df[['Age','EstimatedSalary']]
y = df['Purchased']

#training and testing data
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 20, random_state=0)

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
x_train = sc_X.fit_transform(x_train)
x_test = sc_X.fit_transform(x_test)


# apply logistic regression model on trainig data
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)


from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))


#display confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print('Confusion_matrix \n',cm)

fig,ax = plt.subplots(figsize = (5,5))
sns.heatmap(cm,annot=True,linewidths = 3, cmap="Blues")
plt.show()
