
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def RemoveOutlier(df,var):
    Q1 = df[var].quantile(0.25)
    Q3 = df[var].quantile(0.75)
    IQR = Q3-Q1
    high,low = Q3+1.5*IQR, Q1-1.5*IQR

    df = df[((df[var] >= low) & (df[var] <= high))]
    print('Outliers Removed in ',var)
    return df

def DisplayOutliers(df,message):
    fig,axes = plt.subplots(2,2)
    fig.suptitle(message)
    sns.boxplot(data = df , x = 'raisedhands' , ax = axes[0,0])
    sns.boxplot(data = df , x = 'VisITedResources' , ax = axes[0,1])
    sns.boxplot(data = df , x = 'AnnouncementsView' , ax = axes[1,0])
    sns.boxplot(data = df , x = 'Discussion' , ax = axes[1,1])
    plt.show()

df = pd.read_csv('student_data.csv');
print('Student Acadamic Performance Dataset is loaded');

choice = 1

while(choice != 10):
    print('1.Describe Dataset');
    print('2.Information of Dataset');
    print('3.Show NULL Values in Dataset');
    print('4.Display Outliers');
    print('5.Conversion from Categorical to Quantitative');
    print('6.Relationship between variables');
    print('10.Exit');

    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        print(df.describe());

    if choice == 2:
        print(df.info);
    
    if choice == 3:
        # display null values
        print('NULL values are \n',df.isna().sum())
    
    if choice == 4:
        #display outliers
        DisplayOutliers(df,'Before Removing Outliers \n')
        df = RemoveOutlier(df,'raisedhands')
        df = RemoveOutlier(df,'VisITedResources')
        df = RemoveOutlier(df,'AnnouncementsView')
        df = RemoveOutlier(df,'Discussion')
        DisplayOutliers(df,'After Removing Outliers \n')
    
    if choice == 5:
        #conversion of Categorical to Quantitative
        df['gender'].replace(['M','F'],[0,1] ,inplace = True)
        print('\nFind Male and replace with 0 as well as female 1');

    if choice == 6:
        print('Relationship Between Variables using Scatterplot : ')
        sns.scatterplot(data = df , x ='raisedhands', y = 'VisITedResources')
        plt.title("Scatterplot for Raisedhands and VisitedResources");
        plt.show()

    if choice == 10:
        break;
