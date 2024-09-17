#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    # Check if the username starts with a letter or number and is of valid length
    if len(username) < minlen:
        return False
    if not username[0].isalnum():
        return False
    # Ensure only valid characters are used (letters, numbers, dots, and underscores)
    if not re.match(r'^[\w.]+$', username):
        return False
    return True

# Test cases
print(validate_user("blue.kale", 3))  # True
print(validate_user(".blue.kale", 3))  # False
print(validate_user("red_quinoa", 4))  # True
print(validate_user("_red_quinoa", 4))  # False
