import pandas as pd
print("-------------question 1--------------\n")

date = pd.Series(['2025-06-25 14:30:00', '2025-06-26 15:45:00', '2025-06-27 09:15:00'])

s = pd.to_datetime(date)
print(s)

print("\n-------------question 2--------------\n")

df1=pd.DataFrame({"car":["a","c","b"],"price":[74,83,67],"id":[1,2,3]})
df2=pd.DataFrame({"car":["s","t","r"],"price":[77,72,84],"id":[1,2,3]})

print(df2.merge(df1,how="inner",on='price'))
print(df2.merge(df1,how="inner",on='id'))
print(pd.merge(df1,df2,how="inner",on='id'))

result=df2.join(df1,rsuffix="_right",lsuffix="_left")
print(result)


print("\n-------------question 3--------------\n")


df4=pd.DataFrame({"car":["a","c","b"],"price":[97,77,27],"id":[1,2,3]})
df5=pd.DataFrame({"car1":["s","t","r"],"price":[82,73,37],"id":[1,2,3]})
df7=pd.concat([df4,df5],keys=["a1","a2"],axis=1)
df9=pd.concat([df4,df5])

print(df9)
df8=df4.merge(df5,how="inner",on='id')