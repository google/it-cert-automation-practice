import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    # Los nombres de usuario no pueden ser más cortos que minlen
    if len(username) < minlen:
        return False

    # Los nombres de usuario solo pueden usar letras, números, puntos y guiones bajos
    if not re.match('^[a-z0-9._]*$', username):
        return False

    # Los nombres de usuario no pueden comenzar con un número
    if not username[0].isalpha():
        return False
    return True

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False


