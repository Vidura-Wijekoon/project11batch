
"""
Created on Thurs Dec  3 17:15:15 2020

@author: user pc vidura97
"""

while (True):
    str1 = input("Enter the name: ")
    
    if (not str1):
        break #terminate the loop exe
    
    if len(str1) < 5:
        print ("short length")
    elif len(str1) >= 5 and len(str1) < 10:
        print ("medium length")
    else:
        print ("long length")
        
#version #2
        
while (True):
    str1 = input("Enter the name: ")
    
    if (not str1):
        print ("Not a valid entry, try again")
        continue
    
    if len(str1) < 5:
        print ("short length")
    elif len(str1) >= 5 and len(str1) < 10:
        print ("medium length")
    else:
        print ("long length")
        


list1 = [1,2,3,4,5]


len(list1)

list1[0]

list1[-1]

dir(list)

help(list.append)

list1.append(10)

list1.insert(1,11)

list1.remove(10)

list1 = [1,2,10,2,3,4,3,5,3]

list1.count(3)

list1.remove(3)
list1.remove(3)
list1.remove(3)

list1 = [1,2,10,2,3,4,3,5,3]

while 3 in list1:
    list1.remove(3)
    

list1 = [1,2,10,2,3,4,3,5,3]

del list1[0]

#list is mutable (you can modify)
#string is immutable (read only)

t = (1,2,3,4,5)
#tuples are read only

t[0] = 100


cteam = ('India','Virat')

#unpacking 
tname, cname = cteam


#using dictionary as a database/storage


cteam = {
'country':'India',
'capt':"Virat",
'wk': "KL Rahul",
'vice-capt':'KL'
 
 }

cteam['wk']

cteam['vice-capt'] = 'KL Rahul'


cteam = {
'country':'India',
'capt':"Virat",
'wk': [('ODI',"KL Rahul"),('Test','Pant')],
'vice-capt':'KL'
 
 }


cteam = {
'country':'India',
'capt':"Virat",
'wk': {'ODI':"KL Rahul",'Test':'Pant'},
'vice-capt':'KL'
 
 }


cteam.keys()
cteam.values()

for item in cteam.keys():
    print (item)



list1 = ['Jaipur','Kota','Bharatpur']

for name in list1:
    print (name)

for item in list1:
    print (item)


str1 = "Forsk"

for item in str1:
    print (item)

str1[0]

t = ("Forsk",'Coding')
t[0]

for item in t:
    for letter in item:
        print (letter)


list1 = [1, 'Iqbal', 2.3, True, None]

        
        
        

