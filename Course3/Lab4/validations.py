#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    """ Usernames can't be shorter than minlen, must start with a letter 
    and must only consists of letters, numbers, dots, underscores"""
    if len(username) > minlen and username[0].isalpha() and re.match('^[a-z0-9._]*$', username):
        return True
    else:
        return False

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # False

