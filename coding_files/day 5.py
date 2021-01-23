# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 17:12:50 2020

@author: user pc vidura97
"""

a = 10

list1 = [1,2,3,4,5]

#regular exp

import re

s = 'aaa@xxx.com bbb@yyy.com ccc@zzz.com'

re.sub('[a-z]*@','ABC@',s)

str1 = 'abc123xyz456_0'

re.findall('\d$',str1)

str1 ='foo123bar'

re.search('\d{3}',str1)

str1 = '456foo123bar'
result = re.search('\d{3}',str1)

print(result)

if re.search('d{3}',str1):
    print("Found a match")
else:
    print("No match")
    
str2 = 'Forsk forsk coding school'

re.match('forsk',str2)
re.search('forsk',str2)

re.match('Forsk',str2)
re.search('Forsk',str2)



str1 = 'Forsklabs@gmail.com yugendra@forsk.in yogendrasingh@qualcomm.com ysingh@mango.com 123 syl 653 yogendrajp@gmail.com'
pattern = re.compile(r'\w+@\w+\.\w+')
pattern.findall(str1)

import pandas as pd

df = pd.read_csv("Salaries.csv")