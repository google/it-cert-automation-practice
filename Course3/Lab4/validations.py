#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if username[0]== ('!' or  '@' or  '#' or '$' or '%' or '^' or '&' or '*' ):
        raise TypeError("username must not start with a special character")
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    
    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-z0-9._]*$', username):
        return False
    # Usernames can't begin with a number
    if username[0].isnumeric():
        return False
    for i in username[0] :
        if  ((ord(i) >= 32 and ord(i) < 48)or(ord(i) >= 91 and ord(i) < 97)or (ord(i) >= 123 and ord(i) < 127) or (ord(i) >= 58 and ord(i) < 65) ):
            return False
    return True
print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False


