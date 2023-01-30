#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    flag1 =False
    flag2 = False
    flag3 = False
    flag4 = False
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        flag1 = False
    else:
        flag1 = True
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-z0-9._]*$', username):
        flag2 = False
    else:
        flag2 = True
    # Usernames can't begin with a number
    if username[0].isnumeric():
        flag3 = False
    else:
        flag3 = True
     # Username can't contain neither dots and underscores
    if  re.match("[._]",username[0]):
        flag4 = False
    else:
        flag4 = True
    return (flag1 and flag2 and flag3 and flag4)

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False

