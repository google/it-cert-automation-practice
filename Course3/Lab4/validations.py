def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if not isinstance(username, str):
        return "Error: Username must be a string."
    if minlen < 1:
        return "Error: Minimum length must be at least 1."

    # Ensure case insensitivity by transforming username to lowercase
    username = username.lower()

    # Check the minimum length of the username
    if len(username) < minlen:
        return f"Error: Username must be at least {minlen} characters long."

    # Check for invalid characters
    for char in username:
        if not (char.isalnum() or char in "._"):
            return "Error: Username can only contain letters, numbers, dots, and underscores."

    # Ensure the username does not begin with a number
    if username[0].isdigit():
        return "Error: Username cannot begin with a number."

    # Disallow reserved words
    reserved_words = {"admin", "root", "user", "test"}
    if username in reserved_words:
        return f"Error: Username cannot be a reserved word (e.g., {', '.join(reserved_words)})."

    # Ensure no consecutive dots
    if ".." in username:
        return "Error: Username cannot contain consecutive dots."

    # If all checks pass, return True
    return True