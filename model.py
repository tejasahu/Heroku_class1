# -*- coding: utf-8 -*-
"""23

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tHtBok3Rs3ncT9enRgUyvOtSehryLryT
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

df=pd.read_csv('/content/hire.csv')

df

df.isnull().sum()

df['test_score(out of 10)'].fillna(df['test_score(out of 10)'].mean(),inplace=True)
df

df['experience'].fillna(0,inplace=True)
df

x=df.iloc[:,:3]
y=df.iloc[:,-1]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.1,random_state=5)

from sklearn.linear_model import LinearRegression
mymodel=LinearRegression()
mymodel.fit(x_train,y_train)

y_pred=mymodel.predict(x_test)
y_pred[0]

"""# now predict"""

y=mymodel.predict([[5,6,7]])

y

"""download this file

"""

import pickle
pickle.dump(mymodel,open("model.pkl","wb"))