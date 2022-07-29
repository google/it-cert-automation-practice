#!/usr/bin/env python3

import unittest

from validations import validate_user

class TestValidations(unittest.TestCase):

	def test_valid(self):
		valid_params = [('tututka',3), 
				('TutUtka',2),
				]

		for param_val in valid_params:
			self.assertEqual(validate_user(param_val[0], param_val[1]), True)

	def test_invalid(self):
		invalid_params = [('_tututka',3),
				  ('tutu', 5),
				  ('1tut', 2),
				  ('.tututka',4),
				  ('_tututka',1),
				]
		for param_val in invalid_params:
			self.assertEqual(validate_user(param_val[0], param_val[1]), False)
		

if __name__ == '__main__':
	unittest.main()
