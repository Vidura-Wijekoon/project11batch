# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 17:21:20 2020

@author: user pc vidura97
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 17:15:42 2020

@author: user pc vidura97
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 17:23:29 2020

@author: user pc vidura97
"""

import pandas as pd
import numpy as np

df = pd.read_csv("D:/Internships/Forsk_batch11_ViduraWijekoon/Csv_datasets/balanced_reviews.csv")

print(df.shape)

(df.columns.tolist())

df["overall"].value_counts()

df.isnull().any(axis=0)

df.isnull().any(axis=1)

df[df.isnull().any(axis=1)].head()

#handling the missing data

df.dropna(inplace=True)

df['overall'] == 3

df = df[df['overall'] != 3]

np.where(df['overall'] > 3 , 1, 0)

df['Positivity'] = np.where(df['overall'] > 3 , 1, 0)

features = df['reviewText']

labels = df['Positivity']

from sklearn.model_selection import train_test_split

features_train,features_test,labels_test,labels_train = train_test_split(df['reviewText'], df['Positivity'], random_state = 0)


from sklearn.feature_extraction.text import CountVectorizer

vect = CountVectorizer().fit(features_train)

len(vect.get_feature_names())

vect.get_feature_names()[0:10]

features_train_vectorized = vect.transform(features_train)

features_train_vectorized.toarray()


#model

#classifier model - KNN, LogisticRegression, SVM
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(features_train_vectorized,labels_test)

from sklearn.metrics import roc_auc_score

predictions = model.predict(vect.transform(features_test))
#how to imporovise

roc_auc_score(labels_test, predictions)

from sklearn.metrics import confusion_matrix

confusion_matrix(labels_test, predictions)


#--------------------


#data cleaning part

import nltk

nltk.download('stopwords')

from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer

import re

df['reviewText'][0]

review = re.sub('[^a-zA-Z]',' ', df['reviewText'][0])

review = review.lower()

review = review.split()

review = [word for word in review if not word in set(stopwords.words('english'))]

ps = PorterStemmer()

review = [ps.stem(word) for word in review]

review = " ".join(review)