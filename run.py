#!/usr/bin/env python3.8
from user import User

def createUserAccount(firstName, lastName, username, password):
    new_user = User(firstName, lastName, username,password)