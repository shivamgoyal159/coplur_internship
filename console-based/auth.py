
import getpass
from db import get_connection
from utils import hash_password

current_user = None  
def register():
    global current_user
    if current_user:
        print(f"User '{current_user}' is currently logged in. Please log out to register a new user.")
        return

    username = input("Enter new username: ")

    if len(username) < 5:
        print("Username must be at least 5 characters long.")
        return

    password = getpass.getpass("Enter new password: ")

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            print("Username already exists.")
            return

        hashed = hash_password(password)
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
        print("Registration successful!")

def login():
    global current_user
    if current_user:
        print("A user is already logged in.")
        return

    username = input("Username: ")
    password = getpass.getpass("Password: ")
    hashed = hash_password(password)

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT password, is_logged_in FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()

        if not row:
            print("User does not exist.")
            return
        if row[1]:
            print("User already exists ")
            return
        if row[0] != hashed:
            print("Incorrect password.")
            return

        cursor.execute("UPDATE users SET is_logged_in = 1 WHERE username = ?", (username,))
        current_user = username
        print(f"Logged in as {username}.")

def logout():
    global current_user
    if not current_user:
        print("No user is currently logged in.")
        return

    with get_connection() as conn:
        conn.execute("UPDATE users SET is_logged_in = 0 WHERE username = ?", (current_user,))
    print(f"{current_user} logged out.")
    current_user = None

def change_password():
    global current_user
    if not current_user:
        print("You need to be logged in to change password.")
        login()
        return

    current_password = getpass.getpass("Enter current password: ")
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE username = ?", (current_user,))
        stored_password = cursor.fetchone()[0]

        if hash_password(current_password) != stored_password:
            print("Incorrect current password.")
            return

        new_password = getpass.getpass("Enter new password: ")
        cursor.execute("UPDATE users SET password = ? WHERE username = ?", (hash_password(new_password), current_user))
        print("Password changed successfully.")
