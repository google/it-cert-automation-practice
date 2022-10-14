validations.py file contains validate_user(username, minlen)

How it works by calling the function with two parameters user name and minimum length accepted for a valid user name

- Valid user name length must be more than the minlen provided.
- User name must be string and the first letter must not start with special characters like dot or underscore.
- Minlen must be greater than zero.

examples:
validate_user("blue.kale", 3) # True
validate_user(".blue.kale", 3) # False
validate_user("red_quinoa", 4) # True
validate_user("_red_quinoa", 4) # False
