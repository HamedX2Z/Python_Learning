print("Welcome to the Sign up page!\n")

def is_strong_password():

    # Initialize criteria flags
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*()-+"

    # Check length of the password
    if len(password) < 8:
        print("Error: Password must be at least 8 characters long.")
        return False

    # Loop through each character in the password to check criteria
    for char in password:
        if char.isdigit():
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

# Main part of the program: get username and password from the user
while True:
    username = input("Please Enter a username: ")

    # Checks if the username is more than the valid length or has invalid character
    if " " in username:
        print("Your username cannot contain a space!.\n")
    elif len(username) > 12 or len(username) < 4:
        print("Your username must be less than 12 characters long and\n"
              "more than 4 characters long.\n")
    elif username == "":
        print("Your username cannot be empty!\n")
    else:
        print("Username is saved successfully!\n")
        break

# Loop until a strong password is provided
while True:
    password = input("Please Enter a password: ")
    if is_strong_password():
        print("Registration Successful!")
        break
    else:
        print("Please try again with a strong password.\n")