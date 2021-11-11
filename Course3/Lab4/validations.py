#!/usr/bin/env python3

import re

def validate_user(username, minlen):
	if type(username) != str:
		raise TypeError("username must be string")
	if minlen < 1:
		raise TypeError("minlen must be at least 1")
	if len(username) < minlen:
		return False
	if username[0].isnumeric():
		return False
	if not re.match('^[a-z0-9._]*$', username):
		return False
	if not username[0].isalpha():
		return False
	return True
 


print(validate_user("blue.kale", 3))
print(validate_user(".blue.kale", 3))
print(validate_user("red_quinoa", 4))
print(validate_user("_red_quinoa", 4))
