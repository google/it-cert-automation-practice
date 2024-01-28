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
    # Usernames can only use letters, numbers, and underscores
    if not re.match('^[a-zA-Z][a-zA-Z0-9_]*$', username):
        return False
    # Usernames can't begin with a number
    if username[0].isdigit():
        return False
    return True

# Тестирование функции
print(validate_user("john_doe", 3))   # True
print(validate_user("jane.doe", 3))   # False
print(validate_user("john_doe", 5))  # True
print(validate_user("12john_doe", 3))   # False
