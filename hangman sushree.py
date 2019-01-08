# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 12:44:17 2019

@author: student
"""

#%%
import random
wordList = ["lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
 "laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat"]
guess_word = []
secretWord = random.choice(wordList) 
length_word = len(secretWord)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []
name = input("Please enter Your name\n")
print("Well, that's perfect moment to play some Hangman!\n")
for character in secretWord: 
    guess_word.append("-")
print("Ok, so the word You need to guess has", length_word, "characters")
print("Be aware that You can enter only 1 letter from a-z\n\n")
print(guess_word)
guess_taken = 0
while guess_taken < 7:
    guess = input("Pick a letter\n").lower()
    if not guess in alphabet: 
        print("Enter a letter from a-z alphabet")
    elif guess in letter_storage: 
        print("You have already guessed that letter!")
    else: 

            letter_storage.append(guess)
            if guess in secretWord:
                print("You guessed correctly!")
                for x in range(0, length_word): 
                    if secretWord[x] == guess:
                        guess_word[x] = guess
                        print(guess_word)

                if not '-' in guess_word:
                    print("You won!\n\t\tYou found the word.\n\t\tCONGRATULATIONS")
                    break
            else:
                print("The letter is not in the word. Try Again!")
                guess_taken += 1
                if guess_taken==1:
                    print("__________")
                    print("   |    |")
                    print("        |")
                    print("        |")
                    print("________| ") 
                elif guess_taken==2:
                    print("__________")
                    print("   |    |")
                    print("   O    |")
                    print("        |") 
                    print("________|") 
                elif guess_taken==3:
                    print("__________")
                    print("   |    |")
                    print("   O    |")
                    print("   |    |") 
                    print("________|") 
                elif guess_taken==4:
                    print("__________")
                    print("   |    |")
                    print("   O    |")
                    print("  /|    |") 
                    print("________|")
                elif guess_taken==5:
                    print("__________")
                    print("   |    |")
                    print("   O    |")
                    print("  /|\   |") 
                    print("________|")    
                elif guess_taken==6:
                    print("__________")
                    print("   |    |")
                    print("   O    |")
                    print("  /|\   |") 
                    print("__/_____|")
                elif guess_taken==7:
                    print("__________")
                    print("   |    |")
                    print("   O    |")
                    print("  /|\   |") 
                    print("__/_\___|")   
                    print(" Sorry Mate, You lost :<! The secret word was",         secretWord)
print("Game Over!") 