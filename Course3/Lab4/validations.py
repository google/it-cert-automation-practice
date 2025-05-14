#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Sprawdza, czy nazwa użytkownika spełnia wymagania."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    # Zbyt krótka nazwa
    if len(username) < minlen:
        return False

    # Nie może zaczynać się od kropki, podkreślnika ani cyfry
    if username[0] in '._' or username[0].isnumeric():
        return False

    # Dozwolone tylko litery, cyfry, kropki i podkreślniki
    if not re.match('^[a-zA-Z0-9._]+$', username):
        return False

    return True

# TESTY
print(validate_user("blue.kale", 3))      # True
print(validate_user(".blue.kale", 3))     # False
print(validate_user("red_quinoa", 4))     # True
print(validate_user("_red_quinoa", 4))    # False

