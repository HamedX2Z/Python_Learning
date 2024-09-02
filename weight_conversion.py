print("Welcome to my Weight Conversion Program!")

# kilogram to pound function
def kilo_to_pound():
    try:
        # Prompt the user for input and attempt to convert it to a float
        user_input = float(input("Please Enter the Weight in Kilograms: "))
        pound = 2.205
        result = user_input * pound
        print(f"{user_input} kilograms is equal to {result:.2f} pounds.")

    except ValueError:
        # If input is not a valid number, print an error message
        print("Error: Please enter a valid number for the weight in kilograms.")

# pound to kilogram function
def pound_to_kilo():
    try:
        # prompt the user for input and then converts it into float
        user_input = float(input("Please Enter the Second Number: "))
        kilo = 2.205
        result = user_input / kilo
        print(f"{user_input} kilograms is equal to {result:.2f} pounds.")

    except ValueError:
        # If input is not a valid number, print an error message
        print("Error: Please enter a valid number for the weight in pounds.")
