# Print a welcome message to the admin page of the shopping store
print("Welcome to the Shopping Store Admin page!")

# Initialize empty lists to store food items, their prices, and quantities
foods = []
prices = []
quantities = []
total = 0


def print_cart():
    # Print the contents of the cart
    print("\n-----YOUR CART-----")
    if not foods:
        print("Your cart is empty.")
    else:
        for i, (food, quantity) in enumerate(zip(foods, quantities)):
            print(f"{i + 1}. {quantity} x {food}")


def calculate_total():
    # Calculate the total cost of the food items
    total = sum(price * quantity for price, quantity in zip(prices, quantities))
    print("\n-----YOUR TOTAL-----")
    print(f"Your total is ${total:.2f}.")


# Start an infinite loop to continuously prompt the user for input
while True:
    # Provide options to the user
    print("\nOptions: [1] Add Item [2] Remove Item [Q] Quit")
    choice = input("Choose an option: ").lower()

    if choice == 'q':
        print("\nGoodbye for now!")
        break
    elif choice == '1':
        # Add an item to the cart
        food = input("Enter a food to buy: ")
        while True:
            try:
                # Ask the user to enter the price of the food and convert it to a float
                price = float(input(f"Enter the price of a {food}: $"))
                # Ask the user to enter the quantity of the food and convert it to an integer
                quantity = int(input(f"Enter the quantity of {food}: "))
                if quantity < 1:
                    print("Quantity must be at least 1. Please enter a valid number.")
                    continue
                # Append the food item, its price, and quantity to their respective lists
                foods.append(food)
                prices.append(price)
                quantities.append(quantity)
            except ValueError:
                # Handle invalid input for the price or quantity
                print("Invalid Input! Please enter valid numbers for price and quantity.")
            else:
                # Print updated cart and break the loop if the inputs are valid
                print_cart()
                break
    elif choice == '2':
        # Remove an item from the cart
        if not foods:
            print("Your cart is empty.")
            continue

        print_cart()
        while True:
            try:
                # Ask the user to enter the item number to remove
                item_num = int(input("Enter the item number to remove: "))
                if 1 <= item_num <= len(foods):
                    # Remove the item from the lists
                    index = item_num - 1
                    food_removed = foods.pop(index)
                    prices.pop(index)
                    quantities.pop(index)
                    print(f"{food_removed} has been removed from your cart.")
                    print_cart()
                    break
                else:
                    print("Invalid item number. Please enter a number from the list.")
            except ValueError:
                print("Invalid Input! Please enter a valid number.")
    else:
        print("Invalid choice, please try again.")

# Calculate and print the final total cost of the food items
calculate_total()