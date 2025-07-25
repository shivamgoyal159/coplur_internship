
from db import conndb
import auth

def menu():    
    print("1. Register")
    print("2. Login")
    print("3. Logout")
    print("4. Change Password")
    print("5. Exit")

def main():
    conndb()
    while True:
        menu()
        choice = input("Select option: ")
        if choice == '1':
            auth.register()
        elif choice == '2':
            auth.login()
        elif choice == '3':
            auth.logout()
        elif choice == '4':
            auth.change_password()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
