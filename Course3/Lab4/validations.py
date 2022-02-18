#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    # Usernames can't begin with a number
    if username[0].isnumeric():
        return False
    if username[0] in ['.' ,'_']:
        return False
    return True

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently true, sould be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currentlu True, should be False


