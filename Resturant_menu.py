menu = {"pizza": 3.00,
        "nachos":4.50,
        "popcorn":6.00,
        "fires": 2.50,
        "chips": 1.00,
        "soda": 3.00}

cart = []
total = 0

print("----------Menu----------")

for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

print("------------------------")

while True:
    food = input("What food would you like to buy? (Q to quit): ").lower()
    if food == "q":
        print("Goodbye for now!")
        break
    elif menu.get(food) is not None:
        cart.append(food)
    elif menu.get(food) is None:
        print("Please select an item from the menu!")