print("Welcome to Compound Interest Calculator\n")

while True:
    try:
        investment = float(input("Please Enter the Amount of Investment: "))
        if investment <= 0:
            print("Investment cant be euqal or less than zero!")
        else:
            print(f"Set! Investment Amount is {investment}$")
            break
    except ValueError:
        print("Invalid input! Please Enter a Number!\n")
