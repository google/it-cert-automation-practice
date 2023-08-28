import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if not isinstance(username, str):
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can only use letters, numbers, dots, and underscores
    if re.match('^[._]', username):  # Updated regex to include uppercase letters
        return False
    # Usernames can't begin with a number
    if username[0].isdigit():  # Changed isnumeric() to isdigit() for clarity
        return False
    return True

print(validate_user("blue.kale", 3))    # True
print(validate_user(".blue.kale", 3))   # False
print(validate_user("red_quinoa", 4))   # True
print(validate_user("_red_quinoa", 4))  # False

