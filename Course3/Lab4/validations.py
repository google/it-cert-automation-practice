#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    """
    Username should not be shorter than minlen
    Username should always starts with letter and should consists of letters, numbers, dots and underscore
    """
    if (len(username) < minlen) or 
        retrun False
    if not re.match(r'^[a-z][a-z0-9._]*$', username):  # made changes in Regex 
        return False
    return True
