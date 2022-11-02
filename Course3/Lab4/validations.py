#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
 
    # length check
    if len(username) < minlen:
        return False
    # regualr expression first character check
     if re.match('[._!?"\']',username[0]):
        return False
    #is number check condition
    if username[0].isnumeric():
        return False
    return True



