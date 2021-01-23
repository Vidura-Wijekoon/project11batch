# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 17:31:24 2020

@author: user pc vidura97
"""

import numpy as np
import pandas as pd

df = pd.read_csv('D:/Internships/Forsk_batch11_ViduraWijekoon/Csv_datasets/caesarian.csv')

df.isnull().any(axis=0)

df.dtypes
labels = df.iloc[:,5].values

features = df.iloc[:,0:5].values
features
from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2)



"""
Standard Scaling
"""

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

features_train= sc.fit_transform(features_train)

features_test= sc.transform(features_test)

#classification

#KNN

from sklearn.neighbors import KNeighborsClassifier

classifier =  KNeighborsClassifier(n_neighbors = 5,p = 2)

classifier.fit(features_train,labels_train)

pred = classifier.predict(features_test)

pd.DataFrame(zip(pred, labels_test)).values


from sklearn.metrics import confusion_matrix


confusion_matrix(labels_test, pred)

