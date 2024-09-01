import random

print("Welcome to the Number Guessing Game! \n"
      "I'm thinking of a number between 1 and 100. \n"
      "You have 5 chances to guess the correct number. \n"
      "")

def set_difficulty ():
    print("Please select the difficulty level: ")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    while True:
        choice = input("Please Enter Your Choice: ")
        if choice == "1":
            print("Great! You have selected the Easy difficulty level.")
            return 10
        elif choice == "2":
            print("Great! You have selected the Medium difficulty level.")
            return 5
        elif choice == "3":
            print("Great! You have selected the Hard difficulty level.")
            return 3
        else:
            print("Invalid Choice. Please Enter 1, 2, 3.")


