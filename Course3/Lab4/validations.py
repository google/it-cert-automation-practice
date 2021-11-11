#!/usr/bin/env python3




import re

status = "True"

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    check_to_do = [checklength, checkallleter, checkstartLetter]

    length = len(check_to_do)
    for i in range(length):
        status = check_to_do[i](username,minlen)
        if status is None:
            return True




def checklength(username,minlen):
    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False



def checkallleter(username,minlen):
    # Usernames can only use letters, numbers, dots and underscores

    if not re.match('^[a-z0-9._]*$', username):
        return False


def checkstartLetter(username,minlen):
    # Usernames can't begin with a number
    if username[0].isnumeric():
        return False





print(validate_user("blue.kale", 3))  # True
print(validate_user(".blue.kale", 3))  # Currently True, should be False
print(validate_user("red_quinoa", 4))  # True
print(validate_user("_red_quinoa", 4))  # Currently True, should be False
