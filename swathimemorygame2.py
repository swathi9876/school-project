# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 11:39:02 2019

@author: student
"""
#%%
print("                         MEMORY GAME              ")
print("""INSTRUCTIONS 1:The player needs to find the  pair of the 
             symbols 1 at a time
             2:You are provided 10 chances for the completion
             of game
             3:If you utilise all of ur chances you lost the game
             4:If you find all the pairs then only you will be 
            declared as a winner""")


a=1
b=2
c=3
d=4
e=5
f=6
g=7
h=8
i=9
j=10
k=11
l=12
m=13
n=14
o=15
p=16
print(" _____ _____ _____ _____ ")
print("|",a,"  | ",b, " |",c,"  | ",d, " |")
print("|_____|_____|_____|_____| ") 
print("|",e,"  | ",f, " |",g,"  | ",h, " |")
print("|_____|_____|_____|_____| ") 
print("|",i,"  | ",j, "|",k," | ",l, "|")
print("|_____|_____|_____|_____| ") 
print("|",m," | ",n, "|",o," | ",p, "|")
print("|_____|_____|_____|_____|")




print("SELECT THE OPTION:YES")
print("                 :NO")
      
     
count=13-1
lis1=["#","!","@","%","^","!","~","*","^","$","@","%","#","*","$","~"]
ll=[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
for i in range(12):
       
       pos1=int(input("ENTER POSITION 1:"))
       ll[pos1-1]=lis1[pos1-1]
       
    
       
       
       print(" _____ _____ _____ _____ ")     
       print("|",ll[0],"  | ",ll[1], " |",ll[2],"  | ",ll[3], " |")
       print("|_____|_____|_____|_____| ") 
       print("|",ll[4],"  | ",ll[5], " |",ll[6],"  | ",ll[7], " |")
       print("|_____|_____|_____|_____| ") 
       print("|",ll[8],"  | ",ll[9], " |",ll[10],"  | ",ll[11], " |")
       print("|_____|_____|_____|_____| ") 
       print("|",ll[12],"  | ",ll[13], " |",ll[14],"  | ",ll[15], " |")
       print("|_____|_____|_____|_____| ") 
       pos2=int(input("ENTER POSITION 2:"))
       
       ll[pos2-1]=lis1[pos2-1]
       count=count-1
       
       print(count,"CHANCES REMAINING")
       if ll[pos1-1]==ll[pos2-1]:
        print(" _____ _____ _____ _____ ")          
        print("|",ll[0],"  | ",ll[1], " |",ll[2],"  | ",ll[3], " |")
        print("|_____|_____|_____|_____| ") 
        print("|",ll[4],"  | ",ll[5], " |",ll[6],"  | ",ll[7], " |")
        print("|_____|_____|_____|_____| ") 
        print("|",ll[8],"  | ",ll[9], " |",ll[10],"  | ",ll[11], " |")
        print("|_____|_____|_____|_____| ") 
        print("|",ll[12],"  | ",ll[13], " |",ll[14],"  | ",ll[15], " |")
        print("|_____|_____|_____|_____| ") 
        if ll==lis1:
            print("CONGRATULATIONS!!! YOU WON XD")
            break
       else:
        

        print(" _____ _____ _____ _____ ")
        print("|",ll[0],"  | ",ll[1], " |",ll[2],"  | ",ll[3], " |")
        print("|_____|_____|_____|_____| ") 
        print("|",ll[4],"  | ",ll[5], " |",ll[6],"  | ",ll[7], " |")
        print("|_____|_____|_____|_____| ") 
        print("|",ll[8],"  | ",ll[9], " |",ll[10],"  | ",ll[11], " |")
        print("|_____|_____|_____|_____| ") 
        print("|",ll[12],"  | ",ll[13], " |",ll[14],"  | ",ll[15], " |")
        print("|_____|_____|_____|_____| ") 
        ll[pos1-1]=" "
        ll[pos2-1]=" "
        
        if count==0:
            print("UNFORTUNATELY YOU LOST THE GAME BETTER LUCK NEXT TIME :c")
        else:
            print("TRY AGAIN") 
         
#%%
di={"a"=1,"b"=2,"c"=3,"d"=4,"e"=5,"f"=6,"g"=7,"h"=8,"i"=9,"j"=10,"k"=11,"l"=12,"m"=13,"n"=14,"o"=15}
print(" _____ _____ _____ _____ ")
print("|",di[a],"  | ",di[b, " |",di[c],"  | ",di[d], " |")
print("|_____|_____|_____|_____| ") 
print("|",di[e],"  | ",di[f, " |",di[g],"  | ",di[h], " |")
print("|_____|_____|_____|_____| ") 
print("|",di[i],"  | ",di[j, "|",di[k]," | ",di[l], "|")
print("|_____|_____|_____|_____| ") 
print("|",di[m]," | ",di[n], "|",di[o]," | ",di[p], "|")
print("|_____|_____|_____|_____|") 