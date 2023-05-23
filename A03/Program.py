import pandas as pd
import numpy as np
import sklearn
from sklearn import datasets

iris = datasets.load_iris()

df = pd.DataFrame(iris['data'])

print(df.head())

df.rename(columns = {0:'SepalLengthCm', 1:'SepalWidthCm', 2:'PetalLengthCm', 3:'PetalWidthCm', 4:'Species'},inplace = True)

print(df.head())

print(df.describe())

print(df['SepalLengthCm'].mean())

print(df.median())

print(df.mode())
