#!/usr/bin/env python3

import re

def validate_user(username,minlen):
	if type(username)!=str:
		raise TypeError("username must be a string")
	if minlen<1:
		raise ValueError("minlen must be at least 1")
	if len(username)<minlen:
		return False
	if re.match('^[a-z0-9._]*$',username):
		#print("match")
		#print(re.match('^[a-z0-9]*$',username))
		if username[0].isnumeric():
			return False
		elif re.match('^[._]',username):
#			print(re.match('^[._]',username))
			return False
		else: 
			return True
	else:
		return False




print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False
