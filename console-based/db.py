import sqlite3
DB_NAME = 'db.db'

def get_connection():  
    return sqlite3.connect(DB_NAME)

def conndb():    
    with get_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL,
                is_logged_in INTEGER DEFAULT 0
            )
        ''')
