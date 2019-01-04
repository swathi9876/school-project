# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 11:43:54 2018

@author: student
"""
print("""the rules are as follows:- 
      the player and dealer get 2 cards each , the dealer is blind and player is seen
      if the player has total less than 11, a new card is served 
      if the total ever exceeds 21 , game over
      once you have a total below 21 , you start playing.
      press hit to get a new card and press anything else to stop.
      again , if total exceeds 21, its a bust but if its under 21 , you 
      choose to proceed.
      when you have a satisfactory total , press stop . 
      once stopped , your cards are compared with the dealer and if you 
      have a higher total , you win else you lose
      as a special mention to Mr Rohan Sreelesh , we have added a feature that 
      shows you the first card of the dealer as well... 
      enjoy""")
s=''
import random
l=[1,2,3,4,5,6,7,8,9,10,11,12,13]
z=0
x=random.choice(l)
y=random.choice(l)
x1=random.choice(l)
y1=random.choice(l)
t=x+y
t1=x1+y1
print('the first card of the dealer is',x1)
print('your cards are',x,'and',y) #complication 1
if t >21:
    print("game over")
elif t<=11:                         #complication 2
    z=random.choice(l)
    t=x+y+z
    print('your new cards are',x,y,z)
    print("your total is",x+y+z)
    s=input('hit to play and stop to fold:  ')
    if s=='hit':
        while s!='stop':
            p=random.choice(l)
            print('your card is',p)
            print(t)
            t=x+y+z+p
            print('and total is',t)
            if t>21:
                print("bust")
                break
            s=input('hit to play and stop to fold:  ')
            if s=='hit':
                continue
            else:
                  if t>(x1+y1):
                      print('you win , dealer lost')
                      print("the dealer has",x1+y1)
                  else:
                      print('you lost')
                      print("the dealer has",x1+y1)
                  break
    else:
        if t>(x1+y1):
            print("you won, the dealer had",x1+y1)
        elif t<(x1+y1):
            print("you lost,the dealer had",x1+y1)
elif t>11:  
    print("your total is",t)                            #complication 3
    s=input('hit to play and stop to fold:  ')
    if s=='hit':                                         #p overwritten issue
        while s!='stop':
            p=random.choice(l)
            print('your card is',p)
            t=x+y+z+p
            
            print('and total is',t)
            if t>21:
                print("bust")
                break
            s=input('hit to play and stop to fold:  ')
            if s=='hit':
                continue
            else:
                  if t>(x1+y1):
                      print('you win , dealer lost')
                      print("the dealer has",x1+y1)
                  else:
                      print('you lost')
                      print("the dealer has",x1+y1)
                  break
    else:
        if t>(x1+y1):
            print("you won, the dealer had",x1+y1)
        elif t<(x1+y1):
            print("you lost,the dealer had",x1+y1)
          