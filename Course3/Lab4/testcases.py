#importing validate_user function from validate.py
from validations import validate_user 

# Here are 4 testcases

# testcase1
def testcase1():
    # True
    testcase = validate_user("blue.kale", 3)
    return testcase
    
# testcase2
def testcase2():
    # Currently True, should be False
    testcase = validate_user(".blue.kale", 3)
    return testcase
    
# testcase3
def testcase3():
    # True
    testcase = validate_user("red_quinoa", 4)
    return testcase
    
# testcase4
def testcase4():
    # Currently True, should be False
    testcase = validate_user("_red_quinoa", 4)
    return testcase

# this will print all the above testcases
def testcases():
    print(testcase1())
    print(testcase2())
    print(testcase3())
    print(testcase4())
if __name__ == "__main__":
    testcases()
