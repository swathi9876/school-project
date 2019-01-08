# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 10:10:14 2019

@author: Aaryan H
"""

#%%
import random
print(''' Rules:
      Scissors cuts paper, paper covers rock, rock crushes lizard, 
      lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard,
      lizard eats paper, paper disproves Spock, Spock vaporizes rock and 
      rock crushes scissors.''')
a = input('Enter username: ')
print(a, 'vs Computer')
n = int(input('Enter number of rounds.'))
p = 0
c = 0
for i in range(n):
    l = ['Rock', 'Scissors', 'Paper', 'Lizard', 'Spock']
    player = input('Rock, Paper, Scissors, Lizard or Spock? ')
    if player in l:
        print(player, 'vs', end = ' ')
        index = random.randrange(0,5)
        computer = l[index]
        print(computer)
        if player == computer:
            print('Twinsies...')
            p += 1
            c += 1
        elif player == 'Paper':
            if computer == 'Rock':
                print('Paper covers rock.')
                p += 2
            elif computer == 'Scissors':
                print('Scissors cuts paper.')
                c += 2
            elif computer == 'Lizard':
                print('Lizard eats paper.')
                c += 2
            elif computer == 'Spock':
                print('Paper disproves Spock.')
                p += 2
        elif player == 'Scissors':
            if computer == 'Rock':
                print('Rock crushes Scissors.')
                c += 2
            elif computer == 'Paper':
                print('Scissors cuts paper.')
                p += 2
            elif computer == 'Lizard':
                print('Scissors decapitates lizard.')
                p += 2
            elif computer == 'Spock':
                print('Spock smashes Scissors.')
                c += 2
        elif player == 'Rock':
            if computer == 'Paper':
                print('Paper covers rock.')
                c += 2
            elif computer == 'Scissors':
                print('Rock crushes Scissors.')
                p += 2
            elif computer == 'Lizard':
                print('Rock crushes Lizard.')
                p += 2
            elif computer == 'Spock':
                print('Spock vaporizes Rock.')
                c += 2
        elif player == 'Lizard':
            if computer == 'Rock':
                print('Rock crushes Lizard.')
                c += 2
            elif computer == 'Scissors':
                print('Scissors decapitates Lizard.')
                c += 2
            elif computer == 'Paper':
                print('Lizard eats paper.')
                p += 2
            elif computer == 'Spock':
                print('Lizard poisons Spock.')
                p += 2
        elif player == 'Spock':
            if computer == 'Rock':
                print('Spock vaporises rock.')
                p += 2
            elif computer == 'Scissors':
                print('Spock smashes Scissors.')
                p += 2
            elif computer == 'Lizard':
                print('Lizard poisons Spock.')
                c += 2
            elif computer == 'Paper':
                print('Paper disproves Spock.')
                c += 2
    else:
        print('Enter a valid password.')
        continue
print('Computer:', c)
print(a, ': ', p, sep ='')
if p > c:
    print(a, 'Wins!')
elif c > p:
    print('Computer Wins!')
elif c == p:
    print('DRAW')
