#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if username[0].isnumeric():
        return False
    if not re.match('^[a-z]*$', username[0]):
        return False
    return True


print(validate_user("blue.kale", 3)) # 
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False 


