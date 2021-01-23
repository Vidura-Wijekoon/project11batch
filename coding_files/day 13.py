import numpy as np
import pandas as pd

dataset = pd.read_csv('D:/Internships/Forsk_batch11_ViduraWijekoon/Csv_datasets/Salary_Classification.csv')

dataset.dtypes

dataset['Department'].unique()

dataset.isnull().any(axis = 0)


features = dataset.iloc[:,0:4].values
labels = dataset.iloc[:,-1].values

#label encoding
#one hot encoding is technique to perform label encoding

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

columnTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder = 'passthrough' )


features = np.array(columnTransformer.fit_transform(features), dtype = np.float32)

features = features[:,1:]

from sklearn.model_selection import train_test_split


features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2)



from sklearn.linear_model import LinearRegression


regressor  = LinearRegression()

regressor.fit(features_train, labels_train)

pred = regressor.predict(features_test)


pd.DataFrame(zip(pred, labels_test))


xx = ['Web Dev', 1100, 0, 1]

xx = np.array(xx)

xx = xx.reshape(1,4)

xx = np.array(columnTransformer.transform(xx), dtype = np.float32)


xx = xx[:,1:]

regressor.predict(xx)










