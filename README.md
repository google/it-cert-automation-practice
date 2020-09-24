# Google IT Automation with Python Professional Certificate - Practice files

This repository contains the practice files used throughout the courses that are
part of the Google IT Automation with Python Professional Certificate

There's a separate folder for each course.

Course4 Lab4
======
validations.py
Returns true if the minimum length of the username is met, and if the username doesn not start with a non alpha character, for all else will return False

##Examples

validate_user("blue.kale", 3) # True
validate_user(".blue.kale", 3) # False
validate_user("red_quinoa", 4) # True
validate_user("_red_quinoa", 4) # False
validate_user("3name.user, 4) # False
