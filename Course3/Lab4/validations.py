#!/usr/bin/env python3

import re
import string

def is_special_character(char):
    # Define a set of special characters
    special_characters = set("._!@#$%^&*()_+-={}[]|:;,<.>?/\\")

    # Check if the input character is in the set of special characters
    return char in special_characters

def first_char_not_special(input_string):
    if len(input_string) > 0:
        first_char = input_string[0]
        if not is_special_character(first_char):
            return True
    return False


def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    
    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-z0-9._]*$', username):
        return False
    # Usernames can't begin with a number
    if username[0].isnumeric():
        return False

    if is_special_character(username[0]):
        return False

    return True
print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False

