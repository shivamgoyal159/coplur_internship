import sqlite3

conn = sqlite3.connect("db1.db")

data = conn.execute("select * FROM users")
for x in data:
    print(x)

id = input("ID to delete:")
conn.execute("DELETE FROM users where usid =" +id)
conn.commit()

data = conn.execute("select * FROM users")
for x in data:
    print(x)

conn.close()