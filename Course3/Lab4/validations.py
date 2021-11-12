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
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-zA-Z].[a-z0-9._]*$', username):
        return False
    # Usernames can't begin with a number
    if username[0].isnumeric():
        return False
    return True


print(validate_user("alicia.lore", 5))  # True
print(validate_user("_tico.moreno", 6))  # False
print(validate_user(".pepe.gonza", 5))  # False
print(validate_user("valid.user", 4))  # True
print(validate_user("too_short", 10))  # False
print(validate_user("J.doe", 4))  # True
