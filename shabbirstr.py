# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 12:50:09 2018

@author: student
"""

#%%
#dictionary#
d={}
a=1
while a!=0:
    key=eval(input('enter the team name:'))
    w=eval(input('enter the no. of wins:'))
    l=eval(input('enter the no. of losses:' ))
    p=w/(w+l)*100
    value=(w,p)
    d[key]=value
    s=eval(input('if stop press s:'))
    if s=='s':
        break
    else:
        continue
print(d)
   
#%%
d={}
a=1
while a!=0:
    key=eval(input('enter the product name:'))
    p=eval(input('enter the cost:' ))
    value=(p)
    d[key]=value
    s=eval(input('if stop press s:'))
    if s=='s':
        break
    else:
        continue
print(d)
co=eval(input('to continue press c:'))
if co=='c':
    while a!=0:    
        i=eval(input('enter the product name:'))
        for i in d.keys():
            pr=d.get(i,'no product')
            print(pr)
            st=eval(input('if stop press s:'))
            if s=='s':
                break
            else:
                continue
print('PROGRAM ENDED' )    
#%%
d={}
n=12
for i in range(n):
    key=eval(input('enter month name:'))
    value=eval(input('enter the no. of days:'))
    d[key]=value
i=31
if i in d.values():
    print('the months with 31 days:')
    print(key)
#%%

x={}
y={}
a=1
while a!=0:
    key=eval(input('enter key:'))
    value=eval(input('enter the value:'))
    key1=str(value)
    value1=int(key)
    x[key]=value    
    y[key1]=value
    s=eval(input('to stop press s'))
    if s=='s':
        break
    else:
        continue
print('the original dict:',x)
print('the inverted dict:',y )
#%%
x={}
y={}
a=1
while a!=0:
    key=eval(input('enter key:'))
    value=eval(input('enter the value:'))
    key1=eval(input('enter key:'))
    value1=eval(input('enter the value:'))
    x[key]=value    
    y[key1]=value
    s=eval(input('to stop press s:'))
    if s=='s':
        break
    else:
        continue
z=list(x.keys())
l=len(z)
for i in range(0,l-1):
    if z[i] in y.keys():
        x[key]=key1
        t=list(x)
print(x)
print(y)
print(t)
#%%
x={}
y={}
a=1
while a!=0:
    key=eval(input('enter key:'))
    value=eval(input('enter the value:'))
    key1=eval(input('enter key:'))
    value1=eval(input('enter the value:'))
    x[key]=value    
    y[key1]=value
    s=eval(input('to stop press s:'))
    if s=='s':
        break
    else:
        continue
z=list(x.values())
l=len(z)
for i in range(0,l-1):
    if z[i] in y.values:
        x[key]=key1
        t=list(x)
l1=len(t)/2
print('the keys are',t)
if l1==0:
    print('the no. of overlapped values is zero')
else:
    print('the no. of overlapped values',l1)

#%%
#project#
#physicscalculator#
print('1- density')
print('2-velocity')
print('3-momentum')
print('4-power')
print('5-potential energy')
print('6-kinetic energy')
print('7-ohm law')
print('8-electric power')
print('9-index of refraction')
a=1
while a!=0:
    x=eval(input('enter the needed formula:'))
    if x==1:
        m=eval(input('enter the mass:'))
        v=eval(input('enter the volume:'))
        D = m / v
        print(D)
    elif x==2:
        s=eval(input('enter the displacement'))
        t=eval(input('enter the time taken:'))
        v = s / t 
        print(v)
    elif x==3:
        m=eval(input('enter the mass:'))
        v=eval(input('enter the velocity:'))
        Mo = m*v
        t=eval(input('enter the time taken:')) 
        F=Mo/t
        print(F)
    elif x==4:
        m=eval(input('enter the mass:'))
        v=eval(input('enter the velocity:'))
        Mo = m * v 
        print(Mo)
    elif x==5:
        t=eval(input('enter the time taken:'))
        w =eval(input('enter the amount of work done:'))
        Po = w / t
        print(Po)
    elif x==6:
        m = eval(input('enter the mass:')) 
        g = 10 
        h = eval(input('enter height :'))
        p=m*g*h
        print(p)
    elif x==7:  
        m = eval(input(' enter mass:'))
        v = eval(input(' enter velocity:'))
        p=1/2*m*v**2
        print(p) 
    elif x==8:  
        R = eval(input(' enter Resistance:'))
        I = eval(input(' enter current:'))
        v=I*R
        print(v)
    elif x==9:
        V = eval(input(' enter voltage applied:')) 
        I = eval(input(' enter current:'))
        P=V*I
        print(P)
    elif x==10: 
        c = eval(input(' enter  the velocity of light in a vacuum' ))
        v = eval(input(' enter  the velocity of light in the given material'))
        n=c/v
        print(n)
    S=str(input('to stop press s:'))
    if S=='s':
            break
print('PROGRAMME ENDED')

#%%
#project-2#
#7up,7down,exact7#
n=1
print('A GAME FOR 3 AT A TIME 7UP/7DOWN OR EXACT 7')
print('EACH PLAYER GETS 10 POINTS FROM START')
import random
p1=10
p2=10
p3=10
N=3
while n!=0:
        for i in range (1,N+1):
            B=str(input('enter your bet player:'))
            j=random.randrange(0,12)
            print('the rolled no. is:',j)
            if ('under' in B ) and j<7 and i==1:
               p1=p1+1
            elif ('under' in B) and j<7 and i==2:
                p2=p2+1
            elif ('under' in B) and j<7 and i==3:  
                p3=p3+1
            elif ('above' in B) and j>7 and i==1:  
                p1=p1+1
            elif ('above' in B) and j>7 and i==2:  
                p2=p2+1
            elif ('above' in B) and j>7 and i==3:    
                    p3=p3+1
            elif B==j and i==1:          
                    p1=p1+2
            elif B==j and i==2:
                p2=p2+2
            elif B==j and i==3:
                p3=p3+2
            elif i==1:
                p1=p1-1
            elif i==2:
                p2=p2-1
            elif i==3:
                p3=p3-1
        s=str(input('TO STOP THE GAME PRESS S:')) 
        if s=='s':
              break
        else:
            continue
print('the score of player 1 is:',p1)
print('the score of player 2 is:',p2)
print('the score of player 3 is:',p3)
#%%
names=['sam','amit','jai','arjun','pranay','sabby','aayan','billu','sammy','rishi','grace','jessie','laksh','tvish','parus','raj']
age=['10-16','16-29','29-56','56+']
income=['5000-10000','10000-25000','25000-50000','50000+']
job=['engineer','driver','CA','manager','receptionist','supervisor','chef']
q1=['romantic','sci fi','adventure','horror','comedy','comic']
q2=['yes','no','maybe','does not know']
q3=['no influence','influenced','maybe']
q4=['should be censored','not to be censored']
w='0'
a='0'
s='0'
d='0'
L=''
LL=''
LLL=''
LLLL=''
LLLLL=''
LLLLLL=''
LLLLLLL=''
L1=len(names)
L2=len(age)
L3=len(income)
L4=len(job)
L5=len(q1)
L6=len(q2)
L7=len(q3)
L8=len(q4)
import random
n=1
while n!=0:
    j=random.choice(names)
    i=random.choice(age)
    k=random.choice(income)
    l=random.choice(job)
    m=random.choice(q1)
    n=random.choice(q2)
    o=random.choice(q3)
    p=random.choice(q4)
    print('what is ur name?')
   # for t in range (L1-1):
    #    ll1=names[t]
     #   print(ll1,end='')
   # print('The name is :',j)
    T=str(input())
    print('what is ur age?')
    for y in range (L2):
        ll2=age[y]
        print('   ',ll2,end='')
        print('  ')
    print('The age is:',i)
    print('what is ur income?')
    for x in range (L3):
        ll3=income[x]
        print('   ',ll3,end='')
        print('  ')
    print('The income is:',k)
    print('what is ur job?')
    for z in range(L4):
        ll4=job[z]
        print('  ',ll4,end='')
        print('  ')
    print('The job is:',l)       
    print('what type of films u like?')
    for q in range(L5):
        ll5=q1[q]
        print('    ',ll5,end='')
        print('   ')
    print('The ans to above question is :',m)
    print('do u think films influence our daily lives?')
    for Q in range(L6):
        ll6=q2[Q]
        print('    ',ll6,end='')
        print('    ')
    print('The ans to above question is :',n)
    print('is ur fashion influenced by films?')
    for I in range (L7):
        ll7=q3[I]
        print('   ',ll7,end='')
        print('   ')
    print('The ans to q3 is :',o)
    print('do u think scenes in films should be censored?')
    for J in range(L8):
        ll8=q4[J]
        print('   ',ll8,end='')
        print('   ')
    print('The ans to q3 is :',p)
    L=L+i
    LL=LL+k
    LLL=LLL+l
    LLLL=LLLL+m
    LLLLL=LLLL+n
    LLLLLL=LLLLLL+o
    LLLLLLL=LLLLLLL+p
    print('to stop press s:')
    s=str(input())
    if s=='s':
        break
    else:
        continue
N1=len(L)
for R in range(N1):
    if '10-16' in L:
            w=w+'1'
    elif '16-29' in L:
            a=a+'1'
    elif '29-56' in L:
                s=s+'1'
    elif '56+' in L:
                    d=d+'1'
n1=len(w)
n2=len(a)
n3=len(s)
n4=len(d)
print("the no.of people with age'10-16':",n1-1)
print("the no.of people with age'16-29':",n2-1)
print("the no.of people with age'29-56':",n3-1)
print("the no.of people with age'56+':",n4-1)
