import sqlite3

conn = sqlite3.connect("db1.db")

conn.execute('''
INSERT INTO users(usnm , pass) VALUES ("ABC1","abc123"), ("ABC1","abc123"),("ABC1","abc123"),("ABC1","abc123") 
''')

conn.commit()
conn.close()