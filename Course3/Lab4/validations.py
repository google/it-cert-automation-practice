import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    
    # Check for correct input types
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
        
    # Check for minimum length
    if len(username) < minlen:
        return False
        
    # Check for valid characters
    if not re.match('^[a-z0-9._]*$', username):
        return False
        
    # Check that username doesn't begin with a number
    if username[0].isnumeric():
        return False
    
    # Check that username doesn't begin with a dot or an underscore
    if username[0] in ['.', '_']:
        return False
    
    return True

# Test the function
print(validate_user("blue.kale", 3))  # Should return True
print(validate_user(".blue.kale", 3))  # Should return False
print(validate_user("red_quinoa", 4))  # Should return True
print(validate_user("_red_quinoa", 4))  # Should return False
