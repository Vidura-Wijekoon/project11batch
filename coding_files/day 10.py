#simple linear regression, the first machine learning model


import pandas as pd

#read the dataset

dataset = pd.read_csv("D:/Internships/Forsk_batch11_ViduraWijekoon/Csv_datasets/student_scores.csv")

dataset.isnull().any(axis = 0)

dataset.shape

dataset.ndim

dataset.head()


features = dataset['Hours'].values

labels = dataset['Scores'].values

x = [1,2,3,4,5]
y = [1,2,3,4,5]

import matplotlib.pyplot as plt

plt.scatter(x,y)

plt.scatter(features, labels)


from sklearn.linear_model import LinearRegression

regressor  = LinearRegression() #model

import numpy as np

features = features.reshape(25,1)

regressor.fit(features, labels)

#y = mx + c

x = 9 
m = regressor.coef_

c = regressor.intercept_

score = m*x + c



regressor.predict([[9]])





