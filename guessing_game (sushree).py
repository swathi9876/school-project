# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 12:30:04 2019

@author: student
"""

#%%
import random
print("Welcome to Word Guess game! Lets test how strong your vocabulary is.\n\t\t Good Luck!")
print("You have 5 attempts to guess the word")
WORDS = ("Mathematics","pizza","pasta","examination","computer", "Python", "Program", "Instructions","mississippi","university",
         "happy","handsome","heaven","peace","school")
word = random.choice(WORDS)
correct = word
tries = 1
hint1 = word[0]
hint2 = word[len(word)-1]
hint3 = word[1]
hint4 = word[len(word)-2]
l=len(word)-2
print("\t\tLength of the word: ", len(word),"\n")
print(hint1,'_ '*l,hint2)
guess = input("Guess the word: ")
while guess.lower() != correct.lower() and guess != "" and tries < 5:
    print("No!")
    tries += 1
    if tries==3:
        command = input("Would you like a hint? y or n: ")
        if command.lower() == "y":
            print("The second and second last letter of the word is: ", hint1,hint3,'_ '*(l-1),hint4,hint2)
    print("\nTries remaining: ", 6-tries)
    guess = input("Guess the word: ")
if guess.lower() == correct.lower():
    print("\nYes! You guessed the word! The word was: ", correct)
    print("You guessed it in ", tries)
else:
    print("\nNo! You ran out of tries!")
    print("The word was: ", correct)