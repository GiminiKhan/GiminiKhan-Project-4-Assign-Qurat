#Project 5: Hangman Game
import random
words = ['enum', 'python', 'collab', 'vscode', 'game']

word = random.choice(words)
guessed_letters = []
attempts = 6

print("welcome to hangman game project 5")
print("_" *len(word))

while attempts > 0:
    guess = input("\n guess the letters:").lower()

    if len(guess) !=1 or not guess.isalpha():
        print("write one alphabet only!")
        continue
    if guess in guessed_letters:
        print("This letter has already been guessed, choose another letter")
        continue
    guessed_letters.append(guess)

    if guess in word:
        print ("Correct Guess!")
    else:
        attempts -= 1
        print(f"Wrong {attempts} attempts.")

    displayed_word = " ".join([letter if letter in guessed_letters else "-" for letter in word])
    print(displayed_word)

    if "_" not in displayed_word:
        print(f"Congratulations! the correct word is: {word}")
        break
    else:
        print("Game Over! the correct word is: {word}")
