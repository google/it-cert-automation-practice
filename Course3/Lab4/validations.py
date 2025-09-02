#!/usr/bin/env python3
import re





pattern = r"^[\-\._\s@#!?/\\:]"   # ^ = inicio, [ ] = conjunto prohibido



def validate_user(username, minlen, pattern=None):

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

    # Username can´t start wtih, especial characters.

    if pattern:

        if re.match(pattern, username):

            return False

    # Usernames can't begin with a number

    if username[0].isnumeric():

        return False

    return True



pattern = r"^[\-\._\s@#!?/\\:]"   # ^ = inicio, [ ] = conjunto prohibido



print(validate_user("blue.kale", 3)) # True

print(validate_user(".blue.kale", 3,pattern)) # Currently True, should be False

print(validate_user("red_quinoa", 4,)) # True

print(validate_user("_red_quinoa", 4, pattern)) # Currently True, should be False
