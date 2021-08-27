# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 05:42:22 2021

@author: tjame
"""

import random
from sys import exit

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        exit()

else:
    print("Please type a number next time.")
    exit()
    
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue
    
    if user_guess == random_number:
        print("Correct!")
        break
    elif user_guess > random_number:
        print("Your guess is above the number!")
    else:
        print("Your guess is below the number!")

print("You got in", guesses, "guesses")
