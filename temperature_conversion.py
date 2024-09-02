print("Welcome to my temperature converter program!\n")

# function to convert celsius to fahrenheit
def celsius_to_fahrenheit():
    try:
        user_input = float(input("Please Enter the temperature in Celsius: "))
        fahrenheit = (user_input * 1.8) + 32
        print(f"{user_input} degrees celsius is equal to {fahrenheit} degrees fahrenheit.\n")
    except ValueError:
        print("Invalid Input Please Enter a Number!\n")

# function to convert fahrenheit to celsius
def fahrenheit_to_celsius():
    try:
        user_input = float(input("Please Enter the temperature in Fahrenheit: "))
        celsius = (user_input - 32) / 1.8
        print(f"{user_input} degrees fahrenheit is equal to {celsius} degrees celsius.\n")
    except ValueError:
        print("Invalid Input Please Enter a Number!\n")

# function to exit the program
def exit_program():
    print("Exiting the program. Goodbye!")
    exit()

# main function to
def main():
    while True:
        print("Select the operation that you want to perform\n")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit\n")
        try:
            user_choice = int(input("Please Enter you're choice: "))
            if user_choice == 1:
                celsius_to_fahrenheit()
            elif user_choice == 2:
                fahrenheit_to_celsius()
            elif user_choice == 3:
                exit_program()
        except ValueError:
            print("Invalid input! Please enter a whole number from 1-3.\n")

main()