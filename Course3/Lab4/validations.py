#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if not isinstance(username, str):
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    # Check length *after* other checks to avoid short-circuiting regex
    if not re.match(r"^[a-zA-Z_][a-zA-Z0-9._]*$", username):  # Correct regex
        return False
    if len(username) < minlen: #Move this condition after the regex condition
        return False
    return True


print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False
