# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 09:45:05 2019

@author: student
"""

#%%
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 11:38:54 2019

@author: student
"""
#%%
code1={'A':',:,','B':'.*.','C':'{%{','D':'"<"','E':')()','F':':::',
'G':';:;','H':'*]*','I':'!_!','J':'^_^','K':'&','L':'@^5','M':'$,?','N':'#|#',
'O':'[|[','P':'`~`','Q':'~`~','R':'>2.','S':',*<','T':'+-+','U':'?|?','V':':_=',
'W':'.!.','X':'$:^','Y':';@#','Z':',.?',

'a':'|#5','b':'0$|','c':'%,8','d':'[91','e':'&=-','f':'*&9','g':'(18',
'h':'O_0','i':':\:','j':'@@@','k':'8&%','l':'5,2','m':'7&5','n':'89(','o':'||<',
'p':'$|Y','q':'!@1','r':'&h(','s':'i*&','t':'5/6','u':'*^5','v':'#/r',
'w':'pU6','x':';.[','y':'))(','z':';-+',

'1':'L<.','2':'H//{','3':'*&&','4':'LK8','5':'_--','6':'{=+}','7':'#;0',
'8':'?p]','9':'i+5','0':'@!+',

'!':',,.','&':'oo0','(':'p&+',")":'+._','$':'>>?',' ':'98z'}

ch=input('Enter \'1\' to get encrypted message or \'2\' to get decrypted message:')
if ch=='1':
    s=input('Enter decrypted message:')
    for i in s:
        print(code1[i],end='')

elif ch=='2':
    s=input('Enter encrypted message:')
    p=0
    n=len(s)
    for k in range(n):
        for j in code1.keys():
            i=s[p:p+3]
            if i==code1[j]:
                print(j,end='')
                p=p+3
else:
    print('Error! Invalid entry')         

