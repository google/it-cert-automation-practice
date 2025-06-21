
def validate_user(username, minlen):

    if type(username) != str:

        return False

    if len(username) < minlen:

        return False

    if not username[0].isalpha():  # Kiểm tra ký tự đầu tiên phải là chữ cái

        return False

    return True



# Test cases

print(validate_user("blue.kale", 3))      # True

print(validate_user(".blue.kale", 3))     # False

print(validate_user("red_quinoa", 4))     # True

print(validate_user("_red_quinoa", 4))    # False


