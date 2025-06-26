import pandas as pd
import numpy as np

# data = {"Col1":[3,np.nan,np.nan,2],"Col2":[1.0,pd.NA,pd.NA,2.0],}
# df = pd.DataFrame(data)
#
# print(df)
#
# f = df.fillna('-')
# print("\n",f)
#
# print("--------------------")
#
# df = pd.DataFrame([[5,7,2],[9,6,3],[8,4,7]],
#                   index=['a','b','c'],columns=['one','two','three'])   #agar ek 'f' dede jo ki index me h hi nhi to use vo dhikayega hi nhi
#
# df = df.reindex(['a','b','c','d','e'])   # 'reindex' use to change index
# print(df)
#
# print("--------------------")
#
# # result = df.ffill()   #forward fill - it
# # print(result)
# print(df.ffill())
#
# print("--------------------")
#
# # result = df.bfill()   #forward fill - it
# # print(result)
# print(df.bfill())
# print(df.reindex(['a', 'b', 'c', 'd', 'e']).bfill())    #just to print not to assign
#
# print("-------------------")
#
# print(df.ffill(limit=1))  #just foilling one empty space as limit is 1
#
# print("-------------------")
#
# print(df.bfill(limit=1))




# print("----------replace---------")
#
# df = pd.DataFrame({'one':[5,12,3,45,64,7],'two':[52,73,7,27,0,673]})
# print(df.replace({5:77777,7:4682284367}))    #yaha shrif change hoke print hori h permanently change nhi hori
# print(df)

# result = df.replace({5:77777,7:4682284367})
# print(result)


# print("-------------replace by regex----------")
#
# df = pd.DataFrame(['$40.000*','$40000 conditions attached'],columns=['P'])
# print(df)
#
# df['P'] = df['P'].str.replace(r'\D+','',regex=True).astype('int')
# print(df)
#
# print("----------group by-----------")
#
#
# data = {
#     'Department': ['HR', 'HR', 'IT', 'IT', 'Finance'],
#     'Salary': [30000, 35000, 50000, 55000, 60000]
# }
#
# df = pd.DataFrame(data)
#
# print("-------sum-------")
#
# group_data = df.groupby('Department')['Salary'].sum()
# print(group_data)
#
# print("-------count-------")   # doesn't count nan values
#
# group_data = df.groupby('Department')['Salary'].count()
# print(group_data)
#
# print("-------mean-------")
#
# group_data = df.groupby('Department')['Salary'].mean()
# print(group_data)
#
# print("-------min-------")
#
# group_data = df.groupby('Department')['Salary'].min()
# print(group_data)
#
# print("-------max-------")
#
# group_data = df.groupby('Department')['Salary'].max()
# print(group_data)
#
# print("-------size-------")   # count nan values
#
# group_data = df.groupby('Department')['Salary'].size()
# print(group_data)
#
# print("--------multiple column---------")
#
# data = {
#     'Department': ['HR', 'HR', 'IT', 'IT', 'Finance'],
#     'Name':['x','x','jnhae','trbsb','arwbsf'],
#     'Salary': [30000, 35000, 50000, 55000, 60000]
# }
#
# df = pd.DataFrame(data)
# print(df)
#
# g = df.groupby(['Department','Name'])['Salary'].mean()
# print(g)


# print("-----------sort----------")
#
# data = {'Name':['BAB','CAC','ABA'],'Age':[93,73,16]}
# df = pd.DataFrame(data)
# result = df.sort_values(by='Name')
# result = df.sort_values(by='Age')
# result = df.sort_values(['Name','Age'],ascending=[True,False])     #pahala true\false chalega name ke liye usme check
#                                                                     karega agar name same hua to doosra true ya false
#                                                                     chalega Age ke liye un dono same name ke lie
# result = df.sort_index(ascending=False)
# result = df.sort_index(ascending=True)
""""---------THODI BHAUT RAHA GYI NOTES SE KAR LENA----------"""
# print(result)

# print("------------------Date function-----------------")
#
# print(pd.date_range('6/1/2025',periods=5))  #to print next dates including given date
#
# print("-------------loading csv in dataframe----------------")
#
# df = pd.read_csv('Data.csv')
# print(df)
# print(df['First Name'].value_counts())
# #
# print("---------------------------------")

# print(df.to_string())     #to print full file data without this it will show -- after some data
# print(df.head())   #FIRST FIVE OTHERWISE SPECIFY LIKE (10)
# print(df.head(12))
# print(df.tail())   #last 5 otherwise specify
# print(df.tail(10))
# print(df.info())
# print(df.describe())
# print(df.shape)
# print(df.columns)   # state all the columns

# filtered_df = df[df['Index']>99]    #pura nhi h
# print(filtered_df)


# group_data = df.groupby('City')['Index'].count()
# group_data = df.groupby('City')['Index'].mean()
# print(group_data)


# pd.options.display.max_rows = 100
# df = pd.read_csv('data.csv')
# print(df)

# df = pd.read_csv('customers')      """pura nhi h"""

df = pd.read_csv('Data.csv')
x = df["Index"].mean()
df.fillna({"Index":x},inplace=True)
print(df)