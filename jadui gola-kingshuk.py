# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 00:04:27 2019

@author: kingshuk02
"""
#%%
import random
import time


rep=["Absolutely"," Answer Unclear Ask Later"," Cannot Foretell Now"," Can't Say Now"," Chances Aren't Good"," Consult Me Later"," Don't Bet On It"," Focus And Ask Again"," Indications Say Yes"," Looks Like Yes"," No"," No Doubt About It"," Positively"," Prospect Good"," So It Shall Be"," The Stars Say No"," Unlikely"," Very Likely"," Yes"," You Can Count On It","Bear Market Ahead"," Bull Market Ahead"," Buy Now"," Buy Pork Bellies"," Buy Real Estate"," Buy T-Bills"," Change Brokers"," Don't Buy on Margin"," Go for It"," One Word: Plastics"," Out to Lunch"," Pay Off Loans First"," Ride it Out"," Sell Half Now"," Sell Now"," Sell Real Estate"," Start Own Business"," Tech Stocks Hot"," Think Precious Metals"," Unclear Ask Again","24 Hour Flu"," Abducted By Aliens"," Amnesia"," Car Trouble"," Full Moon"," Huh?"," I Was Mugged"," It's In The Mail"," It's Not My Job"," I've Got a Headache"," Jury Duty"," Kryptonite"," Mexican Food"," My Dog Ate It"," My Fish Died"," No Hablo Ingleses"," Oprah"," The Voices Told Me To"," Traffic Was Bad"," What Memo?","At Least I Love You"," Brilliant Idea!"," Half-Full"," Have You Lost Weight?"," It Can't Be All That Bad"," Look On The Bright Side"," Nice Job!"," Nice Outfit!"," Nice Try!"," People Like You"," Pure Genius!"," That's O.K."," The Sky's The Limit"," Who Says You're Stupid?"," You Can Do It!"," You Look Marvelous"," Your Breath Is So Minty"," You're 100% Fun!"," You're A Winner!"," You're Good Enough......","As If"," Ask Me If I Care"," Dumb Question Ask Another"," Forget About It"," Get A Clue"," In Your Dreams"," Not"," Not A Chance"," Obviously"," Oh Please"," Sure"," That's Ridiculous"," Well Maybe"," What Do You Think?"," Whatever"," Who Cares?"," Yeah And I'm The Pope"," Yeah Right"," You Wish"," You've Got To Be Kidding..."]
b=True
while b==True:
    a=input("do you dare to ask the magic 8 ball a question")
    time.sleep(2)
    if a=="yes"or a=="y":
        input("ask your question to the magic 8 ball")
        time.sleep(1)
        print(random.choice(rep))
    elif a=="no" or a=="n":
        print("fine....byee")
        b=False
    print("don't rely on these answers its just a random answer")    
    
    