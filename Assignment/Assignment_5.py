print("---------------------------------Question 1-------------------------------\n")

"""1) Practise Pandas Series
Create a Pandas Series from Dictionary
Create a Pandas Series from Lists
Access the elements of a Series in Pandas"""

print("---------DICTIONARY-----------\n")

import pandas as pd

data = {'a': 10, 'b': 20, 'c': 30}
dict = pd.Series(data)
print(dict)

print("\n----------LISTS----------\n")

data = [100, 200, 300]
list = pd.Series(data)
print(list)

print("\n-----------ACCESS ELEMENT------------\n")

print(list[0])     # Access by index
print(dict['b'])   # Access by label

print("---------------------------------Question 2-------------------------------\n")

"""2) DataFrames
Make a Pandas DataFrame with a two-dimensional Python list
Create DataFrame from Python dict
Create Pandas DataFrame using list of lists
Create a Pandas DataFrame using list of tuples
Create a Pandas DataFrame from List of Dicts"""

print("-------TWO DIMENSIONAL LIST-------\n")

data = [[1, 'mohit'], [2, 'megnath'], [3, 'abhinav']]
df = pd.DataFrame(data, columns=['ID', 'Name'])
print(df)

print("\n-------dict-------\n")

data = {'Name': ['yash', 'tom'], 'Age': [25, 30]}
df_from_dict = pd.DataFrame(data)
print(df_from_dict)

print("\n--------LIST OF LISTS--------\n")

data = [['A', 90], ['B', 85], ['C', 88]]
df = pd.DataFrame(data, columns=['Grade', 'Score'])
print(df)

print("\n---------LIST OF TUPLES--------\n")

data = [('Math', 80), ('Science', 95)]
df = pd.DataFrame(data, columns=['Subject', 'Marks'])
print(df)

print("\n---------LIST OF DICTS--------\n")

data = [{'Name': 'abhi', 'Age': 25}, {'Name': 'shiv', 'Age': 30}]
df = pd.DataFrame(data)
print(df)

print("---------------------------------Question 3-------------------------------\n")

"""3) Data Iteration
Different ways to iterate over rows in Pandas DataFrame
Selecting rows in Pandas DataFrame based on conditions
Select any row from a DataFrame using iloc[]
Limited rows selection with a given column
Drop rows from the DataFrame based on a certain condition applied on a column
Insert a row at a given position in Pandas DataFrame
Create a list from rows in Pandas DataFrame"""

print("-------WAYS TO ITERATE-------")

print("-------CONDITION BASED ROWS-------")

print("-------USING ILOC[]-------")

print("--------GIVEN COLUMN SELECTION--------")

print("-------DROP ROWS CERTAIN CONDITION ON A COLUMN-------")

print("-------INSERT ROW ON POSITION--------")

print("-------LIST FROM ROWS-------")
