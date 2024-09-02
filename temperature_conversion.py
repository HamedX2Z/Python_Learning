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