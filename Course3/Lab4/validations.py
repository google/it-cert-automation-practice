#!/usr/bin/env python3

import re


def is_username_string(username):
  return type(username) is str

def has_required_length(minlen):
  return minlen > 1


# Functions probably need rewriting with args and kwargs
def is_username_shorter(username, minlen):
  return len(username) < minlen

def has_forbidden_characters(username, minlen):
  return not re.match('^[a-z0-9._]*$', username)

def has_forbidden_first_character(username, minlen):
  return re.match(r'^[._]', username)

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if not is_username_string(username):
        raise TypeError("username must be a string")
    if not has_required_length(minlen):
        raise ValueError("minlen must be at least 1")
    checks = [is_username_shorter, has_forbidden_characters, has_forbidden_first_character]
    for check in checks:
        if check(username, minlen):
            return False   
    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-z0-9._]*$', username):
        return False
    # Usernames can't begin with a number
    if username[0].isnumeric():
        return False
   
    return True

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False

