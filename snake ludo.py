# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 13:16:47 2019

@author: student
"""

import random
a=[]
b=[]
c=[]
k=0
l=0
ab=0
print('_________________','WELCOME TO SNAKE LUDO','_________________')
print('_______________________','RULES','_________________________')
print('dice shows:0,1,2,3,4,5')
print('first to reach 20 wins')
print('                    ','|Lets begin!|')
x=input('enter name player1')
y=input('enter name player2')
u=input('enter name player3')
while k<20 and l<20 and ab<20:
    t=input('press roll player1')
    for j in range(0,1):
        a.append(random.randint(0,5))        
    for i in a:
        k=k+int(i)
        a.remove(i)
        
    if k==1:
        r='lucky enough,its a baby snake stay there'
        print(x,'at',k,r)
    if k==13:
        print('u bit by a snake')
        r=7
        k=k-r
    if k==17:
        q=13
        print(x,'at',k)
        print('Sorry',x,'u bit by a snake','go to',q)
        print('there is a snake at 13 also,go to 7')  
        k=7
    print(x,'at',k)
    s=input('press roll player2' ) 
    
    for j in range(0,1):
        b.append(random.randint(0,5))
    for i in b:
        l=l+int(i)
        b.remove(i)
        
    if l==1:
        r='lucky enough,its a baby snake stay there'
        print(y,'at',k,r)
    if l==13:
        print('u bit by a snake')
        r=7
        l=l-r
    if l==17:
        q=13
        print(y,'at',k)
        print('Sorry',y,'u bit by a snake','go to',q)
        print('there is a snake at 13 also,go to 7')  
        l=7
    print(y,'at',l)
    o=input('press roll player3')
    for j in range(0,1):
        c.append(random.randint(0,5))        
    for i in c:
        ab=ab+int(i)
        c.remove(i)
    if ab==1:
        r='lucky enough,its a baby snake stay there'
        print(u,'at',ab,r)
    if ab==13:
        print('u bit by a snake')
        r=7
        ab=ab-r
    if ab==17:
        q=13
        print(u,'at',ab)
        print('Sorry',u,'u bit by a snake','go to',q)
        print('there is a snake at 13 also,go to 7')  
        ab=7
    print(u,'at',ab)
    
if k>=20 and ab<20 and l<20:
    print(x,'is the winner' )
elif l>=20 and k<20 and ab<20:   
    print(y,'is the winner')
elif ab>=20 and k<20 and l<20:   
    print(u,'is the winner')  
elif k>=20 and ab>=20 and l<20:
    print(x,'and',u,'tied')
elif l>=20 and k>=20 and ab<20:   
    print(y,'and',x,'tied')
elif ab>=20 and l>=20 and l<20:   
    print(u,'and',y,'tied')     