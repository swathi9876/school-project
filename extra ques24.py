# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 09:30:56 2019

@author: student
"""

#%%
#binary to hexadecimal
c=''
j=0
#d={0:0000,1:0001,2:0010,3:0011,4:0100,5:0101,6:0110,7:0111,8:1000,9:1001,10:1010,11:1011,12:1100,13:1101,14:1110,15:1111}
x=(input("give a value"))
l=len(x)
p=4-(l%4)
if l%4!=0:
    for k in range(p):
        c='0'+c
print("the len of c is " ,len(c))
x=c+x
n=len(x)+len(c)
for i in range(n//4):
    
    k=j+4
    a=x[j:k]
    j+=4
    
    if a =='0000':
        print(0,end='')
    elif a=='0010':
        print(2,end='')
    elif a=='0011':
        print(3,end='')
    elif a=='0100':
        print(4,end='')
    elif a=='0101':
        print(5,end='')
    elif a=='0110':
        print(6,end='')
    elif a=='0111':
        print(7,end='')
    elif a=='1001':
        print(8,end='')
    elif a=='1001':
        print(9,end='')
    elif a=='1010':
        print('A',end='')
    elif a=='1011':
        print('B',end='')
    elif a=='1100':
        print("C",end='')
    elif a=='1101':
        print('D',end='')
    elif a=='1110':
        print('E',end='')
    elif a=='1111':
        print("F",end='')
    
print('  is your converted value')
    
#%%
l=[2,6,9]
k=[7,1,4]
j=[]

l.sort()
k.sort()
for i in range(2,-1,-1):
    if l[i]>k[i]:
        j.append(l[i])
        j.append(k[i])
    else:
        j.append(k[i])
        j.append(l[i])
print(j)
        #%%
x=input()
l=len(x)
p=[]
for i in range(l):
    p.append(x[i])

for i in range(l):
    if p[i]==' ':
        p.pop(i)
print(p)
    