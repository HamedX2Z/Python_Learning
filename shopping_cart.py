print("Welcome to the Shopping Store!")

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (press Q to quit): ")
    if food.lower() == "q":
        print("\nGoodbye for now!")
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
