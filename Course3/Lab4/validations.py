#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can only use letters, numbers, dots, and underscores
    if not re.match('^[a-z0-9._]*$', username):
        return False
    # Usernames can't begin with a number
    if username[0].isnumeric():
        return False

    # Additional check to ensure the first character doesn't start with a dot or underscore
    if username[0] in ['.', '_']:
        return False

    return True

# Test cases
print(validate_user("user123", 3))  # True
print(validate_user(".username", 3))  # False
print(validate_user("_username", 3))  # False
print(validate_user("123user", 3))  # False

