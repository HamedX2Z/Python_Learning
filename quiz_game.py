from string import whitespace

print("Hello!! Welcome to my quiz game!")

Score = 0
successful_answer = "Your Answer has been Recorded!"
unSuccessful_answer = "You Answer hasn't been Recorded Please Check your Answer Again!"

question_1_answers = ["1- North America", "2- EU", "3- Middle East", "4- Africa"]

while True:
    question_1 = input("Which region is iran locted in?\n" + ", ".join(question_1_answers) + "\nAnswer = ")

    if question_1 == "Middle East":
        print(successful_answer)
        Score += 1
        print(f"This you're current score: {Score}")
        break
    else:
        print(unSuccessful_answer)


question_2_answers = ["1- Rasht", "2- Tehran", "3- Abadan", "4- Esfehan"]

while True:
    question_2 = input("Whats iran captial city?\n" + ", ".join(question_2_answers) + "\nAnswer = ")

    if question_2 == "Tehran":
        print(successful_answer)
        Score += 1
        print(f"This you're current score: {Score}")
        break
    else:
        print(unSuccessful_answer)


question_3_answers = ["1- 80", "2- 100", "3- 92", "4- 95"]

while True:
    question_3 = input("How much is Iran population? (in Million)\n" + ", ".join(question_3_answers) + "\nAnswer = ")

    if question_3 == "92":
        print(successful_answer)
        Score =+ 1
        print(f"This you're current score: {Score}")
        break
    else:
        print(unSuccessful_answer)