# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 11:46:46 2019

@author: student
"""

#%%
import random
print("WELCOME TO PASSWORD GENERATOR")
print("=============================")
d={}
m=eval(input("Hi! would you like to input the characters to be used for password generation?'yes' or 'no'?"))
if m=='yes':
    chars=input("enter characters you would like to use without any gaps")
    n=int(input('Enter the number of passwords to be generated'))
    length=int(input('password length'))
    for p in range(n):
        u=input('enter a username') 
        key=u
        password=''
        for i in range(length):
            password+=random.choice(chars)                    
            value=password
            d[key]=value
        #print(d)
        #print(password)
elif m=='no':   
    chars='abcdefghijklmnopqrstuvwxyz1234567890!@#$%&'
    n=int(input('Enter the number of passwords to be generated'))
    length=int(input('password length'))
    for p in range(n):
        u=input('enter a username') 
        key=u
        password=''
        for i in range(length):
            password+=random.choice(chars)                    
            value=password
            d[key]=value
        #print(d)
        #print(password)
else:
    print("enter a valid input")
    
k=eval(input('Do you want to change your password?"yay"or"nay"'))
if k=="yay":
    z=input("enter the username for which you would like to change the password")
    n=input("enter a new password")
    if z in d:
        d[z]=n
elif k not in("yay","nay"):
    print("enter a valid input")
    
        
y=eval(input('do you want to cross check for your final password?"yes"or"no"'))
if y=='yes':
    m=input("enter username")
    n=input("enter password")
    if m in d:
        if d[m]==n:
            print("Correct password entered")
        else:
            print("Incorrect password entered")
    else:
        print("Enter a valid username")
print('=======================')
print('Thank you for visiting!')























