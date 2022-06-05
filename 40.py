# #python quiz game

# -------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 0

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print('\n')

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print('\n')

    score = (correct_guesses/len(questions))*100
    print("Your score is: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------


questions = {
 "What is the largest mammal in the world?: ": "A",
 "How many colors are in a rainbow?: ": "B",
 "Which country is home to the kangaroo?: ": "C",
 "Which animal is the tallest in the world?: ": "A"
}

options = [["A. Whale", "B. Ant", "C. Snake", "D. Dog"],
          ["A. Six", "B. Seven", "C. Five", "D. Two"],
          ["A. England", "B. Lao", "C. Australia", "D. Thailand"],
          ["A. Giraffe","B. Tiger", "C. Duck", "D. Frogs"]]

new_game()

while play_again():
    new_game()