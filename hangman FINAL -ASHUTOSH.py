# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 13:10:36 2018

@author: student
"""
#%%

print('''
WELCOME TO 
         
            |     |   /\   |\    | _____  |\    /|   /\   |\    |
            |     |  /  \  | \   | |      | \  / |  /  \  | \   |
            |-----| |    | |  \  | |  ___ |  \/  | |    | |  \  |
            |     | |----| |   \ | |    | |      | |----| |   \ |
            |     | |    | |    \| |____| |      | |    | |    \|
            
            ''')



vowels=['a','e','i','o','u','A','E','I','O','U']
word=input('HELLO USER---------ASK SOMEONE TO ENTER A SUPER TOUGH WORD FOR YOU        ')
l=len(word)
l1=list(word)
l2=list(word)
for i in range(l):
    if word[i] not in vowels:
        l1[i]='_'
print(l1)




hang0=''' __________
                     '''
hang1='''    
__________
    |

                        '''
hang2='''
__________
    |
    O
           '''
hang3='''
__________
    |
    O
    |
    |
           ''' 
hang4='''
__________
    |
    O
   /|\\
    |
          '''
hang5='''
__________
    |
    O
   /|\\
    |
   / \\
           '''
man='''
__________




    O
   /|\\
    |
   / \\
       '''

for d in range(60):
    print()


n=''
for i in l1:
    n=n+' '+i
print("WELCOME PLAYER-----GUESS THIS WORD TO SAVE THE MAN",n)   
print(man)



wrong=0

m=''
while wrong<5 and '_' in l1:
    f=input('PRESS w TO GUESS THE ENTIRE WORD OR l TO GUESS A SINGLE LETTER       ')
    if f=='w':
        wordd=input('ENTER A WORD     ')
        if wordd==word:
            wrong=1
            break
        else:
            wrong=5
        
    else:
        letter=str(input('ENTER A LETTER     '))
        n=''
        if letter in l2:
            ind=l2.index(letter)
            l1[ind]=letter
            print()
            
            for z in range(5):
                lll=l2[ind+1:]
                if letter in lll:
                    ind1=lll.index(letter)
                    ind=ind1+ind+1
                    l1[ind]=letter
            
        else:
            wrong=wrong+1
            print('SORRY PLAYER-----LETTER IS ABSENT ')
            print()
            m=m+letter
        print()
        print()
        for j in l1:
                n=n+' '+j
        print(n)
        print('NUMBER OF WRONG ATTEMPTS=',wrong)
        print('WRONG LETTERS=',m)
        print()
        if wrong==0:
            print(hang0)
        elif wrong==1:
            print(hang1)
        elif wrong==2:
            print(hang2)
        elif wrong==3:
            print(hang3)
        elif wrong==4:
            print(hang4)
if wrong==5:            
    print()
    print(hang5)
    print("GAME OVER-----WRONG GUESS-----YOU KILLED THE MAN---THE WORD IS",word)
    print(hang5)
else:
    print('CONGRATULATIONS PLAYER-----YOU GUESSED IT RIGHT AND SAVED THE MAN----THE WORD IS',word)         
    print(man)
    
#%%
    
    #%%
n=int(input('enter'))
for i in range(n):
    print('bye')