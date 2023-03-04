#!/usr/bin/env python3

import re

def validate_user(username, min_length):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("Username must be a string")
    if min_length < 1:
        raise ValueError("Minimum length must be at least 1")

    if len(username) < min_length:
        return False

    if not re.match('^[a-z0-9._]*$', username):
        return False

    if username[0].isnumeric():
        return False

    return True

def 

