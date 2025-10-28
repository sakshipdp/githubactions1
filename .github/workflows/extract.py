import pandas as pd 

print("extract data from mysql database")

data ={
   "id" : [ 1, 2, 3],
   "name" : ["A","B","C"],
   "age" : [10,20,30]
}

df=pd.DataFrame(data)
print(df)
