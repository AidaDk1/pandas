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

#ex1
dataAr={'users':['Aida',"Aidai",'Aidana'],
         "id" :[123,456,789]
}
dframe=pd.DataFrame(dataAr,index=[1,2,3])
print(dframe)


print(pd.__version__) #version of library

#ex2
calories = {"day1": 420, "day2": 380, "day3": 390}
objects = pd.Series(calories)
print(objects) #creating keyvalue objects 

#ex3
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
dframes= pd.DataFrame(data)
print(dframes)  #creating dataframes.It is a two dimensional arrays,data structure
df = pd.DataFrame(data)

df1= pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df1) #adding index to a dataframe

#DataFrmae from Lists
data1 = [1,2,3,4,5]
dataf = pd.DataFrame(data1)
print(dataf)


data2 = [['Alex',10],['Bob',12],['Clarke',13]]
df2 = pd.DataFrame(data2,columns=['Name','Age'])
print(df2)

#Create a DataFrame from Dict of ndarrays / Lists
data3= {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df3 = pd.DataFrame(data3)
del(df3['Name'])#deleting element
print(df3)

#Create a DataFrame from List of Dicts
data4 = [{'a': 1, 'b': 2,'c':4},{'a': 5, 'b': 10, 'c': 20}]
df4 = pd.DataFrame(data4, index=['first', 'second'])
print(df4)

data5=[{'name':'Aida','surname':'Dosmuratk','id':123},{'name':'Aida','surname':'Dosmuratk','id':123}]
df5=pd.DataFrame(data5,index=['first','second'])
print(df5['name'])











