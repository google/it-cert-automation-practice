#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if not isinstance(username, str):
        return False
    if minlen < 1:
        return False
    if not re.match('^[a-zA-Z][a-zA-Z0-9._]*$', username):
        return False
    return True if len(username) >= minlen else False

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # False

