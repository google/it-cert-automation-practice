#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions.function: validate_user(username,minimum_length)"""
    if type(username) != str:
        raise TypeError("username must be a string")
     
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    
    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        print("Username is smaller than minimum!")
        return False
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-z0-9._]*$', username):
        print("Username can only use small letter,numbers,dots and underscores.")
        return False
    # Usernames can't begin with a number
    if username[0].isnumeric():
        print("Username can't begin with a number!! ")
        return False
    return True



