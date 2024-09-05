print("Welcome to the Shopping Store Admin page!")

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

print("\n-----YOUR CART-----")
for food in foods:
    print(food)

for price in prices:
    total += price

print("-----YOUR TOTAL-----")
print(f"Your total is ${total}.")