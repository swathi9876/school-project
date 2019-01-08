# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 12:21:26 2019

@author: student
"""

import random
import time
import json
%clear
colour_dict={'RED':'R','YELLOW':'Y','ORANGE':'O','GREEN':'G','BLUE':'B','PURPLE':'P'}
title_card=''' 
               *     *    *    *****  *******  ******  *****  *     *  *******  *     *  * * *
               * * * *   * *   *         *     *       *   *  * * * *     *     * *   *  *    *
               *  *  *  *****  *****     *     ******  *****  *  *  *     *     *  *  *  *    *
               *     *  *   *      *     *     *       * *    *     *     *     *   * *  *    *
               *     *  *   *  *****     *     ******  *   *  *     *  *******  *     *  * * *
                                                                                       V-1    
                                                                                       
                                            BY AAYUSH RAJESH                                        '''
print(title_card)
print()
print()
blank='     '
colour_list=['R','Y','O','G','B','P']

print('RULES:')
print('1.The Player will attempt to guess the code set by the Challenger/Computer within a certain number of tries')
print('   Easy-     12 tries')
print('   Medium-   10 tries ')
print('   Difficult-8 tries')
print('2.There are 6 colours to choose from')
print('   RED-   R     YELLOW-Y') 
print('   ORANGE-O     GREEN- G')
print('   BLUE-  B     PURPLE-P')
print('A feedback will be provided after every move')
#CHOOSING DIFFICULY#
while True:
    mode=input('Enter difficulty level- Easy,Medium or Difficult: ')
    mode=mode.upper()
    if mode=='EASY':
        no_of_tries=12
        break
    elif mode=='MEDIUM':
        no_of_tries=10
        break
    elif mode=='DIFFICULT':
        no_of_tries=8
        break
    else:
        print('Not a valid mode. Please enter again')
#CHOOSING OPPONENT AND CREATING CODE#
code=''
while True:
    opponent=input('Enter your opponent- Challenger or Computer: ')
    opponent=opponent.upper()
    if opponent=='CHALLENGER':
        code=input('Enter the 6 colour code Challenger, with the colour codes: ')
        if len(code)!=6:
            print('Code exceeds length 6, try again')
            continue
        for a1 in code:
            if a1 not in colour_list:
                break
        else:
            break
        print('Code does not follow the colour codes')
        continue
    elif opponent=='COMPUTER':
        for a2 in range(6):
            code=code+random.choice(colour_list)
        print('Computer has set the code')
        break
    else:
        print('Not a valid opponent')
%clear
###
print(title_card)
print()
print()
dummy=input('Ready player?')
time.sleep(2)

tries=1
print('KEY:')
print(json.dumps(colour_dict,indent=3))
while no_of_tries!=0:
    
    print('Try',tries)
    
    game=True
    guess=input('Enter your guess')
    guess=guess.upper()
    if len(guess)!=6:                                                                      ##CHECKING FOR 6 LETTER CODE##
        print('Not valid. Try again')     
        continue
    for b in guess:                                                                        ##CHECKING FOR VALID CODE##
        if b not in colour_list:
            game=False
    if game==False:
        print('Not valid. Try again')
        continue
    
    for c1 in range(1,7):
        print(blank,c1,end='           ')
    print()
    for c2 in guess:
        print(blank,c2,end='           ')
    print()
    if guess==code:
        print('FEEDBACK: All colours in their correct positions')                          ##CHECKING FOR ALL CORRECT#
        break
    in_position=''
    for d in range(len(guess)):                                                            ##CHECK FOR COLOUR IN POSITION##
        if guess[d]==code[d]:
            in_position=in_position+str(d+1)+' '
    
    just_in_code=''
    
    for e in range(len(guess)):
        if guess[e] in code and str(e+1) not in in_position:
            just_in_code+=str(e+1)
        
    if in_position!='':
        print('FEEDBACK: Position(s) ',in_position,' have the correct colour in the right place.')
    if just_in_code!='':
        print('          Position(s)',just_in_code,' have a colour that is in the code but at the wrong place.')
    no_of_tries-=1
    tries+=1
else:
    print('You could not guess the code that ',opponent,' set')
    print('It was:',code)
if no_of_tries!=0:
    print('Congratulations!! You guessed the code ',opponent,'set with difficulty level',mode,'in',tries,'moves!')
    print('You are a MasterMind !!')