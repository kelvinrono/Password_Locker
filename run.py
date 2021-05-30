#!/usr/bin/env python3.8
from user import User
import random
from credential import Credentials
def createUserAccount(firstName, lastName, username, password):
    '''
    This function will create a new user account
    '''
    new_user = User(firstName, lastName, username,password)
    return new_user

def create_credentials(credential_account, credential_username,credential_password):
    '''
    Function to create new contact
    '''
    new_credentials = Credentials(credential_account, credential_username, credential_password)
    return new_credentials


def save_user(user):
    '''
    Function that will save the user
    '''


def save_credentials(credential):
    '''
    Function to save contact
    '''
    credential.save_credentials()

def display_user():
    return User.display_user()


def display_credentials():
    return Credentials.display_credentials()

def randomgenerator():
    '''
    This is a method that will create random passwords
    '''
    rand = random.randint(10000,99999)
    return rand

def main():
    print('Welcome to password ;Locker app,please enter your name \n')
    user_name = input()
    print(f"Hello {user_name}. please create password locker acount first")
    print("\n")

    while True:
        print("Use the following codes to proceed:\n na - create a new Locker,\n  ex - exit the password locker app")
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

            save_user(createUserAccount(first_name, last_name, userName,password))#create and save new contact
            print("\n")
            print(f"New user {first_name} {last_name} has been create and saved!")
            print("\n")

            while True:
                print("Use these short codes:\ncc - Create credentials details,\ndc - display credential details,\nex - exit the contact list, \n del - delete account")
                short_code = input().lower()
                
                if short_code == 'cc':
                    print("New Account")
                    print("-"*30)
                    
                    print("Account Type(eg. Facebook, twitter, instagram...) : ")
                    type = input()
                    
                    print("User name : ")
                    username = input()
                    while True:
                        print("use these codes to choose the password modes:\n gp - system generated password,\n tp - type password,\n ")
                        pass_code = input().lower()
                        enteredPassword = ''
                        if pass_code=='tp':
                            print('Enter your password')
                            enteredPassword = input()
                        elif pass_code=='gp':
                            print('Enter your password')
                            enteredPassword = randomgenerator()

                        save_credentials(create_credentials(type, username, enteredPassword))#create and save new contact
                        print("\n")
                        print(f"New contact {username} for {type} saved successfully")
                        print("\n")

                        break
                elif short_code == 'dc':

                    if display_credentials():
                        print("These are the accounts saved in the app:")
                        print('\n')

                        for credential in display_credentials():
                                print(f"{credential.credentials_account} {credential.credentials_username} .....{credential.credentials_password}")

                        print('\n')

                elif short_code=='del':
                    
                    pass
                elif short_code =='ex':
                        print('\n')
                        print("Thanks for using the app. Welcome")
                        break
          
        break
      

        

main()
    

