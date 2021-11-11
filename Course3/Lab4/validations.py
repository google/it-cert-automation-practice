#Now, add the following lines of code at the end of the script:

print(validate_user("blue.kale", 3)) # TrueNow, add the following lines 
#of code at the end of the script:#!/usr/bin/env python3 
print(validate_user(".blue.kale", 3)) # Currently True, should be False 
import re
(validate_user("blue.kale", 3)) # True 
print(validate_user(".blue.kale", 3)) # Currently True, should be False 
def validate_user(username, minlen): print(validate_user("red_quinoa", 
4)) # True """Checks if the received username matches the required 
conditions.""" print(validate_user("_red_quinoa", 4)) # Currently True, 
#should be False Once you've finished writing this script, save the file 
#by pressing Ctrl-o, the Enter key, and Ctrl-x. 
print(validate_user("red_quinoa", 4)) # True Now, run the validations.py 
on the python3 interpreter. print(validate_user("_red_quinoa", 4)) # 
#Currently True, should be False python3 validations.py Output: Once 
#you've finished writing this script, save the file by pressing Ctrl-o, 
#the Enter key, and Ctrl-x. f901317810dd5da1.png

#Here, as we see the output, it function returns true even if the 
username doesnot start with an letter. Here we need to change the check 
of the first character as only letters are allowed in the first 
character of the username. Now, run the validations.py on the python3 
interpreter. Continue by opening validations.py in the nano editor using 
the following command:

nano validations.py if type(username) != str: python3 validations.py 
raise TypeError("username must be a string") Output: if minlen < 1:
        raise ValueError("minlen must be at least 1") 
f901317810dd5da1.png
    # Usernames can't be shorter than minlen
Here, as we see the output, it function returns true even if the 
username doesnot start with an letter. Here we need to change the check 
of the first character as only letters are allowed in the first 
character of the username.  if len(username) < minlen:
        return False
Continue by opening validations.py in the nano editor using the following command:

nano validations.py
There are lots of ways to fix the code; ultimately, you'll want to add additional conditional checks to validate the first character doesn't start with either of the forbidden characters. You can choose whichever way you'd like to implement this.

Once you've finished writing this script, save the file by pressing 
Ctrl-o, the Enter key, and Ctrl-x.  # Usernames can only use letters, 
numbers, dots and underscores
    if not re.match('^[a-z0-9._]*$', username): Now, run the 
validations.py.  return True
    # Usernames can't begin with a number
python3 validations.py    if username[0].isnumeric():
        return False
    return False
print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False


