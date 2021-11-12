
#!/usr/bin/env python3

import re

def validate_user(username, minlen):
	if type(username)!=str:
		raise TypeError("username must be a string")
	if minlen<1:
		raise ValueError("minlen must be at least 1")
	if len(username)<minlen:
		return False
	elif not re.match('^[a-z0-9._]*$', username):
		return False
	elif username[0].isnumeric() or username[0]=='.' or username[0]=='_':
		return False
	else:
		return True

print(validate_user("blue.kale",3)) # True
print(validate_user(".blue.kale",3)) #currently true should be false
print(validate_user("re_quiona", 4)) #true
print(validate_user("_red_quiona", 4)) #currntly true, should be false
