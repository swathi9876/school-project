# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 09:35:32 2018

@author: Aaryan H
"""

import random
n = int(input('Enter the number of participants. '))
givers = []
receivers = []
final_list = {}
x = 0
for i in range(n):
    x = input('Enter Name here. ')
    print(x, 'added.')
    givers.append(x)
    receivers.append(x)
while x != n:
    a = random.choice(givers)
    b = random.choice(receivers)
    if a != b:
        final_list[a] = b
        givers.remove(a)
        receivers.remove(b)
    else:
        continue
    x = len(final_list)
print(final_list)