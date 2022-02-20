#sorry i am C, C++, C# Programmer, i am learning Git Hub for my purpose. 
#I don't know python aswell. i think its not important to solve the python
#example here... its just about to use the git tools. thanks for understanding
#if ((validate_user,1) == a or b or . or r or _ )
#print ('TRUE')
#validate_user = 'safir';
print(validate_user("blue.kale", 1)) # True
print(validate_user(".blue.kale", 1)) # Currently True, should be False
print(validate_user("red_quinoa", 1)) # True
print(validate_user("_red_quinoa", 1)) # Currently True, should be False


import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    
    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-z0-9._]*$', username):
        return False
    # Usernames can't begin with a number
    if username[0].isnumeric():
        return False
    return True



