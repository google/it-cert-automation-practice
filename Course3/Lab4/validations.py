#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-zA-Z][a-zA-Z0-9._]*$', username):
        return False
    # Usernames can't begin with a number
    if username[0].isnumeric():
        return False
    return True

# Print the outputs
print(str(validate_user("blue.kale", 3)).capitalize()) # True
print(str(validate_user(".blue.kale", 3)).capitalize()) # False
print(str(validate_user("red_quinoa", 4)).capitalize()) # True
print(str(validate_user("_red_quinoa", 4)).capitalize()) # False

