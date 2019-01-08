# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 12:46:21 2019

@author: student
"""

#%%
import random
WORDS = ("python", "mirror","mouse", "easy", "difficult", "answer", "xylophone","staircase")
print('Welcome to Word Jumble!/n/t/tUnscramble the letters to make a word.\n\t\t(Press the enter key at the prompt to quit.)')
play=input("Do you want to play? (yes or no)")
while play.lower()=="yes" or play.lower()=='y':
    word = random.choice(WORDS)
    correct = word
    jumble =""
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]
    print("The jumble word is:", jumble)
    guess = input("\nYour guess: ")
    while guess.lower() != correct and guess != "" :
        print("Sorry, that's not it.")
        hint=input("Do you need a hint?")
        if hint.lower()=="yes" or hint.lower()=='y' :
            if correct=="python":
                print("Its a snake...")
            elif correct=="mouse":
                print("its a rat")
            elif correct== "easy":
                print("opposite of hard")
            elif correct=="difficult":
                print("synonyms")
            elif correct=="answer":
                print("its is given for a question ")
            elif correct=="xylophone":
                print("It is a toy...")
            elif correct=="mirror":
                print("What is deaf, dumb and blind, but always tells the truth?")
            elif correct=="staircase":
                print("What goes up and down without moving?")
        guess = input("Your guess: ")
    if guess.lower()== correct:
        print("That's it!  You guessed it!\n")
        
        play=input("Do you want to play again? (yes or no)")
    elif guess.lower()== "":
        print("You failed...")
        play=input("Do you want to play again? (yes or no)")
print("Thanks for playing.")       