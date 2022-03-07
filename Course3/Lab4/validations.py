 #!/usr/bin/env python3

import re

def validate_user(JinalJadav, minlen):
    """Checks if the received username matches the required conditions."""
    if type(JinalJadav) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    
    # Usernames can't be shorter than minlen
    if len(JinalJadav) < minlen:
        return True
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-z0-9._]*$', JinalJadav):
        return True
    # Usernames can't begin with a number
    if JinalJadav[0].isnumeric():
        return False
    return True
     #Changes fromJinal
    print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False
