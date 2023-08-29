#!/usr/bin/env python3
import re

def validate_user(username, min_length):
    if re.match(r'^[a-zA-Z]', username) and len(username) >= min_length:
        return True
    return False

# Test cases
print(validate_user("blue.kale", 3))  # True
print(validate_user(".blue.kale", 3))  # Saat ini True, seharusnya False
print(validate_user("red_quinoa", 4))  # True
print(validate_user("_red_quinoa", 4))  # Saat ini True, seharusnya False

