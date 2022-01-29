#!/usr/bin/env python3

import re


def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    k=0
    # Usernames can't be shorter than minlenø
    # Usernames can only use letters, numbers, dots and underscores
    if re.match('^[0-9._]*$', username[0]):
        k=1
        return False
    # Usernames can't begin with a number
    if username[0].isnumeric():
        k=1
        return False

    if len(username)<minlen:
        k=1
        return False
    if k==0:    
        return True
print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False

