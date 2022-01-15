Git Lab exercise Reference:
==========================
  Fork another repository
  Commit changes to your own fork and create pull requests to the upstream repository
  Gain familiarity with code reviews, and ensure that your fix runs fine on your system before creating the pull request
  Describe your pull request
  
Exercise
========
  Problem statement captured in Bug/Issue opened #18521 - Username not validated for non-alphabetical first letter.
  Fix validate_user method in validations.py
  
################ Fork google/it-cert-automation-practice on github to your git account ##########################

############## Clone a copy of the same to local repository ############################

student@linux-instance:~$ git clone https://github.com/skscodes/it-cert-automation-practice.git
Cloning into 'it-cert-automation-practice'...
remote: Enumerating objects: 55, done.
remote: Total 55 (delta 0), reused 0 (delta 0), pack-reused 55
Unpacking objects: 100% (55/55), done.
student@linux-instance:~$ cd ~/it-cert-automation-practice

student@linux-instance:~/it-cert-automation-practice$ git remote -v
origin  https://github.com/skscodes/it-cert-automation-practice.git (fetch)
origin  https://github.com/skscodes/it-cert-automation-practice.git (push)


########### Add files to upstream ####################


student@linux-instance:~/it-cert-automation-practice$ git remote add upstream https://github.com/skscodes/it-cert-automation-practice.git
student@linux-instance:~/it-cert-automation-practice$ git remote -v
origin  https://github.com/skscodes/it-cert-automation-practice.git (fetch)
origin  https://github.com/skscodes/it-cert-automation-practice.git (push)
upstream        https://github.com/skscodes/it-cert-automation-practice.git (fetch)
upstream        https://github.com/skscodes/it-cert-automation-practice.git (push)

student@linux-instance:~/it-cert-automation-practice$ git config --global user.name "skscodes"
student@linux-instance:~/it-cert-automation-practice$ git config --global user.email "<User email>"

########### Create new branch ##################

  
student@linux-instance:~/it-cert-automation-practice$ git branch improve-username-behavior
student@linux-instance:~/it-cert-automation-practice$ git checkout improve-username-behavior
Switched to branch 'improve-username-behavior'
student@linux-instance:~/it-cert-automation-practice$ cd ~/it-cert-automation-practice/Course3/Lab4
student@linux-instance:~/it-cert-automation-practice/Course3/Lab4$ ls
validations.py

student@linux-instance:~/it-cert-automation-practice/Course3/Lab4$ cat validations.py
#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-z0-9._]*$', username):
        return False
    # Usernames can't begin with a number
    if username[0].isnumeric():
        return False
    return True



student@linux-instance:~/it-cert-automation-practice/Course3/Lab4$ nano validations.py
student@linux-instance:~/it-cert-automation-practice/Course3/Lab4$ cat validations.py
#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-z0-9._]*$', username):
        return False
    # Usernames can't begin with a number
    if username[0].isnumeric():
        return False
    return True

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False


###### BUG #18521 ####################
student@linux-instance:~/it-cert-automation-practice/Course3/Lab4$ python3 validations.py
True
True
True
True

############ Fix File and test changes ###############

student@linux-instance:~/it-cert-automation-practice/Course3/Lab4$ nano validations.py
student@linux-instance:~/it-cert-automation-practice/Course3/Lab4$ python3 validations.py
True
False
True
False

student@linux-instance:~/it-cert-automation-practice/Course3/Lab4$ cat validations.py
$
#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can only start with letters and use letters, numbers, dots and underscores
    if not re.match('^[a-z][a-z0-9._]*$', username):
        return False
    # Usernames can't begin with a number
    if username[0].isnumeric():
        return False
    return True

# Test use cases for username
print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # False



student@linux-instance:~/it-cert-automation-practice/Course3/Lab4$ git status
On branch improve-username-behavior
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   validations.py

no changes added to commit (use "git add" and/or "git commit -a")
student@linux-instance:~/it-cert-automation-practice/Course3/Lab4$ git add validations.py
student@linux-instance:~/it-cert-automation-practice/Course3/Lab4$ git status
On branch improve-username-behavior
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   validations.py

student@linux-instance:~/it-cert-automation-practice/Course3/Lab4$ git commit
[improve-username-behavior 0008e50] Closes: #1 Updated validations.py python script. Fixed the behavior of validate_user function in validations.py.
 1 file changed, 9 insertions(+), 2 deletions(-)

student@linux-instance:~/it-cert-automation-practice/Course3/Lab4$ git push origin improve-username-behavior
Username for 'https://github.com': skscodes
Password for 'https://skscodes@github.com':
Counting objects: 5, done.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (5/5), 594 bytes | 0 bytes/s, done.
Total 5 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote:
remote: Create a pull request for 'improve-username-behavior' on GitHub by visiting:
remote:      https://github.com/skscodes/it-cert-automation-practice/pull/new/improve-username-behavior
remote:
To https://github.com/skscodes/it-cert-automation-practice.git
 * [new branch]      improve-username-behavior -> improve-username-behavior

################################################
Create New Pull request on Github to push these changes to google/it-cert-automation-practice Master repository 
from which we forked these changes.
