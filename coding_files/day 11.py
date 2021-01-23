#Numpy and matplotlib

list1 = [1,2,3,4,5,6,7,8,9,10]

list2 = list1*10

list3 = []

for item in list1:
    list3.append(item*10)
    
[item*10 for item in list1]

#list1 has 1L data items




list1 = [1,2,3,4,5,6,7,8,9,10]

import numpy as np

x = np.array(list1)



a = [1,2,3,4,5,6,7,8,9]

x = np.array(a)

x = x.reshape(3,3)

x = np.arange(10)

x = np.arange(10, dtype = np.uint8)




x = np.zeros((2,3))

x = np.ones((2,3))


x = np.array([1,2,3], dtype = np.float)

x[0] = 10

x[0] = np.nan



import matplotlib.pyplot as plt

x = [1,2,3,4,5]

y = [1,8,27,64,125]

plt.scatter(x,y)

plt.plot(x,y, color ='green')


branches = ['CSE','ECE','IT','EE']

studentscount = [15, 30, 25, 10]

colors = ['gold','yellowgreen','red','blue']

exp = (0.1, 0,0,0)
plt.pie(studentscount, explode = exp, colors = colors,labels = branches)


#https://medium.com/analytics-vidhya/axes-and-dimensions-in-numpy-and-pandas-array-a2490f72631c














