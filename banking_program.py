def set_password():
    #function to set an password for account at the start
    while True:
        password = input("Please Enter a 4 digit Password: ")
        if len(password) == 4 and password.isdigit():
            print("password successfully set!")
            return password
        else:
            print("The password must be 4 digits long and contain only numbers!")

def verify_password(password):
    # Function to verify the user's password
    attempts = 3
    while attempts > 0:
        entered_password = input("Please Enter your password: ")
        if entered_password == password:
            return True
        else:
            attempts -= 1
            print(f"Incorrect password! You have {attempts} attempt(s) left.")

    # If out of attempts, deny access
    print("Too many incorrect attempts. Access denied.")
    return False

def show_balance(balance):
    print(f"Your Balance is ${balance:.2f}")

def deposit():
    amount = float(input("Please Enter the amount that you would like to deposit: "))

    if amount < 0:
        print("That is not a Valid amount!")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Please Enter the amount that you would like to withdraw: "))

    if amount > balance:
        print("You dont have enough Balance to withdraw! Please make a deposit first.")
        return 0
    elif amount <= 0:
        print("Amount must be greater than zero!")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    # Set the password at the start
    password = set_password()

    while is_running:
        print("\nNexa Online Banking program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("Enter your choice (1-4) : ")

        # Verify password before each action
        if choice in ["1", "2", "3"] and not verify_password(password):
            continue

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
            print("Thank you! Have a nice day!")
        else:
            print("Please Enter a Valid Number from (1-4)")

if __name__ == "__main__":
    main()