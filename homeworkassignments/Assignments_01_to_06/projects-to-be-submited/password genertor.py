# project 7: Password Generator in Python

import random
import string

def generated_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#user's input
length = int(input("Enter the length of your desired password:"))

password = generated_password(length)
print("Your Desired Generated Password:",password)

