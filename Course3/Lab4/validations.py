#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:  
        raise ValueError("minlen must be at least 1")
    
    """
    Usernames can't be shorter than minlen
    Username should be not numeric
    Username should always starts with charactor and should consists of charactors, numbers, '.', '_'
    """
    if (len(username) < minlen) or (not re.match(r'^[a-z][a-z0-9._]*$', username)) or (username[0].isnumeric()): # changes in Regex and remove the repetition of code 
        return False
    return True



