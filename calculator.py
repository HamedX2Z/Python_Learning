print("Welcome to my calculator!\n")

# addition function
def addition():
    num1 = float(input("Please Enter the first Number: "))
    num2 = float(input("Please Enter the second Number: "))
    print(num1 + num2)

# subtraction function
def subtraction():
    num1 = float(input("Please Enter the first Number: "))
    num2 = float(input("Please Enter the second Number: "))
    print(num1 - num2)

# multiplication function
def multiplication():
    num1 = float(input("Please Enter the first Number: "))
    num2 = float(input("Please Enter the second Number: "))
    print(num1 * num2)

# division function
def division():
    num1 = float(input("Please Enter the first Number: "))
    num2 = float(input("Please Enter the second Number: "))
    print(num1 / num2)

# main function to run the calculator
def main():
    while True:
        print("Select the operation that you want to perform\n")
        print("1. Addition")
        print("2. Subtraction")
        print("3. multiplication")
        print("4. division\n")

        try:
            user_choice = int(input("Please Enter you're choice: "))

            # Check if the choice is within the valid range
            if user_choice == 1:
                print("Great! You have selected Addition\n")
                addition()
            elif user_choice == 2:
                print("Great! You have selected Subtraction\n")
                subtraction()
            elif user_choice == 3:
                print("Great You have selected multiplication\n")
                multiplication()
            elif user_choice == 4:
                print("Great You have selected division\n")
                division()
            else:
                print("Invalid Choice! Please Enter a Number from 1-4\n")
        except ValueError:
            # Handle non-integer input
            print("Invalid input! Please enter a whole number from 1-4.\n")

# Runs the main function
main()