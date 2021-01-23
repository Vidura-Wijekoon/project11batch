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