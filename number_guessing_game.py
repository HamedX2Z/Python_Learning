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

def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    #select difficulty level
    chances = set_difficulty()

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nLet's start the game!")

    while chances > 0:
        guess = input("\nEnter you guess: ")

        if not guess.isdigit():
            print("Invalid input. Please enter a valid number between 1 and 100.")
            continue

        guess = int(guess)
        attempts += 1

        if guess == secret_number:
            print(f"\nCongratulations! The secret number was {secret_number}!\nYou guessed the correct number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print(f"Incorrect! The number is greater than {guess}.")
        else:
            print(f"Incorrect! The number is less than {guess}.")

        chances -= 1
        print(f"You have {chances} chances left." if chances > 0 else f"\nSorry, you've run out of chances! The correct number was {secret_number}.")

if __name__ == "__main__":
    start_game()