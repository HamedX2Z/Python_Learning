print("Welcome to Compound Interest Calculator\n")

# function to get the user investment amount
def investment():
    while True:
        # try block to check for possible invalid inputs
        try:
            investment_amount = float(input("Please Enter the Amount of Investment: "))
            if investment_amount <= 0:
                print("Investment cant be euqal or less than zero!\n")
            else:
                print(f"Set! Investment Amount is {investment_amount}$\n")
                # returning the investment amount value so it can be used in other parts of the code
                return investment_amount
        except ValueError:
            print("Invalid input! Please Enter a Number!\n")

# Get the user's investment amount
user_investment_amount = investment()

# function to get the users interest rate
def rate():
    while True:
        # try block to check for possible invalid inputs
        try:
            user_interest = int(input("Please Enter the Interest Rate: "))
            if user_interest <= 0:
                print("Interest Rate cant be euqal or less than zero!\n")
            else:
                print(f"Set! Interest Rate is {user_interest}%\n")
                # returning the user interest rate value so it can be used in other parts of the code
                return user_interest
        except ValueError:
            print("Invalid input! Please Enter a Number!\n")

# Get the user's interest rate
user_interest_rate = rate()