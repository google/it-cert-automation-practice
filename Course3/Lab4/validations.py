import re

def validate_user(username, min_length):
    if min_length < 1:
        return False

    # Check the length of the username
    if len(username) < min_length:
        return False

    # Check if the first character is a letter
    if not re.match(r'^[a-zA-Z]', username):
        return False

    # Check if the username contains only letters, numbers, and underscores
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        return False

    return True

# Test cases
print(validate_user("blue.kale", 3))      # False
print(validate_user(".blue.kale", 3))     # False
print(validate_user("red_quinoa", 4))     # True
print(validate_user("_red_quinoa", 4))    # False

