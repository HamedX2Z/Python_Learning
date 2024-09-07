# Printing the initial welcome message for the Quiz Game
print("Welcome to the Quiz Game!")

# Defining a tuple containing all the quiz questions
questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in solar system is the hottest?: ")

# Defining a tuple of tuples containing multiple-choice options for each question
options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

# Defining a tuple with the correct answers for each question
answers = ("C", "D", "A", "A", "B")

# Initializing an empty list to store the user's guesses
guesses = []

# Initializing a variable to keep track of the user's score
score = 0

# Initializing a variable to keep track of the current question number
question_num = 0

# Iterating through each question in the questions tuple
for question in questions:
    # Printing a separator for clarity
    print("----------------------")
    # Printing the question
    print(question)
    # Printing each option for the current question
    for option in options[question_num]:
        print(option)

    # Collecting the user's guess and converting it to uppercase
    guess = input("Enter your guess (A, B, C or D): ").upper()
    # Adding the guess to the list of guesses
    guesses.append(guess)
    # Checking if the guess matches the correct answer and updating the score if it does
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        # Displaying the correct answer if the guess was wrong
        print("The correct answer was", answers[question_num])
    # Moving on to the next question
    question_num += 1

# Printing a separator for the result section
print("----------------------")
print("--------RESULT--------")
print("----------------------")

# Printing the correct answers
print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

# Printing the user's guesses
print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

# Calculating the user's score as a percentage
score = int(score / len(questions) * 100)
# Printing the user's final score
print(f"Score: {score}%")