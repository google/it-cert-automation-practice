#!/usr/bin/env python3


import re

def validate_user(username, minlen):
    
    status = 0
    
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
        status = status + 1
    
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
        status = status + 1
    
    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        status = status + 1
    
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-z0-9._]*$', username):
        status = staus + 1
    
    # Usernames can't begin with a number
    if not username[0].isalpha():
        status = status + 1
        
    if status != 0:
        return False
    else:
        return True 

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False

