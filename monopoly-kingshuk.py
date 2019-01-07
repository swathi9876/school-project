# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 00:18:11 2019

@author: kingshuk02
"""

#%%
import random
import time

positions=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("    |\    /|    _____    |\   |    _____     ____     _____                  ")
print("    | \  / |   |     |   | \  |   |     |   |    |   |     |  |      \   /    ")
print("    |  \/  |   |     |   |  \ |   |     |   |____|   |     |  |       \ /   ")
print("    |      |   |_____|   |   \|   |_____|   |        |_____|  |_____   |          ")    
print()
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print()
print()
print()
print("        1) Start Game")
print("        2) How to Play           ")
print("        3) Quit game" )    
print()  
print()    
print()  
money=1500
houses=0
position=0
totaldouble=0
doubles=True
free=0
rail=0
a1=0
a2=0
a3=0
a4=0
a5=0
a6=0
a7=0
a8=0
a9=0
a10=0
a11=0
a12=0
a13=0
a14=0
a15=0
a16=0
a17=0
a18=0
a19=0
a20=0
a21=0
a22=0
a23=0
a24=0
a25=0
a26=0
a27=0
a28=0
a=int(input("enter your choice 1,2 or 3: "))
if a==1:
    
    print("  ______________________________________________________________________________________________________________")
    print(" |   Go     | Regent  |  Oxford |         |  Bond   |Liverpool|         |  Park   | Luxury  |   May   |         |")
    print(" |   To     | Street  |  Street |Community|  Street | Street  | Chance  |  Lane   |  Tax    |   Fair  |   Go    |")
    print(" |   Jail   |         |         |  Chest  |         | Station |         |         |         |         |         |")
    print(" |   ",positions[30],"   |   ",positions[31],"  |   ",positions[32],"  |   ",positions[33],"  |   ",positions[34],"  |   ",positions[35],"  |   ",positions[36],"  |   ",positions[37],"  |   ",positions[38],"  |   ",positions[39],"  |   ",positions[0],"   |")
    print(" |__________|_________|_________|_________|_________|_________|_________|_________|_________|_________|_________|")
    print(" |Piccadilly|                                                                                         | Old     |")
    print(" |          |                                                                                         | Kent    |") 
    print(" |          |                                                                                         | Road    |")
    print(" |   ",positions[29],"   |                                                                                         |   ",positions[1],"   |")
    print(" |__________|                                                                                         |_________|")
    print(" |  Water   |                                                                                         |         |")
    print(" |  Works   |                                                                                         |Community|")
    print(" |          |                                                                                         |  Chest  |")
    print(" |   ",positions[28],"   |                                                                                         |   ",positions[2],"   |")
    print(" |__________|                                                                                         |_________|")
    print(" | Coventy  |                                                                                         |         |")
    print(" | Street   |                                                                                         | White   |")
    print(" |          |                                                                                         | Chappel |")
    print(" |   ",positions[27],"   |                                                                                         | Road    |")
    print(" |__________|                                                                                         |___",positions[3],"___|")
    print(" |Leicester |                                                                                         | Income  |")
    print(" | Square   |                                                                                         |  Tax    |")
    print(" |          |                                                                                         |         |")
    print(" |   ",positions[26],"   |                                                                                         |   ",positions[4],"   |")      
    print(" |__________|                                                                                         |_________|")
    print(" |Fenchurch |                                                                                         | King's  |")
    print(" | Station  |                                                                                         | Cross   |")
    print(" |          |                                                                                         | Station |")
    print(" |   ",positions[25],"   |                                                                                         |   ",positions[5],"   |")      
    print(" |__________|                                                                                         |_________|")
    print(" |Trafalgar |                                                                                         |         |")
    print(" |  Square  |                                                                                         | Chance  |") 
    print(" |          |                                                                                         |         |")
    print(" |   ",positions[24],"   |                                                                                         |   ",positions[6],"   |")
    print(" |__________|                                                                                         |_________|")
    print(" |  Fleet   |                                                                                         | The     |")
    print(" |  Street  |                                                                                         | Angel,  |")
    print(" |          |                                                                                         |Islington|")
    print(" |   ",positions[23],"   |                                                                                         |   ",positions[7],"   |")
    print(" |__________|                                                                                         |_________|")
    print(" |          |                                                                                         | Euston  |")
    print(" |  Chance  |                                                                                         |  Road   |")
    print(" |          |                                                                                         |         |")
    print(" |   ",positions[22],"   |                                                                                         |   ",positions[8],"   |")
    print(" |__________|                                                                                         |_________|")
    print(" |          |                                                                                         | Penton  |")
    print(" |  Strand  |                                                                                         |  Ville  |")
    print(" |          |                                                                                         |  Road   |")
    print(" |   ",positions[21],"   |                                                                                         |   ",positions[9],"   |")
    print(" |__________|_________________________________________________________________________________________|_________|")
    print(" |   Just   |  Vine   |  Great  |         |  Bow    | Maryle  | North   |  White  | Elictric|  Pall   |         |")
    print(" |  Parking |  Street |  Marl   |Community| Street  |  Bone   | Humber  |  Hall   | Company |  Mall   |  Jail   |")
    print(" |          |         |  street |  Chest  |         | Station | Land    |         |         |         |         |")
    print(" |   ",positions[20],"   |   ",positions[19],"  |   ",positions[18],"  |   ",positions[17],"  |   ",positions[16],"  |   ",positions[15],"  |   ",positions[14],"  |   ",positions[13],"  |   ",positions[12],"  |   ",positions[11],"  |   ",positions[10],"  |")
    print(" |__________|_________|_________|_________|_________|_________|_________|_________|_________|_________|_________|")
    sprite=input("enter any character you  want to play with from !,@,#,$,%,* :")
    gameon=True
    while gameon==True:
            dice1=random.randrange(1,6)
            dice2=random.randrange(1,6)
            print("you rolled a",dice1,"and",dice2)
            if position<=39:
                    position=position+dice1+dice2
            if position>39:
                position=position-40
                money+=200
                print(position)

    
            if dice1==dice2:
                    totaldouble=totaldouble+1
        
            else:
                    totaldouble=0
            if totaldouble==3:
                    print("you throwed doubles three times in a row soo you go to jail")
                    money=money-50
                    print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)
            if position==0:
                print("you landed on go")
                money=money+200
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)
                time.sleep(2)
            if position==2 or position==17 or position==33:
                print("you landed on Community Chest")
                chestcards=random.choice(["Advance to Go (Collect 200)","Bank error in your favor—Collect 200","Doctor's fee—Pay 50","From sale of stock you get £50","Get Out of Jail Free","Go to Jail–Go directly to jail–Do not pass Go–Do not collect £200","Holiday Fund matures—Receive £100","Income tax refund–Collect £20","It is your birthday—Collect £10","Life insurance matures–Collect £100","Pay hospital fees of £100","Pay school fees of £150","Receive £25 consultancy fee","You have won second prize in a beauty contest–Collect £10","You inherit £100"])
                print("you recieved the", chestcards,"card in community chest")
                if chestcards=="Advance to Go (Collect £200)":
                    money=money+200
                    position=0
                elif chestcards=="Bank error in your favor—Collect £200":
                    money=money+200
                    
                elif chestcards=="Doctor's fee—Pay £50":
                    money=money-50
                    
                elif chestcards=="From sale of stock you get £50":
                    money=money+50
                    
                elif chestcards=="Get Out of Jail Free":
                    free=free+1
                    
                elif chestcards=="Go to Jail–Go directly to jail–Do not pass Go–Do not collect £200":
                    position=10
                    money=money-50
                elif chestcards=="Holiday Fund matures—Receive £100":
                    money=money+100
                    
                elif chestcards=="Income tax refund–Collect £20":
                    money=money+20
                    
                elif chestcards=="It is your birthday—Collect £10":
                    money=money+10
                    position=0
                elif chestcards=="Life insurance matures–Collect £100":
                    money=money+100
                    
                elif chestcards=="Pay hospital fees of £100":
                    money=money-100
                    
                elif chestcards=="Pay school fees of £150":
                    money=money-150
                    
                elif chestcards=="Receive £25 consultancy fee":
                    money=money+25
                    
                elif chestcards=="You have won second prize in a beauty contest–Collect £10":
                    money=money+10
                    
                elif chestcards=="You inherit £100":
                    money=money+100
                    
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)
                time.sleep(2)
            if position==6 or position==22 or position==36:
                print("you landed on Chance")
                chancecards=random.choice([
                        "Advance to 'Go'"
                        ,"Go to jail. Move directly to jail. Do not pass 'Go'. Do not collect £200"
                        ,"Advance to Pall Mall. If you pass 'Go' collection £200"
                        ,"Take a trip to Marylebone Station and if you pass 'Go' collect £200"
                        ,"Advance to Trafalgar Square. If you pass 'Go' collect £200"
                        ,"Advance to Mayfair"
                        ,"Go back three spaces"
                        ,"Pay school fees of £150"
                        ,"Drunk in charge fine £20"
                        ,"Speeding fine £15"
                        ,"Your building loan matures. Receive £150"
                        ,"You have won a crossword competition. Collect £100"
                        ,"Get out of jail free. This card may be kept until needed or sold"])
                print("you recieved",chancecards,"card")
                if chancecards=="Advance to 'Go'":
                    money=money+200
                    position=0
                elif chancecards=="Go to jail. Move directly to jail. Do not pass 'Go'. Do not collect £200":
                    position=10
                    money=money-50
                    
                elif chancecards=="Advance to Pall Mall. If you pass 'Go' collection £200":
                    if position>11:
                        money=money+200
                        position=11
                    else:
                        position=11
                    
                elif chancecards=="Take a trip to Marylebone Station and if you pass 'Go' collect £200":
                    if position>15:
                        money=money+200
                        position=15
                    else:
                        position=15
                elif chancecards=="Advance to Trafalgar Square. If you pass 'Go' collect £200":
                    if position>24:
                        money=money+200
                        position=24
                    else:
                        position=24
                    
                elif chancecards=="Advance to Mayfair":
                    position=39
                elif chancecards=="Go back three spaces":
                    position=position-3                   
                elif chancecards=="Pay school fees of £150":
                    money=money-150
                    
                elif chancecards=="Drunk in charge fine £20":
                    money=money-20
                    
                elif chancecards=="Speeding fine £15":
                    money=money-15
                    
                elif chancecards=="Your building loan matures. Receive £150":
                    money=money+150
                    
                elif chancecards=="You have won a crossword competition. Collect £100":
                    money=money+100
                    
                elif chancecards=="Get out of jail free. This card may be kept until needed or sold":
                    free=free+1
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)    
                time.sleep(2)
            if position==1:
                print("you landed on Old Kent Road")
                if a1==0:
                    buy=int(input("press 1 to buy a house or press 0 to continue"))
                    if buy==1:
                            money-=10
                            houses+=1
                            a1+=1
                    else:
                            pass
                    
                elif a1>0:
                   print("you already own a house here")
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)
                time.sleep(2)
            if position==3:
                
                print("you landed on White chappel Road")
                if a2==0:
                    buy=int(input("press 1 to buy a house or press 0 to continue"))
                    if buy==1:
                        money-=20
                        houses+=1
                        a2+=1
                    else:
                        pass
                elif a2>0:
                    print("you already own a house here")
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)
                time.sleep(2)            
            if position==4:
                
                print("you landed on income tax")
                money=money-200
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)
                time.sleep(2)
            if position==5  :
                
                print("you landed on King's cross station")
                if a3==0:
                    buy=int(input("press 1 to buy it or press 0 to continue"))
                    if buy==1:
                            money-=25
                            rail+=1
                            a3+=1
                    else:
                            pass
                elif a3>0:
                    print("you already own a house here")
                
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)
                time.sleep(2)
            if position==7:
                print("you landed on The angel")
                if a4==0:
                    buy=int(input("press 1 to buy a house or press 0 to continue"))
                    if buy==1:
                        money-=30
                        houses+=1
                        a4+=1
                    else:
                        pass
                elif a4>0:
                    print("you already own a house here")
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)   
                time.sleep(2)
            if position==8:
                print("you landed on Euston Road")
                if a5==0:
                    buy=int(input("press 1 to buy it or press 0 to continue"))
                    if buy==1:
                        money-=30
                        rail+=1
                        a5+=1
                    else:
                        pass
                elif a5>0:
                    print("you already own a house here")
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)
                time.sleep(2) 
            if position==9:
                print("you landed on Pentonville Road")
                if a6==0:
                    buy=int(input("press 1 to buy it or press 0 to continue"))
                    if buy==1:
                        money-=40
                        houses+=1
                        a6+=1
                    else:
                        pass
                elif a6>0:
                    print("you already own a house here")
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)    
                time.sleep(2)
            if position==10:
                print("you landed on Jail ")
                time.sleep(2)    
            if position==11:
                print("you landed on Pall Mall")
                if a7==0:
                    buy=int(input("press 1 to buy it or press 0 to continue"))
                    if buy==1:
                        money-=50
                        houses+=1
                        a7+=1
                    else:
                        pass
                elif a7>0:
                    print("you already own a house here")
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)
                time.sleep(2)
            if position==12:
                print("you landed on Electric Company")
                if a8==0:
                    buy=int(input("press 1 to buy it or press 0 to continue"))
                    if buy==1:
                        money=money-(4*(dice1+dice2))
                        rail+=1
                        a8+=1
                    else:
                        pass
                elif a8>0:
                    print("you already own a house here")
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)   
                time.sleep(2)
            if position==13:
                print("you landed on White Hall")
                if a9==0:
                    buy=int(input("press 1 to buy it or press 0 to continue"))
                    if buy==1:
                        money-=50
                        houses+=1
                        a9+=1
                    else:
                        pass
                elif a9>0:
                    print("you already own a house here")
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)    
                time.sleep(2)
            if position==14:
                print("you landed on Nothhumber Land")
                if a10==0:
                    buy=int(input("press 1 to buy it or press 0 to continue"))
                    if buy==1:
                        money-=55
                        houses+=1
                        a10+=1
                    else:
                        pass
                elif a10>0:
                    print("you already own a house here")
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)   
                time.sleep(2) 
            if position==15:
                print("you landed on Marylebone Station")
                if a11==0:
                    buy=int(input("press 1 to buy it or press 0 to continue"))
                    if buy==1:
                        money-=60
                        rail+=1
                        a11+=0
                    else:
                        pass
                elif a11>0:
                    print("you already own a house here")
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)
                time.sleep(2)
            if position==16:
                print("you landed on Bow Street")
                if a12==0:
                    buy=int(input("press 1 to buy it or press 0 to continue"))
                    if buy==1:
                        money-=55
                        houses+=1
                        a12+=1
                    else:
                        pass
                elif a12>0:
                    print("you already own a house here")
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)    
                time.sleep(2)
            if position==18:
                print("you landed on Great Marl Street")
                if a13==0:
                    buy=int(input("press 1 to buy it or press 0 to continue"))
                    if buy==1:
                        money-=60
                        houses+=1
                        a13+=1
                    else:
                        pass
                elif a13>0:
                    print("you already own a house here")
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)
                time.sleep(2)
            if position==19:
                print("you landed on Vine Street")
                if a14==0:
                    buy=int(input("press 1 to buy it or press 0 to continue"))
                    if buy==1:
                        money-=65
                        houses+=1
                        a14+=1
                    else:
                        pass
                elif a14>0:
                    print("you already own a house here")
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)    
                time.sleep(2)
            if position==20:
                print("you landed on Just Parking")
                time.sleep(2)
            if position==21:
                print("you landed on Strand")
                if a15==0:
                    buy=int(input("press 1 to buy it or press 0 to continue"))
                    if buy==1:
                        money-=70
                        houses+=1
                        a15+=1
                    else:
                        pass
                elif a15>0:
                    print("you already own a house here")
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)
                time.sleep(2)
            if position==23:
                print("you landed on Fleet Street")
                if a16==0:
                    buy=int(input("press 1 to buy it or press 0 to continue"))
                    if buy==1:
                        money-=65
                        houses+=1
                        a16+=1
                    else:
                        pass
                elif a16>0:
                    print("you already own a house here")
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)
                time.sleep(2)
            if position==24:
                print("you landed on Trafalgar Square")
                if a17==0:
                    buy=int(input("press 1 to buy it or press 0 to continue"))
                    if buy==1:
                        money-=75
                        houses+=1
                        a17+=1
                    else:
                        pass
                if a17>0:
                    print("you already own a house here")
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)
                time.sleep(2)
            if position==25:
                print("you landed on Fenchurch Station")
                if a18==0:
                    buy=int(input("press 1 to buy it or press 0 to continue"))
                    if buy==1:
                        money-=65
                        rail+=1
                        a18+=1
                    else:
                        pass
                elif a18>0:
                    print("you already own a house here")
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)
                time.sleep(2)
            if position==26:
                print("you landed on Leicester Square")
                if a19==0:
                    
                    buy=int(input("press 1 to buy it or press 0 to continue"))
                    if buy==1:
                        money-=85
                        houses+=1
                        a19+=1
                    else:
                        pass
                elif a19>0:
                    print("you already own a house here")
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)
                time.sleep(2)
            if position==27:
                print("you landed on Coventy Street")
                if a20==0:
                    buy=int(input("press 1 to buy it or press 0 to continue"))
                    if buy==1:
                        money-=85
                        houses+=1
                        a20+=1
                    else:
                        pass
                elif a20>0:
                    print("you already own a house here")
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)
                time.sleep(2)
            if position==28:
                print("you landed on WaterWorks")
                if a21==0:
                    buy=int(input("press 1 to buy it or press 0 to continue"))
                    if buy==1:
                        money-=90
                        rail+=1
                        a21+=1
                    else:
                        pass
                elif a21>0:
                    print("you already own a house here")
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)
                time.sleep(2)
            if position==29:
                print("you landed on Piccadilly")
                if a22==0:
                    buy=int(input("press 1 to buy it or press 0 to continue"))
                    if buy==1:
                        money-=85
                        houses+=1
                        a22+=1
                    else:
                        pass
                elif a22>0:
                    print("you already own a house here")
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)
                time.sleep(2)
            if position==30:
                print("you landed on go to jail")
                if free>=1:
                    free-=1
                    position=10
                    print("you had a get out of jail card")
                else:
                    print("you have landed yourself in trouble so you are in jail")
                    money-=50
                    time.sleep(2)
            if position==31:
                print("you landed on Regent Street")
                if a23==0:
                    buy=int(input("press 1 to buy it or press 0 to continue"))
                    if buy==1:
                        money-=100
                        houses+=1
                        a23+=1
                    else:
                        pass
                elif a23>0:
                    print("you already own a house here")
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)
                time.sleep(2)
            if position==32:
                print("you landed on Oxford Street")
                if a24==0:
                    buy=int(input("press 1 to buy it or press 0 to continue"))
                    if buy==1:
                        money-=95
                        rail+=1
                        a24+=1
                    else:
                        pass
                elif a24>0:
                    print("you already own a house here")
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)
                time.sleep(2)
            if position==34:
                print("you landed on Bond Street")
                if a25==0:
                    buy=int(input("press 1 to buy it or press 0 to continue"))
                    if buy==1:
                        money-=105
                        houses+=1
                    else:
                        pass
                if a25>0:
                    print("you already own a house here")
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)
                time.sleep(2)
            if position==35:
                print("you landed on Liverpool Street Station")
                if a26==0:
                    buy=int(input("press 1 to buy it or press 0 to continue"))
                    if buy==1:
                        money-=80
                        rail+=1
                        a26+=1
                    else:
                        pass
                elif a26>0:
                    print("you already own a house here")
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)    
                time.sleep(2)
            if position==37:
                print("you landed on Park lane ")
                if a27==0:
                    buy=int(input("press 1 to buy it or press 0 to continue"))
                    if buy==1:
                        money-=125
                        houses+=1
                        a27+=1
                    else:
                        pass
                elif a27>0:
                    print("you already own a house here")
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)
                time.sleep(2)
            if position==38:
                print("you landed on Luxury tax")
                money-=75
                time.sleep(2)
            if position==39:
                print("you landed on May Fair")
                if a28==0:
                    buy=int(input("press 1 to buy it or press 0 to continue"))
                    if buy==1:
                        money-=135
                        houses+=1
                        a28+=1
                    else:
                        pass
                elif a28>0:
                    print("you already own a house here")
                print("you have ",money,"euros left and no. of houses bought are",houses,"and the no of other properties owned are",rail)  
                time.sleep(2)
            if money<=0:
                gameon=False
if a==2:
    print("""this is how you play the game
          
          All of the following Monopoly rules come from the official game instructions that have accompanied standard U.S. Monopoly sets since 2008. If they differ from the way your family plays, that's perfectly fine, since Monopoly has always fostered a rich culture of "house rules."
          
          The object of Monopoly is become the wealthiest player by buying, selling, trading and collecting rent on properties. Depending on how long you want to play, you can either play until all but one player has gone bankrupt or set a time limit and crown the richest player the champion.
          
          To start the game, each player chooses a token and one player is selected as the banker. The banker distributes $1,500 in Monopoly money to all players: two $500s, $100s and $50s; six $20s; five each of $10s, $5s and $1s.
          
          The highest roll of the dice goes first. Start in the GO square and move clockwise around the board according to the number on the dice. If you land on an available property, you can buy it by paying the banker the price listed on the title. The advantage of owning property is that opponents have to pay you rent when they land on your square. If you buy all of the properties in the same color group, then you have a monopoly, allowing you to charge double the listed rent. Once you have a monopoly, you can start to build houses and eventually a hotel, raising the rent further. Of course, you have to pay rent whenever you land on an opponent's property.
          
          If you land on an available property, but decline to buy it, then the banker can auction the property to the highest bidder. The banker starts the bidding at any price and all players can participate, including the banker and the player who originally declined the property.
          
          You can get sent to jail three ways, by landing on the square marked "Go to Jail," by picking a "Go to Jail" card or by throwing three doubles in a row. You can also get out of jail three ways: using the "Get out of Jail Free" card, rolling doubles on one of three consecutive turns or paying your way out with $50. If you don't roll doubles after three turns, you have to pay $50 to get out of jail. While in jail, you can still buy or sell properties, build houses and hotels and collect rent.
          
          Trading and private sales of properties between players is not only legal, but highly encouraged. The only thing that players cannot do is give private loans. Only the banker can mortgage a property. The fixed interest rate for "lifting" a mortgage is 10 percent of the price on the title.
          
          A player goes bankrupt when he or she doesn't have enough cash or assets to pay the bank or another player. Players can sell houses and hotels back to the bank for half of their original value -- but if that doesn't provide enough cash, the bankrupt player forfeits all properties to the bank or an opponent and is out of the """)
          
              
if a==3:
  pass
print("Game Exited Thank You!! for playing")            
print("Game made by Kingshuk")        
        




























