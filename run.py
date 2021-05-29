#!/usr/bin/env python3.8
from user import User

def createUserAccount(firstName, lastName, username, password):
    '''
    This function will create a new user account
    '''
    new_user = User(firstName, lastName, username,password)
    return new_user

def save_user(user):
    '''
    Function that will save the user
    '''
def display_user():
    return User.display_user()

def main():
    print('Welcome to password ;Locker app,please enter your name \n')
    user_name = input()
    print(f"Hello {user_name}. please create password locker acount first")
    print("\n")

    while True:
        print("Use the following codes to proceed:\n na - create a new contact,\n  ex - exit the contact list")
        short_code = input().lower()

        if short_code == 'na':
            print("New Account")
            print("-"*30)
            
            print("Enter your username : ")
            userName = input()
            
            print("Enter your first name : ")
            first_name = input()

            print("Enter the last name : ")
            last_name = input()

            print("Enter your password : ")
            password = input()

        elif short_code == "ex":
                    print("Bye .......")
                    break

main()
    

