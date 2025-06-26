import pandas as pd

# data={'A':[1,2,3],'B':[4,5,6]}
# df = pd.DataFrame(data,index=['a','b','c'])
# print(df)
# print("Addition =\n" ,df+2)
# print("Subtraction =\n" ,df-2)
# print("Multiplication =\n" ,df*2)
# print("Division =\n" ,df/2)
# print("Floor Division =\n" ,df//2)
# print("Modulus =\n" ,df%2)
# print("Exponential =\n" ,df**2)
#
# df['C']=df['A']+df['B']
# print("C = \n",df)


# df2= pd.DataFrame({'A':[1,2,3,7],'B':[4,5,6,8]})
# df3= pd.DataFrame({'A':[41,25,73],'B':[62,26,37]},index=[1,2,3])
# # df3= pd.DataFrame({'A':[41,25,73],'B':[62,26,37]},index=[0,1,3])
# print(df2)
# print(df3)
# print("\n Addition of 2 dataframes = \n",df2+df3)
# print("\n Subtraction of 2 dataframes = \n",df2-df3)
# print("\n Multiplication of 2 dataframes = \n",df2*df3)
# print("\n Division of 2 dataframes = \n",df2/df3)
# print("\n Floor Division of 2 dataframes = \n",df2//df3)
# print("\n Modulus of 2 dataframes = \n",df2%df3)
# print("\n Exponential of 2 dataframes = \n",df2**df3)


""""----------------CONCATENATION---------------------"""

# one = pd.DataFrame({
#     'Name':['K1','K2','K3','K4','K5'],
#     'Subject':['sub1','sub2','sub3','sub4','sub5'],
#     'Marks':[26,73,83,84,22]},
#     index=[1,2,3,4,5]
# )
#
# two = pd.DataFrame({
#     'Name':['J1','J2','J3','J4','J5'],
#     'Subject':['SUB1','SUB2','SUB3','SUB4','SUB5'],
#     'Marks':[62,73,72,78,97]},
#     index=[1,2,3,4,5]
# )
#
# result = pd.concat([one,two])
# print(result)
#
# print("----------------------------")
#
# result = pd.concat([one,two],keys=["s1","s2"])
# print(result)
#
# print("------------------------------")
#
# result = pd.concat([one,two],keys=["s1","s2"],ignore_index=True)    #ignoring given indexing and keys and
# # only give index from default index 0  , ignore index normally false hi hota h
# print(result)
#
# print("----------------------------")
#
# result = pd.concat([one,two],keys=["s1","s2"],axis=1)   # axis eak line me print karne ke kam aata h , normally 0 hota h
# print(result)


# """"----------------MERGE---------------------"""
# right = pd.DataFrame({
#     'id':[1,2,3,4,5],
#     'Name':['K1','K2','K3','K4','K5'],
#     'Subject':['sub1','sub2','sub3','sub4','sub5'],
#     'Marks':[26,73,83,78,22]},
#     index=[1,2,3,4,5]
# )
#
# left = pd.DataFrame({
#     'id': [1, 2, 3, 4, 5],
#     'Name':['J1','J2','J3','J4','J5'],
#     'Subject':['SUB1','SUB2','SUB3','SUB4','SUB5'],
#     'Marks':[62,73,72,78,97]},
#     index=[1,2,3,4,5]
# )
#
# result = left.merge(right, on = 'id')
# print(result)
#
# print("-----------------------")
#
# result = left.merge(right, on = 'Marks')
# print(result)
#
# print("-----------------------")
#
# result = right.merge(left, on = 'Marks')
# print(result)
#
# print("-----------------------")
#
# result = left.merge(right, on = ['id','Marks'])
# print(result)
#
# print("-----------------------")
#
# result = right.merge(left, on = ['id','Marks'])
# print(result)
#
# print("-----------------------")
#
# result = right.merge(left, on = 'Marks',how='left')
# print(result)
#
# print("-----------------------")
#
# result = left.merge(right, on = 'Marks',how='right')
# print(result)
#
# print("-----------------------")
#
# result = left.merge(right, on = 'id')
# print(result)
#
# print("----------RIGHT JOIN----------")
#
# result = right.merge(left, on = 'Marks',how='right')
# print(result)
#
# print("----------LEFT JOIN----------")
#
# result = left.merge(right, on = 'Marks',how='left')
# print(result)
#
# print("-----------OUTER----------")
#
# result = left.merge(right, on = 'Marks',how='outer')
# print(result)
#
# print("-----------INNER----------")
#
# result = left.merge(right, on = 'Marks',how='inner')
# print(result)
#
# print("-----------CROSS----------")
#
# result = left.merge(right,how='cross')
# print(result)
#
# print("------------CROSS 2nd method----------")
#
# result = pd.merge(left,right,how='cross')
# print(result)
#
# print("------------JOIN-----------")
#
# result = left.join(right,rsuffix="_right", lsuffix="_left")
# print(result)

# result = left.join(right,rprefix="_right", lprefix="_left")   # chal nhi rha prefix ke liye
# print(result)

print("--------PIVOT--------")    #it is use to convert rows into columns or shorten/summary the big table

# df = pd.DataFrame({"Col1":range(12),"Col2":["A","A","A","B","B","B","C","C","C","D","D","D"],
#                    "Date":pd.to_datetime(["2025-06-20","2025-06-21","2025-06-22"] *4 )})

# df = pd.DataFrame({"Col1":range(12),"Col2":["A","A","A","B","B","B","C","C","C","D","D","D"],
#                    "Date":pd.to_datetime(["2025-06-20","2025-07-20","2025-08-20"] *4 )})
#
# print(df)
#
# print("----------")
#
# result = df.pivot(index="Date" , columns = "Col2" , values = "Col1")
# print(result)
#
# print("----------")
#
# result = df.pivot(index="Date" , columns = "Col1" , values = "Col2")
# print(result)


Data={
    'Course':['CIVIL','CS','CIVIL','CS','CIVIL'],
    'Year':['1','2','1','1','2'],
    'Student':[52,56,73,83,83]
}

df = pd.DataFrame(Data)
print(df)

result = df.pivot_table(
    index = 'Course',columns='Year',values = 'Student', aggfunc='sum'
)
print(result)


