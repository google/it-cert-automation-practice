#!/usr/bin/env python3


import re



def validate_user(username, min_length):

    # Check if username starts with an alphabetic character, followed by alphanumeric characters or underscores

    pattern = r"^[a-zA-Z]"

    if len(username) >= min_length and re.match(pattern, username):

        return True

    else:

        return False

print(validate_user("blue.kale", 3))  # True

print(validate_user(".blue.kale", 3))  # False

print(validate_user("red_quinoa", 4))  # True

print(validate_user("_red_quinoa", 4))  # False


