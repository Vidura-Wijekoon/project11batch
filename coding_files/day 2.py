# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 17:17:17 2020

@author: user pc vidura97
"""
"""
print("Hello Guys")

print(2+3)#Basic python quick review

"""

import math

math.sqrt(25)

dir(math)

help(math.pow)

math.pow(2,8)

import math as mt
mt.sqrt(36)

#data types

a = 10
type(a)

b=None
type( b)

#taking input

Name = input("Enter the name:")
print(Name)

Age = input("Enter the age")
age = int(Age)#type casting

#strings discussion

name = "Forsk"
len(name)
print(name[-1])

name[0:3]


str1 = " My country is SriLanka"

dir(str)

str2 = str1.upper()

#strings in python are read only
#immutable

str1 = str1.upper()

list1 = ['Kandy','Colombo','Jaffna']

if 'Kandy' in list1:
    print("City found")
else:
    print("City is not found")