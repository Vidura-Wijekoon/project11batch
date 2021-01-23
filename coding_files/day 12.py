
import pandas as pd

#read the dataset

dataset = pd.read_csv("D:/Internships/Forsk_batch11_ViduraWijekoon/Csv_datasets/student_scores.csv")

features = dataset['Hours'].values

labels = dataset['Scores'].values

from sklearn.linear_model import LinearRegression


regressor  = LinearRegression() #model

features = features.reshape(25,1)

regressor.fit(features, labels)

x = 9 #int

import numpy as np

x = [9] #list

x = np.array(x)

x = x.reshape(1,1)

regressor.predict(x)





regressor.predict(9)



#drawing the best line for this dataset

import matplotlib.pyplot as plt

plt.scatter(features, labels)

plt.plot(features, regressor.predict(features))



#train test split

dataset = pd.read_csv("D:/Internships/Forsk_batch11_ViduraWijekoon/Csv_datasets/student_scores.csv")

features = dataset['Hours'].values

labels = dataset['Scores'].values


from sklearn.model_selection import train_test_split


features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2)

from sklearn.linear_model import LinearRegression


regressor  = LinearRegression()

features_train = features_train.reshape(20,1)

regressor.fit(features_train, labels_train)

features_test = features_test.reshape(5,1)

pred = regressor.predict(features_test)


pd.DataFrame(zip(pred, labels_test))


#train score
regressor.score(features_train, labels_train)

#test score
regressor.score(features_test, labels_test)











list1 = [1,2,3]

list2 = [11,12,13]


list(zip(list1,list2))



