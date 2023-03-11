#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if  not isinstance(username, str):
        return False
    if not isinstance(minlen, int) or minlen < 1: 
        return False
 
    
    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-zA-Z0-9._]*$', username):
        return False
    # Usernames can't begin with a number
    if username[0].isdigit():
        return False

    return True

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale#", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("8red_quinoa", 4)) # Currently True, should be False

