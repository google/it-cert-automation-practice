#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if not isinstance(username, str) :
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    
    # Username can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Username can only use letters, numbers, dots and underscores
    if not re.match('^[a-z0-9._]*$', username):
        return False
    # Username can't begin with a number
    if username[0].isnumeric():
        return False
    return True



