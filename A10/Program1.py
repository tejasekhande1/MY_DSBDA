import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv');

def RemoveOutlier(df,var):
    Q1 = df[var].quantile(0.25)
    Q3 = df[var].quantile(0.75)

    IQR = Q3-Q1;
    high,low = Q3+1.5*IQR, Q1-1.5*IQR;

    df = df[((df[var] >= low) & (df[var] <= high))]
    return df;

def DisplayOutlier(df,msg):
    fig,axes = plt.subplots(2,2)
    fig.suptitle(msg)
    sns.boxplot(data = df, x ='sepal.length' , ax = axes[0,0])
    sns.boxplot(data = df, x ='sepal.width' , ax = axes[0,1])
    sns.boxplot(data = df, x ='petal.length' , ax = axes[1,0])
    sns.boxplot(data = df, x ='petal.width' , ax = axes[1,1])
    plt.show()

ch = 1;
while(ch != 10):
    print('1.Describe Dataset')
    print('2.Draw Histogram')
    print('3.Draw Box Plot')
    print('4.Identify Outliers')
    print('10.Exit')

    ch = int(input("Enter Your Choice : \n"))

    if ch == 1:
        print(df.describe());
    
    if ch == 2:
        sns.histplot(df['sepal.length'])
        plt.xlabel('SepalLength')
        plt.ylabel('Frequency')
        plt.show()

        sns.histplot(df['sepal.width'])
        plt.xlabel('SepalWidth')
        plt.ylabel('Frequency')
        plt.show()

        sns.histplot(df['petal.length'])
        plt.xlabel('PetalLength')
        plt.ylabel('Frequency')
        plt.show()

        sns.histplot(df['petal.width'])
        plt.xlabel('PetalWidth')
        plt.ylabel('Frequency')
        plt.show()

    if ch == 3:
        sns.boxplot(df['petal.length'])
        plt.show()

        sns.boxplot(df['petal.width'])
        plt.show()

        sns.boxplot(df['sepal.length'])
        plt.show()

        sns.boxplot(df['sepal.width'])
        plt.show()

    if ch == 4:
        DisplayOutlier(df,'Outlier Before Removing');
        df = RemoveOutlier(df,'petal.length');
        df = RemoveOutlier(df,'petal.width');
        df = RemoveOutlier(df,'sepal.length');
        df = RemoveOutlier(df,'sepal.width');
        DisplayOutlier(df,'Outlier After Removing');

    if ch == 10:
        break
