# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 18:31:50 2019

@author: aryav
"""

x={'a':'d','b':'e','c':'f','d':'g','e':'h','f':'i','g':'j','h':'k','i':'l','j':'m','k':'n','l':'o','m':'p','n':'q','o':'r','p':'s','q':'t','r':'u','s':'v','t':'w','u':'x','v':'y','w':'z','x':'a','y':'b','z':'c',' ':'^','A':'D','B':'E','C':'F','D':'G','E':'H','F':'I','G':'J','H':'K','I':'L','J':'M','K':'N','L':'O','M':'P','N':'Q','O':'R','P':'S','Q':'T','R':'U','S':'V','T':'W','U':'X','V':'Y','W':'Z','X':'A','Y':'B','Z':'C','1':'0','2':'9','3':'8','4':'7','5':'6','6':'5','7':'4','8':'3','9':'2','0':'1',',':'<','.':'>','/':'?','"':"'",';':':','}':"]",'{':'[','+':'=','_':'-',')':'!','(':'@','*':'#','&':'$','~':'%','%':'~','$':'&','#':'*','@':'(','!':')','<':"'",'>':'.','?':'/',"'":'"',':':';',']':"}",'[':'{','=':'+','-':'_','!':')','@':'(','#':'*','$':'&','%':'~','%':'~','$':'&','#':'*','@':'(','!':')'}
y=str(input('IF YOU WANT TO GET YOUR CONFIDENTIAL MESSAGE ENCRYPTED, TYPE ENCRYPT OR DECRYPT, TO GET IT DECRYPTED: '))
if y=='ENCRYPT' or y=='Encrypt' or y=='encrypt': 
    d=str(input('ENTER YOUR CONFIDENTIAL MESSAGE: '))
    for i in d:
         if i in x:
              z=x.get(i)
              print(z,end='')
         elif i not in x:
             for key,value in x.items():
                 if value==i:
                     print(key,end='')
if y=='DECRYPT' or y=='Decrypt' or y=='decrypt': 
    e=str(input('ENTER YOUR CONFIDENTIAL MESSAGE: '))
    for i in e:
        for h,k in x.items():
            if k==i:
                print(h,end='')
#%%