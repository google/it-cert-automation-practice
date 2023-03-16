#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if not isinstance(username, str):
        raise TypeError("username must be a string")
    if not isinstance(minlen, int) or minlen < 1:
        raise ValueError("minlen must be an integer greater than or equal to 1")
 
    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-z][a-z0-9]*([._][a-z0-9]+)*$', username):
        return False
    # Usernames can't begin with a number
    if username[0].isdigit():
        return False
    return True

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False
