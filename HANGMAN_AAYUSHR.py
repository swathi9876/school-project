# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 12:19:54 2019

@author: Aayush Rajesh
"""

import random
import time
#DISPLAYS
graphic1='''
              *   *     *     *   *   * * * *   *     *     *     *   *
              *   *    * *    **  *   *         * * * *    * *    **  * 
              * * *   *****   * * *   *  * *    *  *  *   *****   * * *
              *   *   *   *   *  **   *  *  *   *     *   *   *   *  **
              *   *   *   *   *   *   * * * *   *     *   *   *   *   *   
                                                                         V-1    '''

graphicstrike4='''
             ________      
             |      |   
             |      O
             |     /|\\
             |      |
             |     / \\  
          ___|_____        
                            '''

graphicstrike0='''

             _________
             |       | 
             |
             |
             |
             |
          ___|_____          '''
          
graphicstrike1='''

             _________
             |       | 
             |       O 
             |        
             |
             |
          ___|_____          '''

graphicstrike2='''

             _________
             |       | 
             |       O
             |       |
             |       |
             |
          ___|_____          '''
        
graphicstrike3='''

             _________
             |       | 
             |       O
             |      /|\\
             |       |
             |
          ___|_____          '''


choice='Y'
while choice=='Y':
    %clear
    #RANDOM WORD
    word=random.choice(['OUIJA','JAZZ','BAGPIPES','CROQUET','DWARVES','QUILL','CROWD','NEEDLE','GYPSY','CARAVAN','TRACTOR','ALLIGATOR','SPHINX',
                    'PHARAOH','GENERAL','ZOMBIE','MEMENTO','FJORD','JUKEBOX','YACHT','GAZEBO','FISHHOOK','ACOUSTIC','ANTHROPOLOGY','MYTHOLOGY',
                    'ATMOSPHERE','BLACKBOARD','CENTURY','GOVERNMENT','HELICOPTER','HYDRAULIC','IRONCLAD','MARRIAGE','PALEONTOLOGY','PERMAFROST',
                    'PNEUMONOULTRAMICROSCOPICSILICOVOLCANOCONIOSIS','SYZYGY','ASTRONOMY','ZUCCHINI','XYLOPHONE','ZOOLOGIST','WINDSHIELD','ACCORDION',
                    'APPENDIX','BASKETBALL','CASSEROLE','CORRESPONDENT','GYMNASTICS','HIPPOPOTAMUS','INCANDESCENCE'])
    
    n=len(word)
    if n<5:
        a1=n-1
    
    elif n>=5 and n<=6:
        a1=n-2
    elif n>6 and n<=10:
        a1=n-4
    elif n>10:
        a1=n//2
    HMlist=[]
    for i in range(n):
        HMlist.append(word[i])
    positions=[]
    for x in range(n):
        positions.append(x)
    for j in range(a1):
        a2=random.choice(positions)
        HMlist[a2]='_'
        positions.remove(a2)
    
    print(graphic1)
    print('RULES:')
    print('1. You can choose to guess either a letter or a word each turn. Either type LETTER or WORD')
    print('2. ALWAYS enter in prompt in uppercase')
    print('3. Four strikes and you\'re out')    
    dummy=input('Ready?')
    time.sleep(2)
    
    print('LETS PLAY HANGMAN')
    strikes=0
    guesses=''
    while strikes<4:
        remains=''
        for y in range(n):
            if HMlist[y]!=word[y]:
                remains=remains+word[y]
        %clear
        print(graphic1)
        if strikes==0:
            print(graphicstrike0)
        elif strikes==1:
            print(graphicstrike1)
        elif strikes==2:
            print(graphicstrike2)
        elif strikes==3:
            print(graphicstrike3)
        print()
        print()
        print('Strikes:',strikes)
        print('Guesses:',guesses)
        for k in range(n):
            print(HMlist[k],end=' ')
        print()
        mode=input('Would you like to guess a letter or the word?')
        if mode=='WORD':
            guess=input('Enter word')
            if guess==word:
                print('Correct guess!!!')
                break
            else: 
                print('Wrong guess')
                strikes+=1
                continue
        guess=input('Enter letter:')
        
        if guess.islower():
            print('Please enter in capitals')
            time.sleep(1)
            %clear
            continue
        if guess in guesses:
            print('You have already guessed this letter,enter again')
            time.sleep(1)
            %clear
            continue
        if guess in remains:
            guesses+=guess
            for l in range(n):
                if word[l]==guess and HMlist[l]=='_':
                    HMlist[l]=guess
            print('Right guess')
            time.sleep(1)
            %clear
            
        else:
            guesses+=guess
            print('Wrong guess')
            strikes+=1
            time.sleep(1)
            %clear
            continue
        s=''
        for m in HMlist:
            s=s+m
        if s==word:
            print(s)
            break
    if strikes==4:
        print(graphicstrike4)
        print('GAME OVER')
        print('The word to guess was',word)
        choice=input('Would you like to play again? Y/N :')
    else:
        print('Congratulations you have won Hangman!!')
        choice=input('Would you like to play again? Y/N :')
print('Thanks for playing!!')