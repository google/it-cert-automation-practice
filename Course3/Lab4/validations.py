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
    if not username.isalnum():
            flag= False
            print("Usernames can't begin with a number")
        # Usernames can't begin with a number
    if username [0].isnumeric():
            print("The Username contians symbols")
            flag= False
    return flag
if __name__=='__main__':
    username=input('Enter the Username: ')
    minlen=int(input('Enter the minimum length of the Username: '))
    if validate_user(username,minlen): 
         print('Ooo hooo the username is Accepted')
    else:
         pass    
    
