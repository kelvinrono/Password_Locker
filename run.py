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
    user.save_user()
