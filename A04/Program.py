import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def RemoveOutlier(df,var):
    Q1 = df[var].quantile(0.25)
    Q3 = df[var].quantile(0.75)
    IQR = Q3-Q1
    high,low = Q3+1.5*IQR , Q1-1.5*IQR
    df = df[((df[var] <= high) & (df[var] >= low))]
    return df

def DisplayOutlier(df,message):
    fig,axes = plt.subplots(1,2)
    sns.boxplot(data = df , x = 'rm' , ax = axes[0])
    sns.boxplot(data = df , x = 'lstat' , ax = axes[1])
    fig.tight_layout()
    plt.show()

df = pd.read_csv('Boston.csv');

ch = 1;

while(ch != 10):
    print('1.Describe Dataset');
    print('2.Statistical Imformation of Dataset');
    print('3.Find Missing Values');
    print('4.Find Correlation Matrix');
    print('5.Remove Outliers');
    print('6.Linear Regression');

    ch = int(input("Enter Your Choice : \n"))

    if ch == 1:
        print(df.describe());

    if ch == 2:
        print(df.info);

    if ch == 3:
        print(df.isna().sum());

    if ch == 4:
        print('Finding Correlation Matrix using heatmap');
        sns.heatmap(df.corr(),annot = True)
        plt.show()

    if ch == 5:
        print('Remove Outliers from Datasets')
        DisplayOutlier(df,'Before Removing Outlier');
        df = RemoveOutlier(df,'rm')
        df = RemoveOutlier(df,'lstat')
        DisplayOutlier(df,'After Removing Outlier');

    if ch == 6:
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
        print('MAE:',mean_absolute_error(y_test,y_pred))
        print('Model Score : ',model.score(x_test,y_test))

        print('Predict House Price By giving user Input : ')
        features = np.array([[6,19]])
        prediction = model.predict(features)
        print('Prediction : {}'.format(prediction))
