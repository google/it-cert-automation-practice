#!/usr/bin/env python3

import re 

def validate_user(username, minlen):
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    if len(username) < minlen:
        return False
    if not re.match('^[a-z0-9._]*$', username):
        return False
    if username[0] in ['_', '.'] or username[-1] in ['_', '.']:
        return False
    if username[0].isnumeric():
        return False
    return True

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # False


