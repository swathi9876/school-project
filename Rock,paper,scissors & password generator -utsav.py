# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 20:29:40 2019

@author: utsav
"""
#%%ROCK,PAPER,SCISSORS

from random import randint
 
#create a list of play options
t = ["Rock", "Paper", "Scissors"]
 
#assign a random play to the computer
computer = t[randint(0,2)]
n=int(input('enter the number of rounds to play'))
#set player to False
player = False
for i in range (n): 
    while player == False:
#set player to True
        player = input("Rock, Paper, Scissors?")
        if player == computer:
            print("Tie!")
        elif player == "Rock" or 'rock':
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
            else:
                print("You win!", player, "smashes", computer)
        elif player == "Paper" or 'paper':
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
            else:
                print("You win!", player, "covers", computer)
        elif player == "Scissors" or 'scissors':
            if computer == "Rock":
                print("You lose...", computer, "smashes", player)
            else:
                print("You win!", player, "cut", computer)
        else:
            print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
    

#%% 

import random

chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@!#$%&'

print('Note- Special symbols might not always be used in these passwords')
length=int(input('enter a password length'))
lenght=int(length)

for p in range(3):
    password=''
    password1=''
    for c in range(length):
        password+=random.choice(chars)
    print(password)
  
print('The program has executed 3 passwords mentioned above ')

if length<=4 :
    print('Password Level: Weak')
elif length<=6 :
    print('Password Level: Medium')
elif length<=8 :
    print('Password Level: Strong')
elif length<=10:
    print('Password Level: Extreme')
    
#%%