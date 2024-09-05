print("Welcome to the Shopping Store!")

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (press Q to quit): ")
    user_input = food.lower()
    if user_input == "q":
        print("\nGoodbye for now!")
        break