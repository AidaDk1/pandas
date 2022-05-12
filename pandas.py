import pandas as pd
import numpy as np



#Creating Series
m=[21,22,23]
series1=pd.Series(m)
print(series1)#int64


data = np.array(['a','b','c','d'])
series= pd.Series(data)
print(series)#object

s2=pd.Series(data,index=[10,11,12,13])#index tuzuu or label
print(s2)

# nums=[20,21,22]
# l=pd.Series(data,index=['a','b','c'])
# print(l)

#indexti aluu
s3= pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s3[0])
print(s3[:3])
print(s3['a'])

#Series arkyluu dictionary tuzuu
dict1={'studentId':190101,'age':18,'score':95}
sd=pd.Series(dict1)
print(sd)

#DataFrame










