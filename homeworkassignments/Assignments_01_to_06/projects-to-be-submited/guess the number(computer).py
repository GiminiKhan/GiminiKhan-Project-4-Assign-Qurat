# project 2 : Guess The Number Game By Computer.
# 1 to 100 numbers.

import random
def guess_the_number():
    """Project 2: Guess the number game by computer."""
    number = random.randint(1, 100)
    guesses_left = 7
    #welcome message
    print ("welcome to the number guessing game")
    print("I am thinking a number between 1 to 100")

    # loop generated
    while guesses_left > 0:
        print(f"\nYou have {guesses_left} guesses left. ")
        try:
            guess = int(input("Take a guess of another number."))
        except ValueError:
            print("invalid input: Please enter a number")
            continue

        #guess the secret number
        if guess < number:
            print("Too low number . Tell another!")
        elif guess > number:
            print("Too high number. Tell another!")
        else:
            print(f"Congratulation! You got the correct number in {7 - guesses_left + 1} tries. !")
            return
        guesses_left -= 1
        #When all the guesses have ended.
        print(f"\nYou ran out of guess. The number was {number}.")

guess_the_number()
        


