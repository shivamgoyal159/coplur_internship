print("-------------------------------Question 1------------------------------")

import csv

data = [
    ["Name","Address","Mobile","email"],
    ["mohit","ABC","9863281908","gdsvw@gmail.com"],
    ["mohan","DEF","8862545183","fbcxhva@gmail.com"],
    ["manish","GHI","9197346393","vjbwrw@gmail.com"],
]

with open("account.csv","w")as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)


print("-------------------------------Question 3------------------------------")

import sqlite3

conn = sqlite3.connect("db2.db")

conn.execute('''
Create table users(
usid INTEGER PRIMARY KEY AUTOINCREMENT,
usnm VARCHAR(100),
pass VARCHAR(50),
mobile VARCHAR(15),
email VARCHAR(50)
)
''')

