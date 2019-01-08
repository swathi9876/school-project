# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 09:27:55 2019

@author: student
"""

#%%
import random
import time

print('If you have more than Rs.100 in the end, you win!!')
print('Ready ?')
time.sleep(2)

num=1
for i in range(5):
    for j in range(5):
        if(num<=9):
            print(num,end='  ')
        else:
            print(num,end=' ')
        num=num+1
    print()

print()
print()
print()


play={1:'The game begins. Rs.0',2:'+ Rs.10',3:'+ Rs.40',4:'- Rs.10',5:'+ Rs.50',6:'Oops! Move back to block 1', 7:'+ Rs.10',8:'- Rs.30',9:'+ Rs.50',
      10:'You get another throw!',11:'+ Rs.50',12:'+ Rs.30',13:'+ Rs.30',14:'- Rs.50',15:'+ Rs.30',16:'+ Rs.30',17:'- Rs.50',18:'+ Rs.50',19:'+ Rs.50',
      20:'Oops! Move back to block 15!',21:'+ Rs.90',22:'+ Rs.90',23:'You get another throw!',24:'+ Rs.60',25:'- Rs.50',26:'You reached the goal'}


ch=input('Enter \'y\' to continue or \'e\' to exit:')

pos,rs=0,0

while ch=='y' and pos<=25:
	
	val=random.randint(1,6)
	print('Rolling...')
	time.sleep(1)
	print('You got ',val)
	
	pos=pos+val
	
	if pos==6:
		print(play[pos])
		pos=1
		
	elif pos==20:
		print(play[pos])
		pos=15
		
	elif pos==10 or pos==23:
		val1=random.randint(1,6)
		pos=pos+val1
		
	elif pos==2 or pos==7:
		print(play[pos])
		rs=rs+10
		
	elif pos==3:
		print(play[pos])
		rs=rs-10
		
	elif pos==5 or pos==9 or pos==11 or pos==18 or pos==19:
		print(play[pos])
		rs=rs+50
		
	elif pos==12 or pos==13 or pos==15 or pos==16:
		print(play[pos])
		rs=rs+30
		
	elif pos==4:
		print(play[pos])
		rs=rs-10
		
	elif pos==8:
		print(play[pos])
		rs=rs-30
		
	elif pos==14 or pos==17:
		print(play[pos])
		rs=rs-50
		
	elif pos==21 or pos==22:
		print(play[pos])
		rs=rs+90
		
	elif pos==24:
		print(play[pos])
		rs=rs+60
		
	elif pos==25:
		print(play[pos])
		rs=rs-50
		
	elif pos>26:
		print('You reached the end')
		break
		
		
	print('You are at block ',pos)
	print('You have Rs.',rs)
	print()
	print()
		
	ch=input('Enter \'y\' to continue:')

if rs>100:
	print()
	print()
	print('You won!! Congrats!')

else:
	print()
	print()
	print('You lose!!.... Better luck next time!')

	print()
	print()

print('Thank you for playing!')
