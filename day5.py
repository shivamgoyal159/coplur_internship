import pandas as pd      #pd = pandas directory

a = [10,20,30,40]

# s = pd.Series(a)   #write pd if as pd is given otherwise write pandas.series()   ye column me deta h
# print(s[1])
# print(type(s))


# s = pd.Series(a,index=['a','b','c','d'])
# print(s['b'])
# print(type(s))


# data = {"num":[10,20,30,40],
#       "alpha":['A','B','C','D']
# }
# df = pd.DataFrame(data)
# print(df)
# print("--------------------------------------")
# print(df.loc[1])
# print(df.loc[[0,1]]) # do eaksath karane h to 2 square bracket lagane padenge
# print(df.columns)   # printing columns name
# df.columns=["cup","cake"]    #modify column name
# print(df)


# marks = {"day1":583, "day2":483, "day3":884}
# var = pd.Series(marks,dtype=float)
# print(var)


# marks = {"day1":583, "day2":483, "day3":884}
# var = pd.Series(marks,index=['day1','day2','day3'])
# print(var['day2'])


# print(df)
# print(type(df))
#
# print(pd.__version__)   # state the version of pandas


# df = pd.DataFrame([['a','b'],['c','d'], ['e','f'], ['g','h']], columns=['col1', 'col2'])
# print(df)
# result = df.iloc[1:3, :]   #ilog index ke liye hota h
# # result = df.iloc[1:3]  #same h
# print(result)


# df = pd.DataFrame([['a','b'],['c','d'], ['e','f'], ['g','h']], columns=['col1', 'col2'],index = ['r1','r2','r3','r4'])
# print(df)
# result = df.loc['r1':'r2','col1']    #loc string ke liye hota h
# print(result)



# data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
# df = pd.DataFrame(data)
# col_A = df.loc[:, 'A']    # ':' isme specify nhi karenge to sare index ke liye dega
# # col_A = df.loc[1:2, 'A']    #isme specify kara h kara h kaha tak ke liye print karayega
# print(col_A)

#
# df = pd.DataFrame([['a','b'],['c','d'],['e','f'],['g','h']],
#                   columns=['col1','col2'])
# print(df)
# # TO MODIFY
# # df.iloc[1:3]=['x','y']      # columm number specify nhi kiya to dono sari jagah change karega
# # df.iloc[1:3,0]=['x','y']     # columm number 0 pe change karega
# # df.iloc[1:3,1]=['x','y']        # columm number 1 pe change karega
# df.iloc[0:3:2,1]=['x','y']         # ::2 is to change on even places
# print(df)



#TO DROP
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],'B': [4, 5, 6, 7, 8],
      'C': [9, 10, 11, 12, 13]},index=['r1', 'r2', 'r3', 'r4', 'r5'])

print(df)
# result = df.drop(['r1', 'r3'])
# result = df[df["C"] != 10]
result = df[df[["A","B"]] != 4]
print(result)










