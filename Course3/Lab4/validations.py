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

    # If all conditions are met, the username is valid
    return True

# Example usage
print(validate_user("user", 3))        # Should return True
print(validate_user("usr123", 6))      # Should return False
print(validate_user("my_username", 5)) # Should return True
print(validate_user("123abc", 5))      # Should return False
