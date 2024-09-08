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