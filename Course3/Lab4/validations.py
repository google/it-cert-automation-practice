#!/usr/bin/env python3

import re

def validate_user(username, min_length):
    if len(username) < min_length:
        return False
    if username[0] in ['.', '_']:
        return False
    if not all(char.islower() or char == '.' for char in username):
        return False
    # Check if the username has consecutive dots ('..')
    if '..' in username:
        return False
    return True

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # False

