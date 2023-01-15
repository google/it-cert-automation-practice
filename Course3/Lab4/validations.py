#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if not re.match("^[a-zA-Z0-9]", username):
        raise ValueError("The first character must be alphanumeric")

    # Usernames can't be shorter than minlen
    if not username or not username[:1].isalnum():
        raise ValueError("The first character must be alphanumeric")
    if len(username) < minlen:
        raise ValueError("The username must be at least {} characters long".format(min_length))   
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-z0-9._]*$', username):
        return False
    if not str[0].isalnum():
        return False
    if not username or not re.match("^[a-zA-Z0-9]", username):
        return False
    # Usernames can't begin with a number
    if username[0].isnumeric():
        return False
    return True

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False

