#!/usr/bin/env python3

import unittest
from validations import validate_user

class ValidationsTest(unittest.TestCase):
    def test_validate_user_with_empty_username_returns_false(self):
        #Test to verify that False is returned if username is an empty string
        testcase = ''
        expected = False
        self.assertEqual(validate_user(testcase, 2), expected)

    def test_validate_user_with_correct_username_type_string(self):
        #Test to verify that username is a correct string
        testcase = "blue"
        expected = True
        self.assertEqual(validate_user(testcase, 2), expected)

    def test_validate_user_with_incorrect_username_type_raises_typeerror(self):
        # Test an invalid username that is not a string
        testcase = 13113212
        expected = TypeError
        self.assertRaises(expected, validate_user, testcase, 2)

    def test_valid_username_with_dot_and_minlen_3(self):
        # Test a valid username with a dot and minlen = 3
        testcase = "blue.kale"
        expected = True
        self.assertTrue(validate_user(testcase, 3))

    def test_invalid_username_starts_with_dot_and_minlen_3(self):
        # Test an invalid username that starts with a dot and minlen = 3
        testcase = ".blue.kale"
        self.assertFalse(validate_user(testcase, 3))

    def test_valid_username_with_underscore_and_minlen_4(self):
        # Test a valid username with an underscore and minlen = 4
        testcase = "red_quinoa"
        self.assertTrue(validate_user(testcase, 4))

    def test_invalid_username_starts_with_underscore_and_minlen_4(self):
        # Test an invalid username that starts with an underscore and minlen = 4
        testcase = "_red_quinoa"
        self.assertFalse(validate_user(testcase, 4))

    def test_validate_user_with_non_alphanumeric_username(self):
        # Test that usernames containing non-alphanumeric characters return False
        testcase = " blue--- "
        self.assertFalse(validate_user(testcase, 4))

    def test_validate_user_with_username_shorter_than_minlen(self):
        testcase = "a"
        expected = False
        self.assertEqual(validate_user(testcase, 2), expected)

    def test_validate_user_with_username_longer_than_minlen(self):
        testcase = "abcdefg"
        expected = True
        self.assertEqual(validate_user(testcase, 2), expected)

    def test_validate_user_with_username_starting_with_number(self):
        testcase = "5_red_quinoa"
        expected = False
        self.assertEqual(validate_user(testcase, 4), expected)

    def test_validate_user_with_username_containing_only_non_alphanumeric_characters(self):
        testcase = ".-!?"
        expected = False
        self.assertEqual(validate_user(testcase, 1), expected)

    def test_validate_user_with_username_containing_only_alphanumeric_characters(self):
        testcase = "redquinoa123"
        expected = True
        self.assertEqual(validate_user(testcase, 4), expected)

if __name__ == '__main__':
    unittest.main()