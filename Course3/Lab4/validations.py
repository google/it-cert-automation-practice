#!/usr/bin/env python3

import re

def validate_user(username, minlen=3):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("Username must be a string")
    if minlen < 1:
        raise ValueError("Minimum length must be at least 1")
    
    # Usernames can't be shorter than the minimum length
    if len(username) < minlen:
        return False
    # Usernames can only use lowercase letters, digits, dots, and underscores
    if not re.match('^[a-z][a-z0-9._]+$', username):
        return False
    return True

# Test cases
print(validate_user("blue.kaleidoscope"))  # True
print(validate_user(".blue.kaleidoscope"))  # False
print(validate_user("red_quinoa"))  # True
print(validate_user("_red_quinoa"))  # False

