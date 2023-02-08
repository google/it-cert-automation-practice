#!/usr/bin/env python3
def validate_user(username, minlen):
    assert type(username) == str, "username must be a string"
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen: # if length of username is smaller than defined minimum length, RETURN the value False
        return False
    if not username.isalnm(): # if the username does not contain alphanumeric characters, RETURN the value False
        return False
    return True # else RETURN the value True
