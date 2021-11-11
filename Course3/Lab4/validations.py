#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """
    Checks if the received username matches the required conditions.

    >>> validate_user("blue.kale", 3)
    True
    >>> validate_user(".blue.kale", 3)
    False
    >>> validate_user("red_quinoa", 4)
    True
    >>> validate_user("_red_quinoa", 4)
    False
    >>> validate_user("3red_quinoa", 4)
    False

    """

    if type(username) != str:
        raise TypeError("username must be a string")

    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False

    # Usernames can only use letters, numbers, dots and underscores
    if not re.match("^[A-Za-z][a-zG -9._]*$", username):
        return False

    return True


if __name__ == "__main__":

    import doctest
    doctest.testmod()
