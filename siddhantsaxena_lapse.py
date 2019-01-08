# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 13:14:24 2019

@author: student
"""

import random
mcnt=acnt=pcnt=ecnt=50
print('The world is now a dystopia.Nuclear War has killed the majority of the population.\nYou are the President of your country.')
print('Environment:',ecnt,'Army:',acnt,'Approval:',pcnt,'Wealth:',mcnt)
print('These parameters will help you to check the environment levels,army strength,your approval rating and the wealth your country"s reserve currently have.')
print('Make sure that none of these parameters turn 0 or 100 or else you will lose the game')
a='Current laws are very old and unpopular.The people are demanding constitutional reforms'
b='Civil War in the Western Nations has brought us some refugees.What should we do with them?'
c='Sir, the Army would like to research in biological weapons for safety'
d='Recent floods have caused huge fatalities in the Western Province.People are asking for relief'
e='Sir,the South Nation has declared war on us.'
f='Plague has been spreading in the nearby towns and cities.We should provide them with medical aid'
g='Mafia and gun violence has been increasing in the past few months.We should impose a curfew.'
L=[a,b,c,d,e,f,g,]
print('-----------------------------------------------------------------------------------------')
while mcnt>0 and ecnt>0 and acnt>0 and pcnt>0 and mcnt<100 and ecnt<100 and pcnt<100 and acnt<100:
    stn=random.choice(L)
    if stn==a:
        print(stn)
        res1='1:Reform Laws.'
        res2='2:No need for reforms.'
        print(res1,'\t',res2)
        ans=int(input('enter your choice(1 or 2):'))
        if ans==1:
            pcnt+=10
            mcnt-=10
        elif ans==2:
            pcnt-=10
            mcnt+=10
        print('Environment:',ecnt,'Army:',acnt,'Approval:',pcnt,'Wealth:',mcnt)
        print('------------------')
    elif stn==b:
        print(stn)
        res1='1:Let them in.'
        res2='2:Do not let them enter.'
        print(res1,'\t',res2)
        ans=int(input('enter your choice(1 or 2):'))
        if ans==1:
            pcnt+=10
            acnt-=10
        elif ans==2:
            pcnt-=10
            acnt+=10
        print('Environment:',ecnt,'Army:',acnt,'Approval:',pcnt,'Wealth:',mcnt)
        print('------------------')
    elif stn==c:
        print(stn)
        res1='1:I approve.'
        res2='2:No! not at all!.'
        print(res1,'\t',res2)
        ans=int(input('enter your choice(1 or 2):'))
        if ans==1:
            pcnt=0
            mcnt-=30
            acnt+=40
        elif ans==2:
            pcnt+=10
            mcnt-=10
            acnt-=20
        print('Environment:',ecnt,'Army:',acnt,'Approval:',pcnt,'Wealth:',mcnt)
        print('------------------')
              
    elif stn==d:
        print(stn)
        res1='1:Send relief measures.'
        res2='2:Not my problem.'
        print(res1,'\t',res2)
        ans=int(input('enter your choice(1 or 2):'))
        if ans==1:
            pcnt+=20
            mcnt-=10
        elif ans==2:
            pcnt-=10
            mcnt+=20
        print('Environment:',ecnt,'Army:',acnt,'Approval:',pcnt,'Wealth:',mcnt)
        print('------------------')
    elif stn==e:
        print(stn)
        res1='1:Stand our men down.'
        res2='2:TO ARMS!!.'
        print(res1,'\t',res2)
        ans=int(input('enter your choice(1 or 2):'))
        if ans==1:
            pcnt+=10
            acnt-=10
        elif ans==2:
            pcnt-=10
            acnt-=20
            mcnt-=10
        print('Environment:',ecnt,'Army:',acnt,'Approval:',pcnt,'Wealth:',mcnt)
        print('------------------')
    elif stn==f:
        print(stn)
        res1='1:Send aid.'
        res2='2:I do not believe it.'
        print(res1,'\t',res2)
        ans=int(input('enter your choice(1 or 2):'))
        if ans==1:
            pcnt+=20
            mcnt-=20
            ecnt+=10
        elif ans==2:
            pcnt-=20
            mcnt+=10
            ecnt-=20
        print('Environment:',ecnt,'Army:',acnt,'Approval:',pcnt,'Wealth:',mcnt)
        print('------------------')
    elif stn==g:
        print(stn)
        res1='1:Impose Curfew.'
        res2='2:No need for it.'
        print(res1,'\t',res2)
        ans=int(input('enter your choice(1 or 2):'))
        if ans==1:
            pcnt+=40
            mcnt-=20
            acnt-=10
        elif ans==2:
            pcnt-=50
            mcnt+=10
            acnt-=10
        print('Environment:',ecnt,'Army:',acnt,'Approval:',pcnt,'Wealth:',mcnt)
        print('------------------')
  
    continue
else:
    print('YOU LOST')  
           
#%%    