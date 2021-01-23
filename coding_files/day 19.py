import pandas as pd
import numpy as np

df = pd.read_csv("D:/Internships/Forsk_batch11_ViduraWijekoon/Csv_datasets/balanced_reviews.csv")
#EDA Activities

print (df.shape)

(df.columns.tolist())

df['overall'].value_counts()

df.isnull().any(axis = 0)

df.isnull().any(axis = 1)

df[df.isnull().any(axis = 1)].tail()


#handling the missing data
df.dropna(inplace = True)

df['overall'] == 3

df = df[df['overall'] != 3]

df['Positivity'] = np.where(df['overall'] > 3, 1, 0)


#version 01
from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(df['reviewText'], df['Positivity'], random_state = 42)


from sklearn.feature_extraction.text import CountVectorizer


vect = CountVectorizer().fit(features_train)

 

len(vect.get_feature_names())

vect.get_feature_names()[0:10]

features_train_vectorized = vect.transform(features_train)


features_train_vectorized.toarray()

#model 

#classifier model - kNN, LogisticRegression, SVM, NaiveBayes

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(features_train_vectorized, labels_train)

from sklearn.metrics import roc_auc_score

predictions = model.predict(vect.transform(features_test))

roc_auc_score(labels_test, predictions)

#how to improvise

from sklearn.metrics import confusion_matrix
confusion_matrix(labels_test, predictions)

#------------------------------
#version 02
#moving back to data cleaning part
import nltk

nltk.download('stopwords')

from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer

import re

#df['reviewText'][0]

corpus = []

for i in range(0, 527332):
    review = re.sub('[^a-zA-Z]',' ', df.iloc[i,1])
    
    review = review.lower()
    
    review = review.split()
    
    review = [word for word in review if not word in set(stopwords.words('english'))]
    
    
    ps = PorterStemmer()
    
    review = [ps.stem(word) for word in review ]
    
    review = " ".join(review)
    
    corpus.append(review)
    


from sklearn.feature_extraction.text import CountVectorizer



features = CountVectorizer().fit_transform(corpus)[0:10].toarray()

labels = df.iloc[:, 3] 
#teain test spplit
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, random_state = 42)


#model
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(features_train, labels_train)



#score
from sklearn.metrics import roc_auc_score

predictions = model.predict(vect.transform(features_test))

roc_auc_score(labels_test, predictions)



#version 03
#TF_IDF (term frequency-inverse document frequency)


from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(df['reviewText'], df['Positivity'], random_state = 42)

from sklearn.feature_extraction.text import TfidfVectorizer


vect = TfidfVectorizer(min_df = 5).fit(features_train)

features_train_vectorized = vect.transform(features_train)


from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(features_train_vectorized, labels_train)

from sklearn.metrics import roc_auc_score

predictions = model.predict(vect.transform(features_test))

roc_auc_score(labels_test, predictions)














