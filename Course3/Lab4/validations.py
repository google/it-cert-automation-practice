#!/usr/bin/env python3



import re



def validate_user(username, minlen):

    """Checks if the received username matches the required conditions."""

    if not isinstance(username, str):

        raise TypeError("username must be a string")

    if not isinstance(minlen, int) or minlen < 1:

        raise ValueError("minlen must be an integer and at least 1")

    

    # Usernames can't be shorter than minlen

    if len(username) < minlen:

        return False

    # Usernames can only use letters, numbers, dots, and underscores

    # Usernames can't begin with a number, dot, or underscore

    if not re.match(r'^[a-zA-Z][a-zA-Z0-9._]*$', username):

        return False

    

    return True



# Test cases

print(validate_user("blue.kale", 3))  # True

print(validate_user(".blue.kale", 3)) # False

print(validate_user("red_quinoa", 4)) # True

print(validate_user("_red_quinoa", 4)) # False


