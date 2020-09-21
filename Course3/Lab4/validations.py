#!/usr/bin/env python3

import re


def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    """
    Username can't be shorter than minlen
    Username should be not numeric
    Username should always starts with letter and should consists of letters, numbers, dots and underscore
    """
    if (len(username) < minlen) or (not re.match(r'^[a-z][a-z0-9._]*$', username)) or (
    username[0].isnumeric()):  # changes in Regex and remove the repetition of code
        return False
    return True

print(validate_user("a", 1)) # should be True
print(validate_user("abc", 1)) # should be True
print(validate_user(".a", 1)) # currently True but should be False
print(validate_user("1", 1)) # currently True but should be False
print(validate_user("_a1ca", 1)) # currently True but should be False
