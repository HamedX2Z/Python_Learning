# Print a welcome message to the admin page of the shopping store
print("Welcome to the Shopping Store Admin page!")

# Initialize empty lists to store food items and their prices, and a variable to keep track of the total cost
foods = []
prices = []
total = 0

# Start an infinite loop to continuously prompt the user for input
while True:
    # Ask the user to enter a food item, or press 'Q' to quit
    food = input("Enter a food to buy (press Q to quit): ")
    # Check if the user wants to quit
    if food.lower() == "q":
        print("\nGoodbye for now!")
        break
    else:
        # Start another loop to prompt for the price of the entered food
        while True:
            try:
                # Ask the user to enter the price of the food and convert it to a float
                price = float(input(f"Enter the price of a {food}: $"))
                # Append the food item and its price to their respective lists
                foods.append(food)
                prices.append(price)
            except ValueError:
                # Handle invalid input for the price
                print("Invalid Input! Please enter a valid number.")
            else:
                # Break the loop if the price input is valid
                break

# Print the contents of the cart
print("\n-----YOUR CART-----")
for food in foods:
    print(food)

# Calculate and print the total cost of the food items
for price in prices:
    total += price

# Print the total cost
print("-----YOUR TOTAL-----")
print(f"Your total is ${total}.")
