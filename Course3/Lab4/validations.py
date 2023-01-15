#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    pattern = '^[a-zA-Z][a-zA-Z0-9._]*$'
    if not re.match(pattern, username) or len(username) < minlen:
        raise ValueError("The username must begin with a letter and can only contain letters, numbers, dots, and underscores")
    return True

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # False
