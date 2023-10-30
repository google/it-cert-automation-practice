#!/usr/bin/env python3

import re

def validate_user(Nayankumar123456, minlen):
    """Checks if the received username matches the required conditions."""
    if type(Nayankumar123456) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    
    # Usernames can't be shorter than minlen
    if len(Nayankumar123456) < minlen:
        return False
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-z0-9._]*$', Nayankumar123456):
        return False
    # Usernames can't begin with a number
    if Nayankumar123456[0].isnumeric():
        return False
    return True



