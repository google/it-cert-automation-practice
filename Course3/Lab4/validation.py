print(validate_user("blue.kale", 3))#True
print(validate_user(".blue.kale", 3))#Currently True,should be False
print(validate_user("red_quinoa", 4))#True
print(validate_user("_red_quinoa", 4))#Currently True, should be False
