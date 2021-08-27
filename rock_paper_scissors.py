# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 06:17:25 2021

@author: tjame
"""

import random

user_wins = 0
computer_wins = 0
ties = 0
number_of_games = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print(f"Computer picked {computer_pick}.")
    
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        number_of_games += 1
    
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        number_of_games += 1
    
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        number_of_games += 1
        
    elif user_input == "rock" and computer_pick == "rock":
        print("It's a tie!")
        ties += 1
        number_of_games += 1
        
    elif user_input == "paper" and computer_pick == "paper":
        print("It's a tie!")
        ties += 1
        number_of_games += 1
        
    elif user_input == "scissors" and computer_pick == "scissors":
        print("It's a tie!")
        ties += 1
        number_of_games += 1
    
    else:
        print("You lost!")
        computer_wins += 1
        number_of_games += 1

print(f"Of the {number_of_games} games played, you won {user_wins} times, the computer won {computer_wins} times, and there were {ties} ties! Goodbye.")

    
    



