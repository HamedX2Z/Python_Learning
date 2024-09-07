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
