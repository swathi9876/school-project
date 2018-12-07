#%%
import random
import time
runs=0
wickets_user,wickets_pc=10,10
print('Book Cricket Tournment')
toss_outcome=['Heads','Tails']
choice_computer=['Bat','Ball']
k=input('The toss is about to happen...Enter choice ("Heads or Tails"):')
outcome=random.choice(toss_outcome)
if k==outcome:
    time.sleep(2)
    choice=input(('Congrats! You won the toss...Choose if you want to bat or ball:'))
    if choice=='bat':
        print('Starting 1st inning..')
        time.sleep(5)
        print('Enter upper limit of book:')
        upper=int(input('>>>'))
        while wickets_user>0:  
            n=random.randrange(upper)
            if n%10<=6:
                time.sleep(2)
                print('Computer is bowling..')
                time.sleep(1)
                runs=runs+n%10
                print('Runs:',runs)
            elif n%10>6:
                time.sleep(1.5)
                print('Oops!..You are out')
                wickets_user=wickets_user-1
                time.sleep(2)
                print('Wickets left:',wickets_user)
            else:
                print('Trying again')
        print('Final Score:',runs)
        print('Starting 2nd inning')
        time.sleep(5)
        target=runs+1
        print('Target:',target)
        print('You are bowling now')
        print('Enter upper limit of book:')
        upper=int(input('>>>'))
        while wickets_pc>0:    
            n=random.randrange(upper)
            if n%10<=6:
                target=target-n%10
                print(target,'is the amount of runs left for the computer to win')
                if target==0:
                    print('You lose! Computer won..Better luck next time')
                elif target!=0 and wickets_pc==0:
                    break
                print('You won by',target,'runs')
            elif n%10>6:
                wickets_pc=wickets_pc-1
                print('Congrats!You got a wicket')
            else:
                print('Trying again')
elif k!=outcome:
    print('You lost the toss')
input()































































