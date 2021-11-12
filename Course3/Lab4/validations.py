#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    
    # Usernames can't be shorter than minlen or Usernames can only use letters, numbers, dot and underscore
    if len(username) < minlen or not re.match('^[a-z0-9._]*$', username):
        return False
    
    # Usernames can't begin with a number
    elif '.' in username[0] or '_' in username[0] or username[0].isnumeric():
        return False
    else:
        return True



print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False

