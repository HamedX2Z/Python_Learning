print("Welcome to Credit Card Encryption Program")

while True:
    # Asks user for a Credit Number to Encrypt
    CreditCard_Number = input("\nEnter Your Credit Card Number: ")

    # if statement to check if user input contains any invalid data
    if CreditCard_Number.replace(" ", "").isalpha():
        print("Credit Card Number cant contain any letters or spaces!")
    elif len(CreditCard_Number) < 12 or len(CreditCard_Number) > 12:
        print("Credit Card Number must be at 12 digits long!")
    else:
        print(f"Here's Your Encrypted Credit Card Number: XXXX-XXXX-XXXX-{CreditCard_Number[-4:]}")
        break