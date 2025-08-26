#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    
    # Check if the username is shorter than the minimum length
    if len(username) < minlen:
        return False
    
    # Check if the username starts with a number or a special character.
    # The [^a-zA-Z] part checks for any character that is not a letter.
    if re.match(r'[^a-zA-Z]', username[0]):
        return False

    # Check if the entire username contains only valid characters (letters, numbers, dots, and underscores).
    if not re.match(r'^[a-zA-Z0-9._]*$', username):
        return False
        
    return True

# Test cases
print(validate_user("blue.kale", 3)) # Should be True
print(validate_user(".blue.kale", 3)) # Should be False
print(validate_user("red_quinoa", 4)) # Should be True
print(validate_user("_red_quinoa", 4)) # Should be False
