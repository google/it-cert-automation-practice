#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[A-Za-z0-9].*', username):
        return False
    # Usernames can't begin with a number
    if username[0].isnumeric():
        return False
    return True



