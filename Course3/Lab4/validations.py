#!/usr/bin/env python3
import re
def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if username[0].isnumeric():
        return False
    if re.match('^[._]',username):
        return False
    if not re.match('^[a-z0-9_.]*$',username):
        return False
    if len(username) < minlen:
        return False
    return True
print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False


