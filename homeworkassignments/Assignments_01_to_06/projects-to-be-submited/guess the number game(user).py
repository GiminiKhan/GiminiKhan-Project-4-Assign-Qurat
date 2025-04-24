# project 3 - Guess the Number Game Python Project (User)

import random
print ("Guess the number between 1 and 100!")
#generate randon number
number = random.randint(1, 100)

while True:
    guess = int(input( "Enter your guessed number:"))
    if guess <number:
        print("Too low number!")
    elif guess > number:
        print("Too high number!")
    else:
        print("Congratulation You Got It Right!")
        break
    