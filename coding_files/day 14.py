# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 17:12:03 2020

@author: user pc vidura97
"""

import numpy as np
import pandas as pd


dataset = pd.read_csv('D:/Internships/Forsk_batch11_ViduraWijekoon/Csv_datasets/Salary_Classification.csv')

dataset.isnull().any(axis = 0)



features = dataset.iloc[:,0:4].values
labels = dataset.iloc[:,-1].values

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


columnTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder = 'passthrough' )

features = np.array(columnTransformer.fit_transform(features), dtype = np.float32)

features = features[:,1:]

from sklearn.model_selection import train_test_split


features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2)



#Normalization/feature scaling

"""
Standarad and Min max scaling
"""

"""
Standard Scaling
"""

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

features_train= sc.fit_transform(features_train)

features_test= sc.transform(features_test)

from sklearn.linear_model import LinearRegression


regressor  = LinearRegression()


regressor.fit(features_train, labels_train)


xx = ['Development', 1100, 0, 1]

xx = np.array(xx)

xx = xx.reshape(1,4)


xx = np.array(columnTransformer.transform(xx), dtype = np.float32)


xx = xx[:,1:]

xx = sc.transform(xx)

regressor.predict(xx)


##################################


'''
missing data handling
'''

data = pd.read_csv('D:/Internships/Forsk_batch11_ViduraWijekoon/Csv_datasets/cricket_salary_data.csv')

data.isnull().any(axis=0)

features = data.iloc[:,0:3].values

labels = data.iloc[:,-1].values

#imputation

from sklearn.impute import SimpleImputer

#define the imputer
#from numpy import nan can also be used instead np.nan


imputer =  SimpleImputer(missing_values = np.nan, strategy = 'mean')

features[:,1:2] = imputer.fit_transform(features[:,1:2])