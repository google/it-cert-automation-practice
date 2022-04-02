#!/usr/bin/env python3

import re

def validate_user(un, ml):
    """Checks if the received username matches the required conditions."""
    if type(un) != str:
        raise TypeError("username must be a string")
    if ml < 1:
        raise ValueError("minlen must be at least 1")

    # Usernames can't be shorter than minlen
    if len(un) < ml:
        return False

    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-z0-9._]*$', un):
        return False

    # Usernames can't begin with a number
    if not un[0].isalpha():
        return False
    return True

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False


