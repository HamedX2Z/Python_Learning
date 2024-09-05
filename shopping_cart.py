print("Welcome to the Shopping Store!")

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (press Q to quit): ")
    if food.lower() == "q":
        print("\nGoodbye for now!")
        break