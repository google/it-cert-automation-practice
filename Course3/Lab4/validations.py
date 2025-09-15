#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen:
        raise ValueError("usernames can't be shorter than minlen")
    if not re.match('^[a-z0-9._]*$', username):
        raise ValueError("usernames can only use letters, numbers, dots and underscores")
    if not username[0].isalpha():
        raise ValueError("usernames can only begin with a letter")
    return True