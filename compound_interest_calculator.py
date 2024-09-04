print("Welcome to Compound Interest Calculator\n")

# function to get the user investment amount
def investment():
    while True:
        # try block to check for possible invalid inputs
        try:
            investment_amount = float(input("Please Enter the Amount of Investment: "))
            if investment_amount <= 0:
                print("Investment cant be euqal or less than zero!")
            else:
                print(f"Set! Investment Amount is {investment_amount}$")
                # returning the investment amount value so it can be used in other parts of the code
                return investment_amount
        except ValueError:
            print("Invalid input! Please Enter a Number!\n")