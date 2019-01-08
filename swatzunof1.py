# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 02:24:44 2019

@author: babaram
"""
#%%%
print("                     WELCOME TO UNO CARD GAME            ")
print(":-INSTRUCTIONS:")
print(":-The game consists of three players")
print(":-Each player has to place a card whose colour matches with the top card or they need to see whether it is of same no,it applies for reverse as well as skip")
print(":-If the player is does not have the required colour then he/she has a option to take cards from the bundle of cards")
print(":-The player who is left with one card wins the game")
print(":-THe skip is card is used to skip the next players turn while the reverse is used to reverse the order of game")
print(":-Wild card is used to change the colour of the ongoing card")
print(":-4draw  or 2 draw means that next player has to take 4 cards or 2 cards respectively" )
print(":-In 4draw or 2draw the nextplayer chance is skipped" )
print(":-THE one who places the card 4draw has got opportunity to change the colour ")
print(":-Shortcuts:green-g,blue-b,yellow-y,red-r,reverse-rev")
import random
uno0=["g0","r0","y0","b0"]
uno1=["g1","r1","y1","b1"]
uno2=["g2","r2","y2","b2"]
uno3=["g3","r3","y3","b3"]
uno4=["g4","r4","y4","b4"]
uno5=["g5","r5","y5","b5"]
uno6=["g6","r6","y6","b6"]
uno7=["g7","r7","y7","b7"]
uno8=["g8","r8","y8","b8"]
uno9=["g9","r9","y9","b9"]
unorev=["grev","rrev","yrev","brev"]
unoskip=["gskip","rskip","yskip","bskip"]
uno4draw=["4draw1","4draw2","4draw3","4draw4"]
uno2draw=["g2draw","y2draw","r2draw","b2draw"]
unowild=['wild1','wild2','wild3','wild4']
uno=[uno0,uno1,uno2,uno3,uno4,uno5,uno6,uno7,uno8,uno9,unorev,unoskip,uno4draw,unowild,uno2draw]
used,player1,player2,player3=[],[],[],[]
green=["g0","g1","g2","g3","g4","g5","g6","g7","g8","g9","gskip","grev","g2draw",unowild]
blue=["b0","b1","b2","b3","b4","b5","b6","b7","b8","b9","brev","b2draw","bskip",unowild]
red=["r0","r1","r2","r3","r4","r5","r6","r7","r8","r9","rrev","r2draw","rskip",unowild]
yellow=["y0","y1","y2","y3","y4","y5","y6","y7","y8","y9","yrev","y2draw","yskip",unowild]
colour,n="",0
for i in range(3):
    for j in range(14):
     lp=random.randrange(0,15)
     cm=random.randrange(0,4)
     if i==0:
      if uno[lp][cm] not in used:
          player1.append(uno[lp][cm])
          used.append(uno[lp][cm])
          if len(player1)==6:
              break
     if i==1:
      if uno[lp][cm] not in used:
          player2.append(uno[lp][cm])
          used.append(uno[lp][cm])
          if len(player2)==6:
              break
     if i==2:
      if uno[lp][cm] not in used:
          player3.append(uno[lp][cm])
          used.append(uno[lp][cm])
          if len(player3)==6:
              break
print("PLAYER1",player1)
print("PLAYER2",player2)
print("PLAYER3",player3)
topcard=""
d=1
c=0
while c!=1:
     lp=random.randrange(0,15)
     cm=random.randrange(0,4)
     if uno[lp][cm] not in used and uno[lp][cm] not in uno4draw and uno[lp][cm] not in unowild:
         topcard=uno[lp][cm]
         used.append(uno[lp][cm])
         c=1
print("                                     TOP CARD       ",topcard)
if topcard in green:
    colour=green
if topcard in blue:
    colour=blue
if topcard in red:
    colour=red
if  topcard in yellow:
    colour=yellow
gg=0
odd=[1,3,5,7,9,11,13,15]
even=[0,2,4,6,8,10,12,14,16]
for i in range(50):
   if d==1:
        print("PLAYER 1 CMON ITS YOUR TURN")
        print(player1)
        print("Do u want to pick up a card")
        ask= str(input("Type yes or no"))
        print()
        if ask=='yes':
           cc=0
           while cc!=1:
            lp=random.randrange(0,15)
            ccm=random.randrange(0,4)
            if uno[lp][cm] not in used:
              player1.append(uno[lp][cm])
              cc=1
              print(uno[lp][cm])
              used.append(uno[lp][cm])
           ak=str(input("Do you want to place the card that you have picked up"))
           print()
           if ak=="yes":
            ask="no"
           if ak=="no":
            if gg in odd :
              d=3
            if gg in even:
              d=2
        if ask=="no":          
            a=str(input("PLACE A CARD"))   
            print()
            if a in colour or a in uno4draw or a in unowild or topcard[1]==a[1]  :
              print("You can proceed")
            else:
               a=str(input("Place different card"))               
            topcard=a
            print('                   TOPCARD                  ',topcard)
            used.append(a)            
            player1.remove(a)            
            if a in unorev:
                gg=gg+1                        
            if a in unowild:
                ll=str(input("The colour changes to"))
                n=1                            
            if gg in odd :
              d=3
            if gg in even:
              d=2
            if a in unoskip:
             if gg in odd :
                d=2
             if gg in even:
                d=3
            if a in uno4draw or a in uno2draw:
                if a in uno4draw:
                    ld=4
                    ll=str(input("The colour changes to"))
                    n=1
                else:
                    ld=2
                if gg in odd :
                             d=2
                             print("PLAYER 3  PICK UP ",ld,"CARDS ")
                             print("PLAYER 3 YOUR CHANCE IS SKIP")
                if gg in even:
                           d=3
                           print("PLAYER 2  PICK UP ",ld," CARDS ")
                           print("PLAYER 2 YOUR CHANCE IS SKIP")
                count=0
                while count<ld:
                            lp=random.randrange(0,15)
                            cm=random.randrange(0,4)
                            if uno[lp][cm] not in used:
                                if d==2:
                                  player3.append(uno[lp][cm])
                                  print(uno[lp][cm])
                                if d==3:
                                  player2.append(uno[lp][cm])
                                  print(uno[lp][cm])
                                count=count+1
           
   if len(player1) ==1:
       print("PLAYER1 WON")
       break      
   if topcard in green or (n==1 and ll=="green"):
    colour=green
   if topcard in blue or(n==1 and ll=="blue"):
    colour=blue
   if topcard in red or(n==1 and ll=="red"):
    colour=red
   if  topcard in yellow or (n==1 and ll=="yellow"):
    colour=yellow    
   n=0
       
   if d==2: 
        print("PLAYER 2 CMON ITS YOUR TURN")
        print(player2)
        print()
        print("DO YOU WANT TO PICK UP A CARD")
        print()
        ask= str(input("TYPE YES OR NO"))
        if ask=='yes':
           cc=0
           while cc!=1:
            lp=random.randrange(0,15)
            ccm=random.randrange(0,4)
            if uno[lp][cm] not in used:
              player2.append(uno[lp][cm])
              cc=1
              print("YOUR CARD",uno[lp][cm])
           used.append(uno[lp][cm])
           ak=str(input("Do you want to place the card that you have picked up"))
           if ak=="yes":
            ask="no"
           if ak=="no":
            
            if gg in odd :
              d=1
            if gg in even:
              d=3     
        if ask=="no":
            b=str(input("PLACE A CARD"))
            print()
            
            if b in colour or b in uno4draw or b in unowild or topcard[1]==b[1] :
              print("you can proceed")
              print()
            else:
               b=str(input("place another card"))
            topcard=b
            used.append(b)
            print('                          TOPCARD             ',topcard)
            print()
            
            player2.remove(b)
            print(player2)
            if b in unorev:
                gg=gg+1
            if gg in odd :
              d=1
            if gg in even:
              d=3               
            if b in unoskip:
             if gg in odd :
                d=3
             if gg in even:
                d=1
            if b in unowild:
                ll=str(input("The colour changes to"))
                n=1
            if b in uno4draw or b in uno2draw:
                
                if b in uno4draw:
                    ld,n=4,1
                    ll=str(input("The colour changes to"))
                else:
                    ld=2
                if gg in odd :
                             d=3
                             print("PLAYER 1 CMON ITS YOUR TURN PICK UP ",ld," CARDS ")
                             print("YOUR CHANCE IS SKIPPED PLAYER1")
                if gg in even:
                           d=1
                           print("PLAYER 3 CMON ITS YOUR TURN PICK UP ",ld," CARDS ")
                           print("YOUR CHANCE IS SKIPPED PLAYER3")
                count=0
                while count<=ld:
                            
                            lp=random.randrange(0,15)
                            cm=random.randrange(0,4)
                            if uno[lp][cm] not in used:
                                if d==1:
                                  player3.append(uno[lp][cm])
                                  print(uno[lp][cm])
                                if d==3:
                                  player1.append(uno[lp][cm])
                                  print(uno[lp][cm])
                                count=count+1
           
   if len(player2) ==1:
       print("PLAYER1 WON")
       break 
   if topcard in green or (n==1 and ll=="green"):
    colour=green
   if topcard in blue or(n==1 and ll=="blue"):
    colour=blue
   if topcard in red or(n==1 and ll=="red"):
    colour=red
   if  topcard in yellow or (n==1 and ll=="yellow"):
    colour=yellow    
   n=0    
 
   if d==3:
        print("PLAYER 3 CMON ITS YOUR TURN")
        print(player3)
        print("Do you want to pick up")
        print()
        ask= str(input("TYPE YES OR NO"))
        if ask=='yes':
          cc=0
          while cc!=1:
             lp=random.randrange(0,15)
             cm=random.randrange(0,4)
             if uno[lp][cm] not in used:
                 
               player3.append(uno[lp][cm])
               used.append(uno[lp][cm])
               cc=1
               print(uno[lp][cm])
          ak=str(input("Do you want to place the card that you have picked up"))
          if ak=="yes":
            ask="no"
          if ak=="no":
            
            if gg in odd :
              d=2
            if gg in even:
              d=1
        
        if ask=="no":
            c=str(input("PLACE A CARD "))
            if c in colour or c in uno4draw or c in unowild or topcard[1]==c[1] :
              print("you can proceed")
            else:
               c=str(input("place another card"))
            topcard=c
            print('                             TOPCARD',topcard)
            player3.remove(c)
            print()
            if c in unorev:
                gg=gg+1
            if gg in odd :
              d=2
            if gg in even:
              d=1
            if c in unoskip:
             if gg in odd :
                d=1
             if gg in even:
                d=2
            if c in unowild:
                ll=str(input("The colour changes to"))
                n=1
            if c in uno4draw or c in uno2draw:
                
                if c in uno4draw:
                    ld,n=4,1
                    ll=str(input("The colour changes to"))
                else:
                    ld=2
                if gg in odd :
                             d=1
                             print("PLAYER 2  PICK UP ",ld," CARDS ")
                             print("PLAYER2 UR CHANCE IS SKIPPED")
                if gg in even:
                           d=2
                           print("PLAYER 1 PICK UP ",ld," CARDS ")
                           print("PLAYER 1 UR CHANCE IS SKIPPED")
                count=0
                while count<=ld:
                            lp=random.randrange(0,15)
                            cm=random.randrange(0,4)
                            print()
                            if uno[lp][cm] not in used:
                                if d==1:
                                  player2.append(uno[lp][cm])
                                  print(uno[lp][cm])
                                if d==2:
                                  player1.append(uno[lp][cm])
                                  print(uno[lp][cm])
                                count=count+1

   if len(player3) ==1:
       print("PLAYER3 WON")
       break
   if topcard in green or (n==1 and ll=="green"):
    colour=green
   if topcard in blue or(n==1 and ll=="blue"):
    colour=blue
   if topcard in red or(n==1 and ll=="red"):
    colour=red
   if  topcard in yellow or (n==1 and ll=="yellow"):
    colour=yellow    
   n=0