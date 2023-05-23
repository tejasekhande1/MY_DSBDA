import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('iris.csv');

ch = 1;

while(ch != 10):
    print('1.Describe Dataset');
    print('2.Imformation of Dataset');
    print('3.Min() and Max()');
    print('4.Mean');
    print('5.Mode');
    print('6.Median');
    print('8.Find NaN')
    print('7.Groupwise Summary');
    print('10.Exit');

    ch = int(input("Enter Your Choice : "))

    if ch == 1 :
        print(df.describe());

    if ch == 2:
        print(df.info);

    if ch == 3:
        print(df['sepal.width'].min())
        print(df['sepal.length'].min())
        print(df.min())
        print(df.max());

    if ch == 4:
        print(df.mean());

    if ch == 5:
        print(df.median());

    if ch == 6:
        print(df.std());

    if ch == 7:
        m1 = df['sepal.length'].min()
        print(m1)

    if ch == 8:
        print(df.notnull())
