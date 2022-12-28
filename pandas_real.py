import pandas as pd
#df=pd.read_csv("C:/Users/user669/PycharmProjects/pythonProject/softwareengineers/Developers/pokemon_data.excel")
df=pd.read_excel("C:/Users/user669/PycharmProjects/pythonProject/softwareengineers/Developers/pokemon_data.xlsx")

#print(df.iloc[1:4])##exclude the last index position(represents in colum number)
#print(df.loc[1:4])#include the last index position(represents in colum name)
#print(df.loc[1:5,["Type 1","HP"]])##
#print(df.iloc[1:4])
#print(df.head())
#Aprint(df.loc[0:5,"Name":"Generation"])#use the range operater
#print(df.iloc[0,2])#0- is the row,2-is colum indexposition
#print(df.iloc[[0,1,2]])##the result is 0,1,2- is the rows.
#print(df.iloc[0:5,[1,2]])
##sort ==>ascending order=big to small=True
         #decending=false
#print(df.sort_values("Speed"))#sort the specific colum
#print(df.sort_values("Speed",ascending=False))
#print(df.shape)#shape of ecxel sheet
#print(df.isnull().sum())# it will give the number of a null values in ecxel sheet
#print(df.isnull().sum().sum())#total number of a null values in a sheet
df2=df.fillna(value=12)
print(df2)
df2_read_excel("C:/pokemon_data.xlsx")
#print(df.head(300))


#df3=df.fillna(value=100)
#print(df3)
#print(df.isnull().sum())
#data=['Attack','Defense','Speed']
#df['total']=df[data].sum(axis=1).iloc([1,800,3])

#df2 =df.iloc[lambda x: x.index % 2 != 0]& df.iloc[:,4:8]
#print(df2)







