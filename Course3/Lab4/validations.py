#!/usr/bin/env python3


def validate_user(username, minlen):
    """Checks if the recieved username matches the required conditions."""
    flag=True
    if type(username) != str:
        print("username must be a string")
        flag=False
    if minlen < 1:
        print("minlen must be at least 1")
        flag= False
    if len(username) < minlen:
            flag= False
            print('The given username has length smaller than the minlen')
    if not  username.isalnum():
            flag= False
            print("Username contains Symbols")
        # Usernames can't begin with a number
    if username [0].isnumeric():
            print("Username begins with a number")
            flag= False
    return flag
if __name__=='__main__':  
    print(validate_user("blue.kale", 3)) # True
    print(validate_user(".blue.kale", 3)) # Currently True, should be False
    print(validate_user("red_quinoa", 4)) # True
    print(validate_user("_red_quinoa", 4)) # Currently True, should be False    
