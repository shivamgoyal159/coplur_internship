import sqlite3

conn = sqlite3.connect("db1.db")   # name kuch bhi le sakte h extension .db hi hoga

conn.execute('''
Create table users2(
usid INTEGER PRIMARY KEY AUTOINCREMENT ,
usnm VARCHAR(100),
pass VARCHAR(50),
mobile VARCHAR(15),
email VARCHAR(50)
)
''')

conn.close()