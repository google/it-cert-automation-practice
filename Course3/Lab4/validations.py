#!/usr/bin/env python3
import re
def validate_user(username, minlen):
    assert type(username) == str, "Username must be a string"
    if minlen < 1:
        raise ValueError("minlen must be atleast 1")
    if len(username) < minlen:
        return False
    #if not username.isalnum():
     #   return False
    if not re.match('(?![_.])^[a-z0-9._]*$', username):
        return False  
   # if username[0].isnumeric():
    #    return False
    return True
    
print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False
