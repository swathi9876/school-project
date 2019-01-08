# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 09:19:13 2018

@author: Aaryan H
"""
#%%
jokes = {}
jokes[1] = '''My sister and I often laugh about how competitive we are.
But I laugh more.'''
jokes[2] = 'If we shouldn’t eat at night, why do they put a light in the fridge?'
jokes[3] = 'Velcro - What a rip off!'
jokes[4] = """Don't you hate it when someone answers their own questions?
I do"""
jokes[5] = ''' So what if I don't know what Armageddon means?
It's not the end of the world...'''
#%%
ball = {}
ball[1] = 'It is certain.'
ball[2] = 'It is decidedly so.'
ball[3] = 'Signs point to yes.'
ball[4] = 'Yes - definitely.'
ball[5] = 'Cannot predict now.'
ball[6] = 'Try again later.'
ball[7] = "Don't count on it"
ball[8] = 'It is highly doubtful.'
#%%
import random
print('Hi! I am Kōkua! Your Personal assistant!', ':}')
print('It is my duty to make your life as convenient as possible.')
print('To get a full list of my functions, type "HELP"')
print('Type "Bye" to send me away.' )
inp = ''
while inp != 'Bye':
    inp = input('How can I help you? ')
    if inp == 'HELP':
        print('HELP', 'Tell me a joke', 'Help me decide', 'Spin the wheel', sep = ', ')
        print('Bye')
    elif inp == 'Tell me a joke':
        a = random.randrange(1,6)
        print(jokes[a])
    elif inp == 'Help me decide':
        sent = input('Ask a question.')
        a = random.randrange(1,9)
        print(ball[a])
    elif inp == 'Bye':
        print('Bye! It was my pleasure serving you...')
    elif inp == 'Spin the wheel':
        l = []
        n = int(input('Enter the number of choices.'))
        for i in range(n):
            print(i+1)
            cho = input('Enter the choice. ')
            l.append(cho)
        a = random.randrange(n)
        print('The choice selected is', l[a])
        