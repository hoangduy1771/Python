# dictionary
questions = {
    "Is the Earth round?": "B",
    "What is the currency of Vietnam?": "C",
    "What in the animal kingdom is a doe?": "A",
    "How many players are in a football team?": "D"
}

options = [["A. False", "B. True", "C. Sometimes", "D. Earth is flat"],
           ["A. Franc", "B. Pound", "C. Dong", "D. Yen"],
           ["A. a female deer", "B. a female cow", "C. an female alligator", "D. female sparrow"],
           ["A. 10", "B. 13", "C. 12", "D. 11"]]


def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for question in questions:
        print("===========================================")
        print(question)
        for option in options[question_num - 1]:
            print(option)
        guess = input("Enter (A, B, C or D): ").upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(question), guess)
        question_num += 1
    display_score(correct_guesses, guesses)
    play_again()


def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


def display_score(correct_guesses, guesses):
    print("===========================================")
    print("Correct Answers : ", end=" ")
    for answer in questions:
        print(questions.get(answer), end=" ")
    print()
    print("Your guesses: ", end=" ")
    for guess in guesses:
        print(guess, end=" ")
    print()
    score = int((correct_guesses / len(questions)) * 100)
    print("Your score: " + str(score) + " %")
    print("===========================================")


def play_again():
    if input("Do you want to play a new game? Type Y to play again: ").upper() == "Y":
        new_game()


new_game()
print("Byeee!")

