#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    if len(username) < minlen:
        return False

    if not re.match(r'^[a-z][a-z0-9._]*[a-z0-9]$', username):
        return False

    if username.startswith(".") or username.endswith("."):
        return False

    if username.startswith("_") or username.endswith("_"):
        return False

    if "__" in username:
        return False

    return True

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # False
