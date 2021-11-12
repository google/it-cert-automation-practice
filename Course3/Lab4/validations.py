#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    bool = True
    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        bool = False
    # Usernames can only use letters, numbers, dots and underscores
    elif not re.match(r'^[a-z0-9\._]+$', username):
        bool = False
    # Usernames can't begin with a number
    elif  re.match(r'\.|\_|\d ', username[0]):
        bool = False
    return bool



print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False



