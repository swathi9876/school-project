#%%
from colorama import Fore,Style
import random
import matplotlib.pyplot as plt
SaLdic={2:38,16:6,7:14,8:31,15:26,21:42,28:84,36:44,46:25,49:11,51:67,62:19,64:60,71:91,74:53,78:98,87:94,89:68,92:88,95:75,99:80}
colors=['b','g','r','c','m','y','k','w']
def showgrid():
    for i in SaLdic:
        if i==99 or i==64:
            continue
        val=SaLdic[i]
        x=[(i%10-1)*10,(val%10-1)*10]
        if val%10==0:
            x=[(i%10)*10,(val%10)*10]    
        y=[i-i%10,val-(val%10)]
        if val>i:
            col='g'
        else:
            col='y'
        plt.plot(x,y,c=col)
    plt.plot([80,90],[90,70],c='y')
    plt.plot([30,90],[60,50],c='y')
    plt.title('(っ◔◡◔)っ ♥ Snakes and Ladders ♥')
    print('Green:Ladders\nYellow:Snakes')
    for j in range(11):
        x=[(j*10)-5 for i in range(11)]
        y=[10*i-5 for i in range(11)]
        y1=[(j*10)-5 for i in range(11)]
        x1=[i*10-5 for i in range(11)]
        plt.plot(x,y,c='k')
        plt.plot(x1,y1,c='k') 
    plt.yticks([10*i for i in range(10)],[10*(i-1) for i in range(1,11)])    
    plt.xticks([10*i for i in range(10)],[i for i in range(1,11)])      
showgrid()
plt.show() 
gamewin=False
incorrect=True
while incorrect:
    try:
        player_num=int(input('Enter number of players(minimum 2):'))
        if player_num<=1:
            player_num=int(input('Enter number of players again..You cant possibly be so lonely:')) 
        incorrect=False
    except:
        print('Not  a number')
        incorrect=True
player_names=[]
for i in range(player_num):
    player_names.append(input('Enter name of player:'))
    print('Your color is',colors[i])
print(player_names)
player_positions=[]
xc=[]
yc=[]
for i in range(player_num):
    player_positions.append(0)
    xc.append(0)
    yc.append(0)
dice=[1,2,3,4,5,6]    
while not gamewin:
   
    for i in range(player_num):
        print('Press enter to roll')
        input()
        roll=random.choice(dice)
        
        if roll==6:
            print(Fore.GREEN + player_names[i],'rolled a six you get to roll again ')
            roll=roll+random.choice(dice)
            print(Style.RESET_ALL)
        if roll==12:
            print(Fore.GREEN + 'You rolled two sixes congrats you get to roll again')
            roll=roll+random.choice(dice)
            print(Style.RESET_ALL)
        print(player_names[i],'rolled a',roll)    
        newpos=player_positions[i]+roll    
        if newpos>100:
            print(Fore.RED + player_names[i],"can't go ahead of 100")
            print(Style.RESET_ALL)
            continue
        elif newpos==100:
            print(Fore.GREEN + player_names[i],'won the game congrats')
            print(Style.RESET_ALL)
            gamewin=True
            break
        elif newpos in SaLdic:
             print(player_names[i],'rolled a ',roll,'and went to ',newpos,'and')
             if newpos>SaLdic[newpos]:
                print(Fore.RED + player_names[i],'was bitten by a snake...')
                print(Style.RESET_ALL)
                player_positions[i]=SaLdic[newpos]
                print('New position of',player_names[i],'is',player_positions[i])
             elif newpos<SaLdic[newpos]:
                 print(Fore.GREEN + player_names[i],'found a ladder')
                 print(Style.RESET_ALL)
                 player_positions[i]=SaLdic[newpos]
                 print('New position of',player_names[i],'is',player_positions[i])
        
        else:
            player_positions[i]=player_positions[i]+roll
            print(player_names[i],'rolled a',roll,'and your new position is',player_positions[i])
        showgrid()
        xc[i]=(player_positions[i]%10-1)*10
        yc[i]=(player_positions[i]//10)*10
        if player_positions[i]%10==0:
            xc[i]=90
            yc[i]=(player_positions[i]//10-1)*10
        for j in range(player_num):
            plt.scatter(xc[j],yc[j],c=colors[j])
        plt.show()
print('Bye have a great time')
input()        