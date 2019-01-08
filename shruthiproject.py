# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 12:20:51 2019

@author: student
"""

#%%decryptionencryption
sol=''
string=str(input('enter a string for coding'))
n=len(string)
for i in range(n):
    y=string[i]
    if ord(y)<=50:
        p=ord(y)-10
        sol+=chr(p) 
    elif ord(y)>50 and ord(y)<=75:
        q=ord(y)+25
        sol+=chr(q)
    elif ord(y)>75 and ord(y)<=100:
        r=ord(y)+200
        sol+=chr(r)
    elif ord(y)>100 and ord(y)<=200:
        s=ord(y)+1000
        sol+=chr(s)

print(sol,'is the secret message')
s=str(input('enter the output received'))
ans=''
for j in range(n):
    z=s[j]
    if ord(z)>=-10 and ord(z)<=40:
        a=ord(z)+10
        ans+=chr(a)
    elif ord(z)>75 and ord(z)<=100:
        b=ord(z)-25
        ans+=chr(b)
    elif ord(z)>275 and ord(z)<=300:
        c=ord(z)-200
        ans+=chr(c)
    elif ord(z)>1100 and ord(z)<=1200:
        d=ord(z)-1000
        ans+=chr(d)

print(ans,'is the original message')


#%%guess the no.
l=[]
point=0
print('You initially have 0 points.For every correct answer you are awarded 3 points and for wrong answer 1 mark is deducted')
print('You are allowed to play till your points become -6')
q=None
import random
result='start'
while result!='quit':
    for i in range(9):
        p=random.randrange(1,26)
        
        l.append(p)
    print(l)
    x=eval(input('enter no'))
    q=random.choice(l)
    if q==x:
        
        print('you win')
        point+=3
        print('points are',point)
    else:
        
        print('you lose')
        print('the no was:',q)
        point-=1
        print('points are',point)
    if point<-5:
        result='quit'
    else:
        result='continue'
    l=[]
#%%riddle

point=0
print('there are 5 levels')
print('for correct answer you get points ten times the round no.')
print('for wrong answer 25% of points of the round are deducted')
print('if you pass no points are deducted')
x=eval(input('enter your target points'))
d={'what is a table that you can eat':'vegetable','it can be served but never eaten':'tennis ball','the more you take the more you leave it behind':'footsteps','it has many keys but no doors':'keyboard','i am alive but donot need food,water can kill me':'fire'}
for i in range(len(d)):
    print('ready for level:',i+1)
    print(list(d.keys())[i])
    s=input('enter answer')
    if s==list(d.values())[i]:
        print('correct answer')
        point+=(i+1)*10
        print('points are',point)
    elif s=='pass':
        print('the answer is',list(d.values())[i])
        print('points are',point)
    else:
        print('wrong answer')
        point-=0.25*(i+1)*10
        print('the answer is',list(d.values())[i])
        print('points are',point)
print('game over')
if point>=x:
    print('well played')
else:
    print('good try')   
#%%
    
    
    
