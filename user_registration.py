def is_strong_password():

    # Initialize criteria flags
    has_upper = False
    has_lower = False
    has_digit = False
    has_number = False
    has_special = False
    special_characters = "!@#$%^&*()-+"

    # Check length of the password
    if len(password) < 8:
        print("Error: Password must be at least 8 characters long.")
        return False

    # Loop through each character in the password to check criteria
    for char in password:
        if char.isdigital():
            has_digit = True
        elif char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char in special_characters:
            has_special = True

    if not has_upper:
        print("Error: Password must contain at least one uppercase letter.")
    elif not has_lower:
        print("Error: Password must contain at least one lowercase letter.")
    elif not has_digit:
        print("Error: Password must contain at least one number.")
    elif not has_special:
        print("Error: Password must contain at least one special character.")

    #return True only if all criteria are met
    return has_upper and has_lower and has_digit and has_special