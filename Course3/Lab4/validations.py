#!/usr/bin/env python3

import re


def validate_user(username):
    # Check if the username is empty
    if not username:
        return False

    # Check if the first character is a letter
    if not username[0].isalpha():
        return False

    # Check if all characters are valid (letters, digits, underscores, dots)
    for char in username:
        if not (char.isalnum() or char in ['_', '.']):
            return False

    return True

# Corrected function calls — only one argument each
print(validate_user("blue.kale"))      # True
print(validate_user(".blue.kale"))     # False
print(validate_user("red_quinoa"))     # True
print(validate_user("_red_quinoa"))    # False
