#!/usr/bin/env python3

import re

def validate_user(username, minlen):

    if type(username) != str:
        raise TypeError("username harus string")
    if minlen < 1:
        raise ValueError("minlen minimal harus 1")

    if len(username) < minlen:
        return False

    if not re.match('^[a-z0-9._]*$', username):
        return False

    if not username[0].isalpha():
        return False
    return True

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False
