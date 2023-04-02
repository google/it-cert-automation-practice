# Validate username

This purpose of this script is to validtae users name to make sure the ony begin with alpherbetic  
characters(either lower or upper case), contains only dot(.) or uderscore (_) special charater or numbers  
This basically contains one function `validate_user`

## Function
validate_user:
> This function takes two arguments `username` and `minlen`. The purpose of the function is to check if the received  
> username matches certain conditions, and return True if it does, or False otherwise. The conditions that the function  
> checks for are as follow
> 1. The `username` must be a string. If it is not, the function raises a `TypeError`.
> 2. The `minlen` argument make sure that the length of the `username` must be at least 1. If it is not, the function raises a `ValueError`.
> 3. The length of the `username` must be at least `minlen`.
> 4. The `username` can only use letters (both uppercase and lowercase), numbers, dots and underscores. It cannot use any other special characters.
> 5. The `username` cannot begin with a number. 
> To check for conditions 3-5, the function uses a regular expression pattern match with the `re` module.  
> The pattern used is `^[A-Za-z][a-z0-9._]*$`, which matches a string that starts with a letter (both uppercase and lowercase),  
> followed by zero or more occurrences of letters (both uppercase and lowercase), digits, dots, and underscores.



