import random
from art import logo

# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

print(logo)

# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")

# correct_answer = random.randint(1, 100)
# print(f"Pssst, the correct answer is {correct_answer}")

# level = input("Choose a difficulty. Type 'easy' or 'hard':")

# user_guess = ""
# isCorrect = False


# if level == "easy":
#   print("You have 10 attempts remaining to guess the number.")
# elif level == "hard":
#   print("You have 5 attempts remaining to guess the number.")
# else:
#   print("Oops, wrong text (:")


# def check_guess():
#    if user_guess > correct_answer:
#      print("Oops, Too High, Guess again.")
#    elif user_guess < correct_answer:
#      print("Oops, Too low, Guess again.")
#    elif user_guess == correct_answer:
#      print(f"You got it, the correct answer is {correct_answer}")
#      global isCorrect
#      isCorrect = True

# check_guess()


# while  user_guess != correct_answer:
#     user_guess = int(input('Make a guess:'))


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

correct_answer = random.randint(1, 100)

print(correct_answer)
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if level == "easy":
    attempts = 10
elif level == "hard":
    attempts = 5
else:
    print("Oops, wrong text.")
    exit()

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    user_guess = int(input('Make a guess: '))

    if user_guess > correct_answer:
        print("Oops, Too High, Guess again.")
    elif user_guess < correct_answer:
        print("Oops, Too low, Guess again.")
    else:
        print(f"You got it! The correct answer is {correct_answer}")
        break

    attempts -= 1

if attempts == 0:
    print("You ran out of attempts. Game over!")

