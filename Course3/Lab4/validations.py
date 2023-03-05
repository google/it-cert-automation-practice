#!/usr/bin/env python3
import re

def validate_user(username, minlen):
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-zA-Z][a-zA-Z0-9_.]*$', username):
        return False
    # Usernames can't begin with a number, dot or underscore
    if username[0].isdigit() or username[0] == '.' or username[0] == '_':
        return False
    return True

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # False
