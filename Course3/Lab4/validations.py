def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) is not str or minlen < 1:
        return False
    if len(username) < minlen:
        return False
    if not username[0].isalpha():  # Check if the first character is a letter
        return False
    # Ensure that the username contains only letters, numbers, dots, or underscores
    for char in username:
        if not (char.isalnum() or char in ['.', '_']):
            return False
    return True

# Testing lines
print(validate_user("blue.kale", 3))        # Expected: True
print(validate_user(".blue.kale", 3))       # Expected: False
print(validate_user("red_quinoa", 4))       # Expected: True
print(validate_user("_red_quinoa", 4))      # Expected: False
