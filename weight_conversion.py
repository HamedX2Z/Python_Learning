from struct import pack_into

print("Welcome to my Weight Conversion Program!")

# kilogram to pound function
def kilo_to_pound():
    try:
        # Prompt the user for input and attempt to convert it to a float
        user_input = float(input("Please Enter the Weight in Kilograms: "))
        pound = 2.205
        result = user_input * pound
        print(f"{user_input} kilograms is equal to {result:.2f} pounds.\n")

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
        print(f"{user_input} kilograms is equal to {result:.2f} pounds.\n")

    except ValueError:
        # If input is not a valid number, print an error message
        print("Error: Please enter a valid number for the weight in pounds.")

#function to exit the game
def exit_game():
    print("Exiting the program. Goodbye!")
    exit()

# main function to run the program
def main():
    while True:
        print("Select the operation that you want to perform\n")
        print("1. Kilogram to Pound")
        print("2. Pound to Kilogram")
        print("3. Exit\n")
        try:
            user_choice = int(input("Please Enter you're choice: "))
            if user_choice == 1:
                kilo_to_pound()
            elif user_choice == 2:
                pound_to_kilo()
            elif user_choice == 3:
                exit_game()
            else:
                print("Invalid Choice! Please Enter a Number from 1-2\n")
        except ValueError:
            print("Invalid input! Please enter a whole number from 1-2.\n")
main()