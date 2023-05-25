#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    
    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can only use letters, numbers, dots and underscores
    # changing a pattern , 
    # first checking string does not begin with . _ or number
    # second string includes froam a-z, 0-9 and ._ char
    # third delete condition to check if  username[0] is a number.j
    if not re.match('^[^\._0-9][a-z0-9._]*$', username):
        return False
    # Usernames can't begin with a number
    # if username[0].isnumeric():
    #     return False
    return True


# example to chek what is happend
# print(validate_user("blue.kale", 3)) # True
# print(validate_user(".blue.kale", 3)) # Currently True, should be False
# print(validate_user("red_quinoa", 4)) # True
# print(validate_user("_red_quinoa", 4)) # Currently True, should be False


