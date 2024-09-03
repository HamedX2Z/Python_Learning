print("Welcome to Credit Card Encryption Program")

while True:
    # Asks user for a Credit Number to Encrypt
    CreditCard_Number = input("\nEnter Your Credit Card Number: ")

    # Removes spaces and checks for invalid characters
    sanitized_number = CreditCard_Number.replace(" ", "")

    # if statement to check if the input contains only digits
    if not sanitized_number.isdigit():
        print("Credit Card Number Must only contain digits!")
    # Check if the sanitized number is exactly 12 digits long
    elif len(sanitized_number) != 12 :
        print("Credit Card Number must be 12 digits long!")
    else:
        # Format the output with only the last 4 digits visible
        print(f"Here's Your Encrypted Credit Card Number: XXXX-XXXX-XXXX-{sanitized_number[-4:]}")
        break