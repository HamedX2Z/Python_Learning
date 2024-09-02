print("Welcome to my Weight Conversion Program!")

# kilogram to pound function
def kilo_to_pound():
    num1 = float(input("Please Enter the First Number: "))
    pound = 2.205
    result = num1 * pound
    print(result)

# pound to kilogram function
def pound_to_kilo():
    num1 = float(input("Please Enter the Second Number: "))
    kilo = 2.205
    result = num1 / kilo
    print(result)