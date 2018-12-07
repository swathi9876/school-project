# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 11:05:48 2018

@author: student
"""

#python3.6

import random
import matplotlib.pyplot as plt 
import time
print()
print('                       ELECTRONIC ARTS SPORTS           ')
time.sleep(1.5)
n=1
print('                In association with HANAN CORPORATIONS  ')
time.sleep(1.5)
print()
print('                             presents                   ')
time.sleep(1.5)
print()
time.sleep(1.5)
print()
print('              +++++++++  +   +++++++++        +                        ')
print('              +          +   +              +   +                      ') 
print('              +          +   +             +     +                     ') 
print('              +++++++    +   +++++++      +       +                    ') 
print('              +          +   +           +++++++++++                   ') 
print('              +          +   +          +           +                  ')
print('              +          +   +         +             +                 ')
print()
time.sleep(1.5)
print('                        NEYMAR JR  :  THE HISTOIRE                     ')
print()
print()
start=input('                       Press ENTER to start the game             ')
print()
print('                               LOADING                                 ')
print()
print('              ',end='')
print('',end=' ')
for i in range(20):
    n=1
    for i in range(1,23000):
        n=n*i
    n=1
    print('>',end=' ')
print('')
print()
time.sleep(1.5)
print()

print('Rules of game are as follows:')
print('1>The moves of ATTACKER are:')
print('      a>to PASS , press p and then press enter')
print('      b>to CROSS , press c and then press enter')
print('      c>to GIVE THROUGH BALL, press tb and then press enter')
print('      d>to SHOOT , press s and then press enter')
print('      e>to do SKILLS , press skill and then press enter')
print('      f>to SUBSTITUTE , press sub and then press enter')
print('                     NOTE : A player in a particualar position can only be substituted once in the game')
print('      g>if you enter anything except the above commands your player will commit FOUL ')
print('      h>to read the RULES again , press rules and then press enter')
print('      i>to QUIT , press quit and then press enter')
print('1>The moves of DEFENDER are:')
print('      a>to BODY TACKLE , press 2 and then press enter')
print('      a>to SLIDE TACKLE , press 4 and then press enter')
print('      a>to GRAB , press 6 and then press enter')
print('      a>to DASH , press 8 and then press enter')
print()


n=1
for i in range(1,42500):
    n=n*i
n=1
print()
print('                          Barcelona VS PSG                             ')
for i in range(1,42500):
    n=n*i
n=1
print()


x=random.randint(0,1)

time=0

playerpin1='Buffon'
playerpin2=0
playerpin3=0
playerpin4=0
playerpin5=0
playerpin6=0
playerpin7=0
playerpin8=0
playerpin9=0
playerpin10=0
playerpin11=0

playerbin1='Ter Stegnen'
playerbin2=0
playerbin3=0
playerbin4=0
playerbin5=0
playerbin6=0
playerbin7=0
playerbin8=0
playerbin9=0
playerbin10=0
playerbin11=0

subb1=0
subb2=0
subb3=0
subb4=0
subb5=0
subb6=0
subb7=0
subb8=0
subb9=0
subb10=0
subb11=0

subp1=0
subp2=0
subp3=0
subp4=0
subp5=0
subp6=0
subp7=0
subp8=0
subp9=0
subp10=0
subp11=0

s1='Akka'
s2='Around The World'
s3='Elastico'
s4='Neymar Rocket'
s5='Rainbow'
s6='Hocus Pocus'
s7='Matrix'
s8='Juggling'
s9='D-Trec'
s10='No Look Pass'
s11='Roulette Panna'
s12='Tornado Twist'
s13='Nutmeg'
s14='Stepovers'
s15='Whiplash'
s16='Scissor Move'
s17='Lizard'
s18='Heel Flick'
s19='Pro-Mora'
s20='Fake Shot'


q=0
quitme=0

n=0
playerb=10
playerbn='Messi'
playerp=10
playerpn='Neymar'
bar=0
psg=0
bargoal=0
psggoal=0

print('                             Enter Full Time                           ')
t=int(input('>>>'))

if x==0:
    bar=1
    print('               Good Morning, Welcome to Barcelona stadium...       ')
    print()
    print('Messi (10) starts...')
    
else:
    psg=1
    print('                Good Morning, Welcome to Paris stadium..           ')
    print()
    print('Neymar (10) starts....')     
    
while time!=t:
    
    time=time+1
    
    print()
    
    print('           [ Time :',time,'min || PSG:',psggoal,'| BAR:',bargoal,']')    

    ppx1=5
    ppx2=random.randint(10,30)
    ppx3=random.randint(10,30)
    ppx4=random.randint(10,30)
    ppx5=random.randint(10,30)
    ppx6=random.randint(35,55)
    ppx7=random.randint(35,55)
    ppx8=random.randint(35,55)
    ppx9=random.randint(60,85)
    ppx10=random.randint(65,90)
    ppx11=random.randint(60,85)
    
    ppy1=random.randint(40,60)
    ppy2=random.randint(0,15)
    ppy3=random.randint(30,45)
    ppy4=random.randint(55,70)
    ppy5=random.randint(85,100)
    ppy6=random.randint(0,20)
    ppy7=random.randint(40,60)
    ppy8=random.randint(80,100)
    ppy9=random.randint(15,30)
    ppy10=random.randint(45,55)
    ppy11=random.randint(70,85)
    
    pbx1=95
    pbx2=random.randint(70,90)
    pbx3=random.randint(70,90)
    pbx4=random.randint(70,90)
    pbx5=random.randint(70,90)
    pbx6=random.randint(45,65)
    pbx7=random.randint(45,65)
    pbx8=random.randint(45,65)
    pbx9=random.randint(15,40)
    pbx10=random.randint(10,35)
    pbx11=random.randint(15,40)
    
    pby1=random.randint(40,60)
    pby2=random.randint(0,15)
    pby3=random.randint(30,45)
    pby4=random.randint(55,70)
    pby5=random.randint(85,100)
    pby6=random.randint(0,20)
    pby7=random.randint(40,60)
    pby8=random.randint(80,100)
    pby9=random.randint(15,30)
    pby10=random.randint(45,55)
    pby11=random.randint(70,85)

    psgx = [ppx2,ppx3,ppx4,ppx5,ppx6,ppx7,ppx8,ppx9,ppx10,ppx11] 
    psgy = [ppy2,ppy3,ppy4,ppy5,ppy6,ppy7,ppy8,ppy9,ppy10,ppy11] 

    plt.scatter(ppx1,ppy1,color= "purple",marker= "*", s=100)      # GK edit colour

    plt.scatter(psgx, psgy,color= "blue",marker= "*", s=80)  
 
    barx = [pbx2,pbx3,pbx4,pbx5,pbx6,pbx7,pbx8,pbx9,pbx10,pbx11] 
    bary = [pby2,pby3,pby4,pby5,pby6,pby7,pby8,pby9,pby10,pby11]

    plt.scatter(pbx1,pby1,color= "violet",marker= "o", s=100)      # GK edit colour
    plt.scatter(barx, bary, color= "red",marker= "o", s=80)   
    
    if psg==1:
        if playerp==1:
            plt.scatter(ppx1,ppy1, label= "Buffon", color= "black",marker= "*", s=110)
        if playerp==2:
            plt.scatter(ppx2,ppy2, label= "Thiago Silva", color= "black",marker= "*", s=110)
        if playerp==3:
            plt.scatter(ppx3,ppy3, label= "Kimbempe", color= "black",marker= "*", s=110)
        if playerp==4:
            plt.scatter(ppx4,ppy4, label= "Meunier", color= "black",marker= "*", s=110)
        if playerp==5:
            plt.scatter(ppx5,ppy5, label= "Marquinhos", color= "black",marker= "*", s=110)
        if playerp==6:
            plt.scatter(ppx6,ppy6, label= "Verrati", color= "black",marker= "*", s=110)
        if playerp==7:
            plt.scatter(ppx7,ppy7, label= "Dani Alves", color= "black",marker= "*", s=110)
        if playerp==8:
            plt.scatter(ppx8,ppy8, label= "Rabiot", color= "black",marker= "*", s=110)
        if playerp==9:
            plt.scatter(ppx9,ppy9, label= "Cavani", color= "black",marker= "*", s=110)
        if playerp==10:
            plt.scatter(ppx10,ppy10, label= "Neymar JR", color= "black",marker= "*", s=110)
        if playerp==11:
            plt.scatter(ppx11,ppy11, label= "Mbappe", color= "black",marker= "*", s=110)
    
    if bar==1:    
        if playerb==1:
            plt.scatter(pbx1,pby1, label= "Ter Stegnen", color= "black",marker= "o", s=110)
        if playerb==2:
            plt.scatter(pbx2,pby2, label= "Umtiti", color= "black",marker= "o", s=110)
        if playerb==3:
            plt.scatter(pbx3,pby3, label= "Pique", color= "black",marker= "o", s=110)
        if playerb==4:
            plt.scatter(pbx4,pby4, label= "Rakitic", color= "black",marker= "o", s=110)
        if playerb==5:
            plt.scatter(pbx5,pby5, label= "Sergio Busquets", color= "black",marker= "o", s=110)
        if playerb==6:
            plt.scatter(pbx6,pby6, label= "Denis Suarez", color= "black",marker= "o", s=110)
        if playerb==7:
            plt.scatter(pbx7,pby7, label= "Coutinho", color= "black",marker= "o", s=110)
        if playerb==8:
            plt.scatter(pbx8,pby8, label= "Arthur", color= "black",marker= "o", s=110)
        if playerb==9:
            plt.scatter(pbx9,pby9, label= "Suarez", color= "black",marker= "o", s=110)
        if playerb==10:
            plt.scatter(pbx10,pby10, label= "Messi", color= "black",marker= "o", s=110)
        if playerb==11:
            plt.scatter(pbx11,pby11, label= "Dembele", color= "black",marker= "o", s=110)
        
    
    plt.xlabel('Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! Neymar! ') 

    plt.ylabel('Messi! Messi! Messi! Messi! Messi! Messi!') 
 
    plt.title('FIFA PYTHON 18\nPSG(B) VS BARCELONA(R)') 

    plt.legend() 

    plt.show()     
    
    print()

    if quitme==1:
	    break
        
    if quit==2:
        quit=0
        print('Rules of game are as follows:')
        print('1>The moves of ATTACKER are:')
        print('      a>to PASS , press p and then press enter')
        print('      b>to CROSS , press c and then press enter')
        print('      c>to GIVE THROUGH BALL, press tb and then press enter')
        print('      d>to SHOOT , press s and then press enter')
        print('      e>to do SKILLS , press skill and then press enter')
        print('      f>to SUBSTITUTE , press sub and then press enter')
        print('                     NOTE : A player in a particualar position can only be substituted once in the game')
        print('      g>if you enter anything except the above commands your player will commit FOUL ')
        print('      h>to read the RULES again , press rules and then press enter')
        print('      i>to QUIT , press quit and then press enter')
        print('1>The moves of DEFENDER are:')
        print('      a>to BODY TACKLE , press 2 and then press enter')
        print('      a>to SLIDE TACKLE , press 4 and then press enter')
        print('      a>to GRAB , press 6 and then press enter')
        print('      a>to DASH , press 8 and then press enter')
        

    if bar==1:
        playerp=12-playerb
        
        if playerb==1:
            playerbn='Ter Stegnen'
            if subb1!=0:
                playerbn=playerbin1        
        if playerb==2:
            playerbn='Umtiti'
            if subb2!=0:
                playerbn=playerbin2    
        if playerb==3:
            playerbn='Pique'
            if subb3!=0:
                playerbn=playerbin3    
        if playerb==4:
            playerbn='Rakitic'
            if subb4!=0:
                playerbn=playerbin4
        if playerb==5:
            playerbn='Sergio Busquets'
            if subb5!=0:
                playerbn=playerbin5    
        if playerb==6:
            playerbn='Denis Suarez'
            if subb6!=0:
                playerbn=playerbin6    
        if playerb==7:
            playerbn='Coutinho'
            if subb7!=0:
                playerbn=playerbin7    
        if playerb==8:
            playerbn='Arthur'
            if subb8!=0:
                playerbn=playerbin8    
        if playerb==9:
            playerbn='Suarez'
            if subb9!=0:
                playerbn=playerbin9    
        if playerb==10:
            playerbn='Messi'
            if subb10!=0:
                playerbn=playerbin10    
        if playerb==11:
            playerbn='Dembele'
            if subb11!=0:
                playerbn=playerbin11    
        if playerp==1:
            playerpn='Buffon'
            if subp1!=0:
                playerpn=playerpin1
        if playerp==2:
            playerpn='Thiago Silva'
            if subp2!=0:
                playerpn=playerpin2    
        if playerp==3:
            playerpn='Kimbempe'
            if subp3!=0:
                playerpn=playerpin3     
        if playerp==4:
            playerpn='Meunier'
            if subp4!=0:
                playerpn=playerpin4    
        if playerp==5:
            playerpn='Marquinhos'
            if subp5!=0:
                playerpn=playerpin5    
        if playerp==6:
            playerpn='Verrati'
            if subp6!=0:
                playerpn=playerpin6    
        if playerp==7:
            playerpn='Dani Alves'
            if subp7!=0:
                playerpn=playerpin7    
        if playerp==8:
            playerpn='Rabiot'
            if subp8!=0:
                playerpn=playerpin8    
        if playerp==9:
            playerpn='Cavani'
            if subp9!=0:
                playerpn=playerpin9    
        if playerp==10:
            playerpn='Neymar JR'
            if subp10!=0:
                playerpn=playerpin10    
        if playerp==11:
            playerpn='Mbappe'
            if subp11!=0:
                playerpn=playerpin11 
                
        print('How should',playerpn,'(',playerp,') defend ?')
        defense=input('>>>')
        print()
                
        n=0          
        print('What should',playerbn,'(',playerb,') do ?')
        m=input('>>>')

        if m=='skill' or m=='skills' or m=='skl' or m=='9':
            q=random.randint(1,25)
            if q==1:
                print('Commentatory: What a beautiful',s1,'done by',playerbn,'(',playerb,') !!!')
            if q==2:
                print('Commentatory: Look at that',s2,'done by',playerbn,'(',playerb,') !!!')
            if q==3:
                print('Commentatory:OMG!!',s3,'done by',playerbn,'(',playerb,') !!!')
            if q==4:
                print('Commentatory: What a beautiful',s4,'done by',playerbn,'(',playerb,') !!!')
            if q==5:
                print('Commentatory:',s5,'done by',playerbn,'(',playerb,') !!!') 
            if q==6:
                print('Commentatory:The astounding',s6,'by ',playerbn,'(',playerb,') !!!')
            if q==7:
                print('Commentatory: What a beautiful',s7,'done by',playerbn,'(',playerb,') !!!')
            if q==8:
                print('Commentatory: Look at that',s8,'done by',playerbn,'(',playerb,') !!!')
            if q==9:
                print('Commentatory:OMG!!',s9,'done by',playerbn,'(',playerb,') !!!')
            if q==10:
                print('Commentatory: Unbelievable',s10,'done by',playerbn,'(',playerb,') !!!')
            if q==11:
                print('Commentatory: Remarkable',s11,'done by',playerbn,'(',playerb,') !!!') 
            if q==12:
                print('Commentatory:The astounding',s12,'by ',playerbn,'(',playerb,') !!!')
            if q==13:
                print('Commentatory: Ha Ha Ha !!! What a beautiful',s13,'done by',playerbn,'(',playerb,') under',playerpn,'(',playerp,') !!!')
            if q==14:
                print('Commentatory: Look at that',s14,'done by',playerbn,'(',playerb,') !!!')
            if q==15:
                print('Commentatory:OMG!!',s15,'done by',playerbn,'(',playerb,') !!!')
            if q==16:
                print('Commentatory: What a beautiful',s16,'done by',playerbn,'(',playerb,') !!!')
            if q==17:
                print('Commentatory:',s17,'done by',playerbn,'(',playerb,') !!!') 
            if q==18:
                print('Commentatory:The astounding',s18,'by ',playerbn,'(',playerb,') !!!')
            if q==19:
                print('Commentatory: What a beautiful',s19,'done by',playerbn,'(',playerb,') !!!')
            if q==20:
                print('Commentatory: Look at that',s20,'done by',playerbn,'(',playerb,') !!!')   
                if playerb!=11:
                    playerb=playerb+1
                else:
                    playerb=playerb-1
            if q==21:
                psg=1
                bar=0
                print('Commentatory: Ha Ha Ha !!! Skill Failed !! Ball intercepted by',playerpn,'(',playerp,') of PSG !!')     
            if q==22:
                psg=1
                bar=0
                print('Commentatory: OH  MY GOD!!! Skill Failed !! Ball intercepted by',playerpn,'(',playerp,') of PSG !!')
            if q==23:
                psg=1
                bar=0
                print('Commentatory: Ha Ha Ha !!! Skill Failed !! Nice Interception by',playerpn,'(',playerp,') of PSG !!')
            if q==24:
                psg=1
                bar=0
                print('Commentatory:What a Joke !!! Skill Failed !! Ball intercepted by',playerpn,'(',playerp,') of PSG !!') 
            if q==25:
                psg=1
                bar=0
                print('Commentatory: LOOK !!! Skill Failed !! Ball intercepted by',playerpn,'(',playerp,') of PSG !!')
                
        if m=='q' or m=='quit' or m=='esc' or m=='exit' or m=='0':
            quitme=1
            continue                                 
		              
                
        if m=='rules' or m=='rule' or m=='r':
            quit=2
        if m=='p' or m=='2':
            n=1
        if m=='c' or m=='4':
            n=2
        if m=='tb' or m=='8':
            n=3
        if m=='s' or m=='6':
            n=4
        if m=='sub' or m=='7':
            bar=1
            psg=0
            playerbout=input('Enter name of player to be substituted..')
            if playerbout=='ter stegnen' or playerbout=='ter' or playerbout=='stegnen':                
                subb1=1
                playerbin1=input('Enter name of player who goes in...')
                print('Commentatory:',playerbout,'goes out and here comes in',playerbin1)
            if playerbout=='umtiti':                
                subb2=1
                playerbin2=input('Enter name of player who goes in...')
                print('Commentatory:',playerbout,'goes out and here comes in',playerbin2)
            if playerbout=='pique':                
                subb3=1
                playerbin3=input('Enter name of player who goes in...')
                print('Commentatory:',playerbout,'goes out and here comes in',playerbin3)
            if playerbout=='rakitic':                
                subb4=1
                playerbin4=input('Enter name of player who goes in...')
                print('Commentatory:',playerbout,'goes out and here comes in',playerbin4)
            if playerbout=='sergio busquets' or playerbout=='sergio' or playerbout=='busquets':                
                subb5=1
                playerbin5=input('Enter name of player who goes in...')
                print('Commentatory:',playerbout,'goes out and here comes in',playerbin5)
            if playerbout=='denis suarez' or playerbout=='denis':                
                subb6=1
                playerbin6=input('Enter name of player who goes in...')
                print('Commentatory:',playerbout,'goes out and here comes in',playerbin6)
            if playerbout=='coutinho':                
                subb7=1
                playerbin7=input('Enter name of player who goes in...')
                print('Commentatory:',playerbout,'goes out and here comes in',playerbin7)
            if playerbout=='arthur':                
                subb8=1
                playerbin8=input('Enter name of player who goes in...')
                print('Commentatory:',playerbout,'goes out and here comes in',playerbin8)
            if playerbout=='suarez':                
                subb9=1
                playerbin9=input('Enter name of player who goes in...')
                print('Commentatory:',playerbout,'goes out and here comes in',playerbin9)
            if playerbout=='messi' or playerbout=='lionel messi':                
                subb10=1
                playerbin10=input('Enter name of player who goes in...')
                print('Commentatory:',playerbout,'goes out and here comes in',playerbin10)
            if playerbout=='dembele':                
                subb11=1
                playerbin11=input('Enter name of player who goes in...')
                print('Commentatory:',playerbout,'goes out and here comes in',playerbin11)
        
        y=random.randint(1,4)
        if n==1 and y!=1:
            if playerb<11:
                playerb=playerb+1
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11
                print('Commentatory: Pass to player',playerbn,'succesful !! Nice Pass man!!')
            else:
                playerb=playerb-1
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11
                print('Commentatory: Pass to player',playerbn,'succesful !!')
        
        if n==2 and y!=2:
            if playerb<10:
                playerb=playerb+2
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11
                print('Commentatory: Cross to player',playerbn,'succesful !! WOW! What a trap!! ')
            else:
                playerb=playerb-2
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11
                print('Commentatory: Cross to player',playerbn,'succesful !!')
                
        if n==3 and y!=3:
            if playerb<9:
                playerb=playerb+3
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11
                print('Commentatory: Through ball to player',playerbn,'succesful !! what ball man !! WOW!!')
            else:
                playerb=playerb-3
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11
                print('Commentatory: Through ball to player',playerbn,'succesful !!')
                
        if n==4 and y==4:
            if playerb>8:
                bargoal=bargoal+1
                bar=0
                psg=1
                playerp=10
                print('Commentatory:',playerbn,'scores!!! Goooooal!! Awesome!!! BARCELONA',bargoal,'and PSG',psggoal)
                print('Commentatory: Now Neymar starts...' )
                print()        
            if playerb<=8:
                psg=1
                bar=0
                playerp=1                
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                print('Commentatory:',playerpin1,'saves it')
                
        if n==4 and y!=4:
            bar=0
            psg=1
            playerp=1
            if playerp==1:
                playerpn='Buffon'
                if subp1!=0:
                    playerpn=playerpin1
            print('Commentatory:',playerpin1,'saves it')
            
        if n!=4 and n==y :
                bar=0
                psg=1
                playerp=12-playerb
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11        
                print('Commentatory: Ball intercepted by player',playerpn,'of PSG')
        
        if m!='s' and m!='c' and m!='tb' and m!='p' and m!='sub' and m!='skill' and m!='skills' and m!='0' and m!='2' and m!='4' and m!='6' and m!='7' and m!='8' and m!='9':
            print('Foul!! Freekick awarded to PSG')
            freekick=input('Enter direction of shoot ie. l or r')
            g=random.randint(0,1)
            if freekick=='l' and g==0:
                bargoal=bargoal+1
                bar=0
                psg=1
                playerp=10
                print('Commentatory:',playerbn,'scores!!! Goooooal!! Awesome!!! BARCELONA',bargoal,'and PSG',psggoal)
                print('Commentatory: Now Neymar starts...' )
                print()
            if freekick=='r' and g==1:
                bargoal=bargoal+1
                bar=0
                psg=1
                playerp=10
                print('Commentatory:',playerbn,'scores!!! Goooooal!! Awesome!!! BARCELONA',bargoal,'and PSG',psggoal)
                print('Commentatory: Now Neymar starts...' )
                print()
            if freekick=='l' and g==1:
                bar=0
                psg=1
                playerp=1
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                print('Commentatory:',playerpin1,'saves it')
            if freekick=='r' and g==0:
                bar=0
                psg=1
                playerp=1
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                print('Commentatory:',playerpin1,'saves it')
            
            
    elif psg==1:
        playerb=12-playerp
        
        if playerb==1:
            playerbn='Ter Stegnen'
            if subb1!=0:
                playerbn=playerbin1        
        if playerb==2:
            playerbn='Umtiti'
            if subb2!=0:
                playerbn=playerbin2    
        if playerb==3:
            playerbn='Pique'
            if subb3!=0:
                playerbn=playerbin3    
        if playerb==4:
            playerbn='Rakitic'
            if subb4!=0:
                playerbn=playerbin4
        if playerb==5:
            playerbn='Sergio Busquets'
            if subb5!=0:
                playerbn=playerbin5    
        if playerb==6:
            playerbn='Denis Suarez'
            if subb6!=0:
                playerbn=playerbin6    
        if playerb==7:
            playerbn='Coutinho'
            if subb7!=0:
                playerbn=playerbin7    
        if playerb==8:
            playerbn='Arthur'
            if subb8!=0:
                playerbn=playerbin8    
        if playerb==9:
            playerbn='Suarez'
            if subb9!=0:
                playerbn=playerbin9    
        if playerb==10:
            playerbn='Messi'
            if subb10!=0:
                playerbn=playerbin10    
        if playerb==11:
            playerbn='Dembele'
            if subb11!=0:
                playerbn=playerbin11    
        if playerp==1:
            playerpn='Buffon'
            if subp1!=0:
                playerpn=playerpin1
        if playerp==2:
            playerpn='Thiago Silva'
            if subp2!=0:
                playerpn=playerpin2    
        if playerp==3:
            playerpn='Kimbempe'
            if subp3!=0:
                playerpn=playerpin3     
        if playerp==4:
            playerpn='Meunier'
            if subp4!=0:
                playerpn=playerpin4    
        if playerp==5:
            playerpn='Marquinhos'
            if subp5!=0:
                playerpn=playerpin5    
        if playerp==6:
            playerpn='Verrati'
            if subp6!=0:
                playerpn=playerpin6    
        if playerp==7:
            playerpn='Dani Alves'
            if subp7!=0:
                playerpn=playerpin7    
        if playerp==8:
            playerpn='Rabiot'
            if subp8!=0:
                playerpn=playerpin8    
        if playerp==9:
            playerpn='Cavani'
            if subp9!=0:
                playerpn=playerpin9    
        if playerp==10:
            playerpn='Neymar JR'
            if subp10!=0:
                playerpn=playerpin10    
        if playerp==11:
            playerpn='Mbappe'
            if subp11!=0:
                playerpn=playerpin11 
                
        print('How should',playerbn,'(',playerb,') defend ?')
        defense=input('>>>')
        print()
        
        n=0        
        print('What should',playerpn,'(',playerp,') do ?')
        m=input('>>>')
        
        if m=='skill' or m=='skills' or m=='skl' or m=='skls' or m=='9':
            q=random.randint(1,25)
            if q==1:
                print('Commentatory: What a beautiful',s1,'done by',playerpn,'(',playerp,') !!!')
            if q==2:
                print('Commentatory: Look at that',s2,'done by',playerpn,'(',playerp,') !!!')
            if q==3:
                print('Commentatory:OMG!!',s3,'done by',playerpn,'(',playerp,') !!!')
            if q==4:
                print('Commentatory: What a beautiful',s4,'done by',playerpn,'(',playerp,') !!!')
            if q==5:
                print('Commentatory:',s5,'done by',playerpn,'(',playerp,') !!!') 
            if q==6:
                print('Commentatory:The astounding',s6,'by ',playerpn,'(',playerp,') !!!')
            if q==7:
                print('Commentatory: What a beautiful',s7,'done by',playerpn,'(',playerp,') !!!')
            if q==8:
                print('Commentatory: Look at that',s8,'done by',playerpn,'(',playerp,') !!!')
            if q==9:
                print('Commentatory:OMG!!',s9,'done by',playerpn,'(',playerp,') !!!')
            if q==10:
                print('Commentatory: Unbelievable',s10,'done by',playerpn,'(',playerp,') !!!')
            if q==11:
                print('Commentatory: Remarkable',s11,'done by',playerpn,'(',playerp,') !!!') 
            if q==12:
                print('Commentatory:The astounding',s12,'by ',playerpn,'(',playerp,') !!!')
            if q==13:
                print('Commentatory: Ha Ha Ha !!! What a beautiful',s13,'done by',playerpn,'(',playerp,') under',playerbn,'(',playerb,') !!!')
            if q==14:
                print('Commentatory: Look at that',s14,'done by',playerpn,'(',playerp,') !!!')
            if q==15:
                print('Commentatory:OMG!!',s15,'done by',playerpn,'(',playerp,') !!!')
            if q==16:
                print('Commentatory: What a beautiful',s16,'done by',playerpn,'(',playerp,') !!!')
            if q==17:
                print('Commentatory:',s17,'done by',playerpn,'(',playerp,') !!!') 
            if q==18:
                print('Commentatory:The astounding',s18,'by ',playerpn,'(',playerp,') !!!')
            if q==19:
                print('Commentatory: What a beautiful',s19,'done by',playerpn,'(',playerp,') !!!')
            if q==20:
                print('Commentatory: Look at that',s20,'done by',playerpn,'(',playerp,') !!!')
                if playerp!=11:
                    playerp=playerp+1
                else:
                    playerp=playerp-1
            if q==21:
                psg=0
                bar=1
                print('Commentatory: Ha Ha Ha !!! Skill Failed !! Ball intercepted by',playerbn,'(',playerb,') of Barcelona !!')     
            if q==22:
                psg=0
                bar=1
                print('Commentatory: OH  MY GOD!!! Skill Failed !! Ball intercepted by',playerbn,'(',playerb,') of Barcelona !!')
            if q==23:
                psg=0
                bar=1
                print('Commentatory: Ha Ha Ha !!! Skill Failed !! Nice Interception by',playerbn,'(',playerb,') of Barcelona !!')
            if q==24:
                psg=0
                bar=1
                print('Commentatory:What a Joke !!! Skill Failed !! Ball intercepted by',playerbn,'(',playerb,') of Barcelona !!') 
            if q==25:
                psg=0
                bar=1
                print('Commentatory: LOOK !!! Skill Failed !! Ball intercepted by',playerbn,'(',playerb,') of Barcelona !!')
        
        if m=='q' or m=='quit' or m=='esc' or m=='exit' or m=='0':
            quitme=1
            continue                      
        
        if m=='rules' or m=='rule' or m=='r':
            quit=0
            print('Rules of game are as follows:')
            print('1>The moves of ATTACKER are:')
            print('      a>to PASS , press p and then press enter')
            print('      b>to CROSS , press c and then press enter')
            print('      c>to GIVE THROUGH BALL, press tb and then press enter')
            print('      d>to SHOOT , press s and then press enter')
            print('      e>to do SKILLS , press skill and then press enter')
            print('      f>to SUBSTITUTE , press sub and then press enter')
            print('                     NOTE : A player in a particualar position can only be substituted once in the game')
            print('      g>if you enter anything except the above commands your player will commit FOUL ')
            print('      h>to read the RULES again , press rules and then press enter')
            print('      i>to QUIT , press quit and then press enter')
            print('1>The moves of DEFENDER are:')
            print('      a>to BODY TACKLE , press 2 and then press enter')
            print('      a>to SLIDE TACKLE , press 4 and then press enter')
            print('      a>to GRAB , press 6 and then press enter')
            print('      a>to DASH , press 8 and then press enter')
            
        if m=='p' or m=='2':
            n=1
        if m=='c' or m=='4':
            n=2
        if m=='tb' or m=='8':
            n=3
        if m=='s' or m=='6':
            n=4
        if m=='sub' or m=='7':
            bar=0
            psg=1
            playerpout=input('Enter name of player to be substituted..')
            if playerpout=='buffon':                
                subp1=1
                playerpin1=input('Enter name of player who goes in...')
                print('Commentatory:',playerpout,'goes out and here comes in',playerpin1)
            if playerpout=='thiago silva' or playerpout=='silva' or playerpout=='thiago':                
                subp2=1
                playerpin2=input('Enter name of player who goes in...')
                print('Commentatory:',playerpout,'goes out and here comes in',playerpin2)
            if playerpout=='kimbempe':                
                subp3=1
                playerpin3=input('Enter name of player who goes in...')
                print('Commentatory:',playerpout,'goes out and here comes in',playerpin3)
            if playerpout=='meunier':                
                subp4=1
                playerpin4=input('Enter name of player who goes in...')
                print('Commentatory:',playerpout,'goes out and here comes in',playerpin4)
            if playerpout=='marquinhos':                
                subp5=1
                playerpin5=input('Enter name of player who goes in...')
                print('Commentatory:',playerpout,'goes out and here comes in',playerpin5)
            if playerpout=='verrati':        
                subp6=1
                playerpin6=input('Enter name of player who goes in...')
                print('Commentatory:',playerpout,'goes out and here comes in',playerpin6)
            if playerpout=='dani alves' or playerpout=='alves' or playerpout=='dani':                
                subp7=1
                playerpin7=input('Enter name of player who goes in...')
                print('Commentatory:',playerpout,'goes out and here comes in',playerpin7)
            if playerpout=='rabiot':                
                subp8=1
                playerpin8=input('Enter name of player who goes in...')
                print('Commentatory:',playerpout,'goes out and here comes in',playerpin8)
            if playerpout=='cavani':                
                subp9=1
                playerpin9=input('Enter name of player who goes in...')
                print('Commentatory:',playerpout,'goes out and here comes in',playerpin9)
            if playerpout=='neymar' or playerpout=='neymar jr':                
                subp10=1
                playerpin10=input('Enter name of player who goes in...')
                print('Commentatory:',playerpout,'goes out and here comes in',playerpin10)
            if playerpout=='mbappe':                
                subp11=1  
                playerpin11=input('Enter name of player who goes in...')
                print('Commentatory:',playerpout,'goes out and here comes in',playerpin11)
            
        y=random.randint(1,4)
        if n==1 and y!=1:
            if playerp<11:
                playerp=playerp+1
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11
                print('Commentatory: Pass to player',playerpn,'succesful !! Nice Pass man!!')
            else:
                playerp=playerp-1
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11
                print('Commentatory: Pass to player',playerpn,'succesful !!')
        
        if n==2 and y!=2:
            if playerp<10:
                playerp=playerp+2
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11
                print('Commentatory: Cross to player',playerpn,'succesful !! WOW! What a trap!! ')
            else:
                playerp=playerp-2
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11
                print('Commentatory: Cross to player',playerpn,'succesful !!')
                
        if n==3 and y!=3:
            if playerp<9:
                playerp=playerp+3
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11
                print('Commentatory: Through ball to player',playerpn,'succesful !! what ball man !! WOW!!')
            else:
                playerp=playerp-3
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11
                print('Commentatory: Through ball to player',playerpn,'succesful !!')
                
        if n==4 and y==4:
            if playerp>8:
                psggoal=psggoal+1
                bar=1
                psg=0
                playerb=10
                print('Commentatory:',playerpn,'scores!!! Goooooal!! Awesome!!! BARCELONA',bargoal,'and PSG',psggoal)
                print('Commentatory: Now Messi starts...')
                print()
            if playerp<=8:
                psg=0
                bar=1
                playerb=1
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1 
                print('Commentatory:',playerbin1,'saves it')
        
        if n==4 and y!=4:
            bar=1
            psg=0
            playerb=1
            if playerb==1:
                playerbn='Ter Stegnen'
                if subb1!=0:
                    playerbn=playerbin1 
            print('Commentatory:',playerbin1,'saves it')
        
        if n!=4 and n==y :
                bar=1
                psg=0
                playerb=12-playerp
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1        
                if playerb==2:
                    playerbn='Umtiti'
                    if subb2!=0:
                        playerbn=playerbin2    
                if playerb==3:
                    playerbn='Pique'
                    if subb3!=0:
                        playerbn=playerbin3    
                if playerb==4:
                    playerbn='Rakitic'
                    if subb4!=0:
                        playerbn=playerbin4
                if playerb==5:
                    playerbn='Sergio Busquets'
                    if subb5!=0:
                        playerbn=playerbin5    
                if playerb==6:
                    playerbn='Denis Suarez'
                    if subb6!=0:
                        playerbn=playerbin6    
                if playerb==7:
                    playerbn='Coutinho'
                    if subb7!=0:
                        playerbn=playerbin7    
                if playerb==8:
                    playerbn='Arthur'
                    if subb8!=0:
                        playerbn=playerbin8    
                if playerb==9:
                    playerbn='Suarez'
                    if subb9!=0:
                        playerbn=playerbin9    
                if playerb==10:
                    playerbn='Messi'
                    if subb10!=0:
                        playerbn=playerbin10    
                if playerb==11:
                    playerbn='Dembele'
                    if subb11!=0:
                        playerbn=playerbin11    
                if playerp==1:
                    playerpn='Buffon'
                    if subp1!=0:
                        playerpn=playerpin1
                if playerp==2:
                    playerpn='Thiago Silva'
                    if subp2!=0:
                        playerpn=playerpin2    
                if playerp==3:
                    playerpn='Kimbempe'
                    if subp3!=0:
                        playerpn=playerpin3     
                if playerp==4:
                    playerpn='Meunier'
                    if subp4!=0:
                        playerpn=playerpin4    
                if playerp==5:
                    playerpn='Marquinhos'
                    if subp5!=0:
                        playerpn=playerpin5    
                if playerp==6:
                    playerpn='Verrati'
                    if subp6!=0:
                        playerpn=playerpin6    
                if playerp==7:
                    playerpn='Dani Alves'
                    if subp7!=0:
                        playerpn=playerpin7    
                if playerp==8:
                    playerpn='Rabiot'
                    if subp8!=0:
                        playerpn=playerpin8    
                if playerp==9:
                    playerpn='Cavani'
                    if subp9!=0:
                        playerpn=playerpin9    
                if playerp==10:
                    playerpn='Neymar JR'
                    if subp10!=0:
                        playerpn=playerpin10    
                if playerp==11:
                    playerpn='Mbappe'
                    if subp11!=0:
                        playerpn=playerpin11
                print('Commentatory: Ball intercepted by player',playerbn,'of Barcelona')
        
        if m!='s' and m!='c' and m!='tb' and m!='p' and m!='sub' and m!='skill' and m!='skills' and m!='0' and m!='2' and m!='4' and m!='6' and m!='7' and m!='8' and m!='9':
            print('Foul!! Freekick awarded to Barcelona')
            freekick=input('Enter direction of shoot ie. l or r')
            g=random.randint(0,1)
            if freekick=='l' and g==0:
                psggoal=psggoal+1
                bar=1
                psg=0
                playerb=10
                print('Commentatory:',playerpn,'scores!!! Goooooal!! Awesome!!! BARCELONA',bargoal,'and PSG',psggoal)
                print('Commentatory: Now Messi starts...')
                print()
            if freekick=='r' and g==1:
                psggoal=psggoal+1
                bar=1
                psg=0
                playerb=10
                print('Commentatory:',playerpn,'scores!!! Goooooal!! Awesome!!! BARCELONA',bargoal,'and PSG',psggoal)
                print('Commentatory: Now Messi starts...')
                print()
            if freekick=='l' and g==1:
                bar=1
                psg=0
                playerb=1
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1 
                print('Commentatory:',playerbin1,'saves it')
            if freekick=='r' and g==0:
                bar=1
                psg=0
                playerb=1
                if playerb==1:
                    playerbn='Ter Stegnen'
                    if subb1!=0:
                        playerbn=playerbin1 
                print('Commentatory:',playerbin1,'saves it')

                
else:
    print('Commentatory: Full Time! || Barcelona :',bargoal,'| PSG :',psggoal,'||')

print()
print('Hope you enjoyed the game')
print('Thank you')
rating=input('Pls give feedback for this game...')
print()
print('Thank you for your feedback !!!!')
print('          - Hanan Basheer')
print('            CEO , Hanu Corporations 2018')
print()
print(' News: FIFA Python 2019 coming soon in your nearby stores.....')
stop=input('Prebook NOW...')

time.sleep(100)