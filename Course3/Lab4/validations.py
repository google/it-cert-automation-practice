#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the username matches the required conditions."""
    if type(username) != str:
        raise TypeError("Username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1.")
    Forbidden = ".<_>:/\|?*"
    for f in Forbidden:
        if username[0] in Forbidden:
            return False 
    
    # Usernames cant be shorten than minlen
    if len(username) < minlen:
        return False
    # Usernames can only user letter, numbers, dots and underscores
    if not re.match('^[a-z0-9._]*$', username):
        return False
    # Usernames cant beginn with a number
    if username[0].isnumeric():
        return False
    return True

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False
    
  


