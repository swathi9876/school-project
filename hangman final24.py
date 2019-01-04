# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 09:54:12 2018

@author: student
"""

#hangman
import random
o=[]
h=[]
a=[]
w=[]
l=['abruptly','absurd','abyss','affix','askew','avenue','awkward','axiom','azure','bagpipes','bandwagon','banjo','bayou','beekeeper','bikini','blitz','blizzard','boggle','bookworm']
print("do you want to enter a word or use an inbuilt word")
c=input()
if c=='yes':
    print("enter your word")
    word=input()
    print(word)
    for i in range(len(word)):
        w.append(word[i])
        print('_,',end='')
        
        p=''
    print('now start entering letters, you have',len(word)+4,'chances')
        
    for j in range(len(word)+4):
        p=input()
        if p in w:
            print("correct")
            a.append(p)
        else:
            print("false")
    print(a)
    print("these are the letters you have guessed correctly")
    print("now enter the word , you have 3 chances")
    for m in range(3):
        g=input()
        if g==word:
            print("you won")
            break
        else:
            print("try again, you have",2-m,'chance(s)')

else:
    x=random.choice(l)
    print(x)
    for i in range(len(x)):
        o.append(x[i])
        p=''
        print('_,',end='')
    print('now start entering letters, you have',len(x)+3,'chances')
    print('here are some letters to help you')
    for u in range(len(x)//2):
        print(random.choice(x))
    for j in range(len(x)+3):
        p=input()
        if p in o:
            print("correct")
            a.append(p)
        else:
            print("false")
    print(a)
    print("these are the letters you have guessed correctly")
    print("now enter the word , you have 3 chances")
    for m in range(3):
        g=input()
        if g==x:
            print("you won")
            break
        else:
            print("try again, you have",2-m,'chance(s)')

            
#take the inbuilt words in a dictionary with key as the
# word to be guessed and the value as the hints