def show_balance():
    print(f"Your Balance is ${balance:.2f}")

def deposit():
    amount = float(input("Please Enter the amount that you would like to deposit: "))

    if amount < 0:
        print("That is not a Valid amount!")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("Please Enter the amount that you would like to withdraw: "))

    if amount > balance:
        print("You dont have enough Balance to withdraw! Please make a deposit first.")
        return 0
    elif amount <= 0:
        print("Amount must be greater than zero!")
        return 0
    else:
        return amount

balance = 0
is_running = True

while is_running:
    print("Nexa Online Banking program")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = input("Enter your choice (1-4) : ")

    if choice == "1":
        show_balance()
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdraw()
    elif choice == "4":
        is_running = False
        print("Thank you! Have nice day!")
    else:
        print("Please Enter a Valid Number from (1-4)")

print("Thank you! Have a nice day!")