#!/usr/bin/env python3

import re

regex = re.compile(r'^[a-z0-9._]*$') 

def validate_user(username, minlen):
  """Check if username meets our requirements"""
  if type(username) != str:
      raise TypeError("username must be a string")

  if minlen < 1:
      raise ValueError("minlen must be at least 1")
  
  # Usernames can't start with underscore
  if username.startswith('.') or username.startswith('_'):
      return False

  # Usernames can't be shorter than minlen  
  if len(username) < minlen:
      return False
      
  # Usernames can only use letters, numbers, dots and underscores
  if not regex.match(username):
      return False  

  # Usernames can't begin with a number
  if username[0].isnumeric():
      return False

  return True
print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False


