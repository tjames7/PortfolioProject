# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 07:09:57 2021

@author: tjame
"""

name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You've come to a river, you can walk around it or swim across. Type walk to walk around and swim to swim across: ").lower()
    
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")
    
    
elif answer == "right":
    answer = input("You've come to a bridge, it looks wobbly, do you want to cross it or head back? Answer with cross or back").lower()

    if answer == "back":
        print("You go back and lose")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? Choose yes or no").lower()
        
        if answer == "yes":
            print("You talk to the stranger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore this stranger and they are offended, you lose.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")
    
print(f"Thank you for trying {name}")