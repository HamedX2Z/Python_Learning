# Print a welcome message to the admin page of the shopping store
print("Welcome to the Shopping Store Admin page!")

# Initialize empty lists to store food items, their prices, and quantities
foods = []
prices = []
quantities = []
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
                # Break the loop if the inputs are valid
                break

# Print the contents of the cart
print("\n-----YOUR CART-----")
for food, quantity in zip(foods, quantities):
    print(f"{quantity} x {food}")

# Calculate and print the total cost of the food items
for price, quantity in zip(prices, quantities):
    total += price * quantity

# Print the total cost
print("\n-----YOUR TOTAL-----")
print(f"Your total is ${total:.2f}.")