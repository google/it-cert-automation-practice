# Google IT Automation with Python Professional Certificate - Practice files

This repository contains the practice files used throughout the courses that are
part of the Google IT Automation with Python Professional Certificate

There's a separate folder for each course.

Added a fix for validate_user in `Course3/Lab4` by improving regex check. The regex now checks for the first char to be a letter in `[a-z]`. The remaining regex was same as the original.
Examples:
`.blue.kale` is not a valid user as it starts with `.` which is not in `[a-z]`.
`_red_quinoa` is not a valid user as it starts with `_` (underscore) which is not in `[a-z]`.
