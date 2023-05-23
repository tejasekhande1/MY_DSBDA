import pandas as pd
import numpy as np

df = pd.read_csv('placement_data.csv');
print("Placement dataset is successfully loaded into the data frame");

choice = 1
while(choice != 10):
    print('-----------Menu---------')
    print('1.Display Imformation');
    print('2.Display Statistical Imformation of Dataset');
    print('3.Finding Missing Values in Dataset');
    print('4.Change DataType of columns');
    print('5.Conversion of Categorial to quantitative');
    print('7.Display Load Dataset');
    print('10.Exit');

    choice = int(input('Enter Your Choice : '))

    if choice == 1:
        print('Imformation of Dataset :\n',df.info);
        print('Shape of Dataset (row x col): ',df.shape);
        print('Columns Name : ',df.columns);
        print('Total Elements in dataset : ',df.size);
        print('Datatype of attributes : ',df.dtypes)
        print('First 5 rows : \n',df.head().T)
        print('Last 5 rows : \n',df.tail().T);

    if choice == 2:
        print('Statistical Imformation of Numerical Columns : \n',df.describe());

    if choice == 3:
        print('Total Number of Null Values in Dataset : ',df.isna().sum());

    if choice == 4:
        print('Check Datatype of sl_no : ',df['sl_no'].dtypes)
        df['sl_no'] = df['sl_no'].astype('int8')
        print('Check Datatype of sl_no : ',df['sl_no'].dtypes)
        df['ssc_p'] = df['ssc_p'].astype('int8')
        print('Check Datatype of ssc_p : ',df['ssc_p'].dtypes)

    if choice == 5:
        df['gender'].replace(['M','F'],[0,1] ,inplace = True)
        print('\nFind Male and replace with 0 as well as female 1');

    if choice == 6:
        print('Normalization Using Min-Max Feature Scaling : ')
        df['salary'] = (df['salary']-df['salary'].min())/(df['salary'].max()-df['salary'].min())
        print(df.head().T)

    if choice == 7:
        df = pd.read_csv('placement_data.csv');
        print(df.head().T)

    if choice == 10:
        break;
