# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 07:09:57 2021

@author: tjame
"""

name = input("Type your name: \n")
print(f"\ndWelcome {name} to this adventure!")

answer = input(
    "You've woken up in the forest by yourself, it's cold and damp. You have no recollection of what's happened before you blacked out. You walk 15 yards and stumble onto a trail, after 50 yards it splits left and right. Which way would you like to go? (Type left or right)\n").lower()

if answer == "left":
    answer = input("You've come to a river, you can keep walking or swim across. Type walk to keep walking and swim to swim across: (Type walk or swim)\n").lower()
    
    if answer == "swim":
        print("\nYou swam across and the current took you under, you cannot escape it and you lost the game.")
    elif answer == "walk":
        print("\nYou walked for many miles, ran out of water and you lost the game.")
    else:
        print("\nNot a valid option. You lose.")
    
    
elif answer == "right":
    answer = input("You've come to a bridge, it looks wobbly, do you want to cross it or head back? (Type cross or back) \n").lower()

    if answer == "back":
        print("\nYou go back and lose")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? (Type yes or no) \n").lower()
        
        if answer == "yes":
            print("\nYou talk to the stranger and they give you a car ride to safety. You WIN!")
        elif answer == "no":
            print("\nYou ignore this stranger and they are offended and leave you stranded, you lose.")
        else:
            print("\nNot a valid option. You lose.")
    else:
        print("\nNot a valid option. You lose.")

else:
    print("\nNot a valid option. You lose.")
    
print(f"\nThank you for playing {name}")