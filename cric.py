# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 19:12:18 2019

@author: kingshuk02
"""

#%%
import random
def ball():
  ini_run=0
  a=True  
  while a==True:
      b=int(input("enter one number from 1 to 6" ))
      c=random.randrange(1,6)
      if b==c:
            print("Computer lost a wicket")
            a=False
            print("computer made ",ini_run,"runs")
      else:
          ini_run+=c
      print("computer made ",ini_run,"runs")
  print("you need ",ini_run+1,"runs to win")
  d=True
  comp=0
  while d==True:
      e=int(input("enter one number from 1 to 6"))
      f=random.randrange(1,6)
      if e==f:
          print("You lost one wicket")
          print("you made ",comp,"runs")
          d=False
      else:
          comp+=e     
          print("You made ",comp,"runs")     
          
          
          if comp<ini_run+1:
              print("you lost the game")
              d=False
  if comp>ini_run+1:
              print("you won the game")
  
                         
      
def runs():
  ini_run=0
  a=True  
  while a==True:
      b=int(input("enter one number from 1 to 6" ))
      c=random.randrange(1,6)
      if b==c:
            print("you lost a wicket")
            a=False
            print("you made ",ini_run,"runs")      
      else:
          ini_run+=b
      print("you made ",ini_run,"runs")
  print("computer needs ",ini_run+1,"runs")
  d=True
  comp=0
  while d==True:
      e=int(input("enter one number from 1 to 6"))
      f=random.randrange(1,6)
      if e==f:
          print("Computer lost one wicket")
          d=False
          print("computer made ",comp,"runs")
      else:
          comp+=f     
          print("computer made ",comp,"runs")     
          
          
          if comp>ini_run+1:
              print("you lost the game")
              d=False
  if comp<ini_run+1:
              print("you won the game")
              
      
          
print("Welcome to Cricket")
toss=input("enter if you want heads or tails: ")
coin=random.choice(["heads","tails"])
if toss==coin:
    choice=input("what do you want to choose batting or balling: ")
    if choice=="batting":
        runs()
        
    elif choice=="balling":
        ball()
else:
    print("you lost the toss")
    choice2=random.choice(["batting","balling"])
    if choice2=="batting":
        print("the computer chose Batting")
        ball()
    if choice2=="balling":
        print("the computer chose Balling")
        runs()          
print("Thank You for playing" )              












