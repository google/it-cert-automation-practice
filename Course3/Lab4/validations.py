#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    check = True
    if type(username) != str:
        check = False
        raise TypeError("username must be a string")
    if minlen < 1:
        check = False
        raise ValueError("minlen must be at least 1")
    
    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        check = False
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-z0-9._]*$', username):
        check = False
    # Usernames can't begin with a number
    if username[0].isnumeric():
        check = False
    if not re.match('^[a-z]*$', username[0]):
        check = False
    return check

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False
