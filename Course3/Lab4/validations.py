#!/usr/bin/env python3

import re

def validate_user(usernaame, minlen):
    """Checks if the received username matches the required conditions."""
    if type(usernaame) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    
    # Usernames can't be shorter than minlen
    if len(usernaame) < minlen:
        return False
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-z0-9._]*$', usernaame):
        return False
    # Usernames can't begin with a number
    if usernaame[0].isnumeric():
        return False
    return True

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False
