#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if username[0].isnumeric():
        return False
    if username[0] in ['.' ,'_']:
        return False
    return True
print(validate_user("blue.kale", 10)) # True
print(validate_user(".blue.kale", 10)) # Currently True, should be False
print(validate_user("red_quinoa", 10)) # True
print(validate_user("_red_quinoa", 10)) # Currently True, should be False

