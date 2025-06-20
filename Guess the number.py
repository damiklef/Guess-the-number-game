# Guess the number
import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    no_of_tries = 5
    while guess != random_number:
        print(f"You have {no_of_tries} of guess left")
        guess = int(input(f"Guess a number between 1 and {x:}: "))
        no_of_tries -= 1
        
        if no_of_tries == 0:
            print(f"Sorry the nummber is {random_number}")
            break
    else:
        print(f"Your guess is {guess} and the random number is {random_number}")
guess(10)