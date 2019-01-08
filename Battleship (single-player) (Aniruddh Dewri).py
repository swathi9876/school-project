import random
E,E1,E7,E8=[],[],0,0
while E8!=5:
    if E8==0:
        E6=random.randrange (0,2)
        if E6==0:
            x=random.randrange (0,10)
            x=chr (ord ("A")+x)
            i=0
            while i!=5:
                if i==0:
                    y=random.randrange (0,10)
                    g,h=y,y
                    E1.append ([x,y])
                    i+=1
                else:
                    y=random.randrange (g-1,g+2)
                    if y in [0,1,2,3,4,5,6,7,8,9]:
                        if [x,y] in E1:
                            i+=0
                        else:
                            E1.append ([x,y])
                            g=y
                            i+=1
                    else:
                        if E1[0][1]==0 and y==g-1:
                            y,g=h+1,h+1
                            E1.append ([x,y])
                            i+=1
                        elif E1[0][1]==9 and y==g+1:
                            y,g=h-1,h-1
                            E1.append ([x,y])
                            i+=1
                        elif E1[0][1]>E1[1][1]:
                            g,y=h+1,h+1
                            E1.append ([x,y])
                            i+=1
                        else:
                            g,y=h-1,h-1
                            E1.append ([x,y])
                            i+=1
        else:
            y=random.randrange (0,10)
            i=0
            while i!=5:
                if i==0:
                    x=random.randrange (0,10)
                    g,h=x,x
                    x=chr (ord ("A")+x)
                    E1.append ([x,y])
                    i+=1
                else:
                    x=random.randrange (g-1,g+2)
                    if x in [0,1,2,3,4,5,6,7,8,9]:
                        if [chr (ord ("A")+x),y] in E1:
                            i+=0
                        else:
                            g=x
                            x=chr (ord ("A")+x)
                            E1.append ([x,y])
                            i+=1
                    else:
                        if E1[0][0]=="A" and x==g-1:
                            g,x=h+1,h+1
                            x=chr (ord ("A")+x)
                            E1.append ([x,y])
                            i+=1
                        elif E1[0][0]=="J" and x==g+1:
                            g,x=h-1,h-1
                            x=chr (ord ("A")+x)
                            E1.append ([x,y])
                            i+=1
                        elif E1[0][0]>E1[1][0]:
                            g,x=h+1,h+1
                            x=chr (ord ("A")+x)
                            E1.append ([x,y])
                            i+=1
                        else:
                            g,x=h-1,h-1
                            x=chr (ord ("A")+x)
                            E1.append ([x,y])
                            i+=1
        E+=E1
        E8+=1
    elif E8==1:
        E2=[]
        E6=random.randrange (0,2)        
        if E6==0:
            x=random.randrange (0,10)
            x=chr (ord ("A")+x)
            i=0
            while i!=4:
                if i==0:
                    k=0
                    y=random.randrange (0,10)
                    g,h=y,y
                    if [x,y] in E:
                        i+=0
                        k+=1
                    else:
                        E2.append ([x,y])
                        i+=1
                else:
                    y=random.randrange (g-1,g+2)
                    if y in [0,1,2,3,4,5,6,7,8,9]:
                        if [x,y] in E2 or [x,y] in E:
                            i+=0
                            if [x,y] in E:
                                k+=1
                            if k==2:
                                break
                        else:
                            E2.append ([x,y])
                            g=y
                            i+=1
                    else:
                        k+=1
                        if k==2:
                            break
                        if E2[0][1]==0 and y==g-1:
                            y,g=h+1,h+1
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E2.append ([x,y])
                                i+=1
                        elif E2[0][1]==9 and y==g+1:
                            y,g=h-1,h-1
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E2.append ([x,y])
                                i+=1
                        elif E2[0][1]>E2[1][1]:
                            g,y=h+1,h+1
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E2.append ([x,y])
                                i+=1
                        else:
                            g,y=h-1,h-1
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E2.append ([x,y])
                                i+=1
        else:
            E2=[]
            y=random.randrange (0,10)
            i=0
            while i!=4:
                if i==0:
                    k=0
                    x=random.randrange (0,10)
                    g,h=x,x
                    x=chr (ord ("A")+x)
                    if [x,y] in E:
                        i+=0
                        k+=1
                    else:
                        E2.append ([x,y])
                        i+=1
                else:
                    x=random.randrange (g-1,g+2)
                    if x in [0,1,2,3,4,5,6,7,8,9]:
                        if [chr (ord ("A")+x),y] in E2 or [chr (ord ("A")+x),y] in E:
                            i+=0
                            if [chr (ord ("A")+x),y] in E:
                                k+=1
                            if k==2:
                                break
                        else:
                            g=x
                            x=chr (ord ("A")+x)
                            E2.append ([x,y])
                            i+=1
                    else:
                        k+=1
                        if k==2:
                            break
                        if E2[0][0]=="A" and x==g-1:
                            g,x=h+1,h+1
                            x=chr (ord ("A")+x)
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E2.append ([x,y])
                                i+=1
                        elif E2[0][0]=="J" and x==g+1:
                            g,x=h-1,h-1
                            x=chr (ord ("A")+x)
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E2.append ([x,y])
                                i+=1
                        elif E2[0][0]>E2[1][0]:
                            g,x=h+1,h+1
                            x=chr (ord ("A")+x)
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E2.append ([x,y])
                                i+=1
                        else:
                            g,x=h-1,h-1
                            x=chr (ord ("A")+x)
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E2.append ([x,y])
                                i+=1
        if k>=2:
            E8+=0
        else:
            E+=E2
            E8+=1
    elif E8==2:
        E3=[]
        E6=random.randrange (0,2)
        if E6==0:
            x=random.randrange (0,10)
            x=chr (ord ("A")+x)
            i=0
            while i!=3:
                if i==0:
                    k=0
                    y=random.randrange (0,10)
                    g,h=y,y
                    if [x,y] in E:
                        i+=0
                        k+=1
                    else:
                        E3.append ([x,y])
                        i+=1
                else:
                    y=random.randrange (g-1,g+2)
                    if y in [0,1,2,3,4,5,6,7,8,9]:
                        if [x,y] in E3 or [x,y] in E:
                            i+=0
                            if [x,y] in E:
                                k+=1
                            if k==2:
                                break
                        else:
                            E3.append ([x,y])
                            g=y
                            i+=1
                    else:
                        k+=1
                        if k==2:
                            break
                        if E3[0][1]==0 and y==g-1:
                            y,g=h+1,h+1
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E3.append ([x,y])
                                i+=1
                        elif E3[0][1]==9 and y==g+1:
                            y,g=h-1,h-1
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E3.append ([x,y])
                                i+=1
                        elif E3[0][1]>E3[1][1]:
                            g,y=h+1,h+1
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E3.append ([x,y])
                                i+=1
                        else:
                            g,y=h-1,h-1
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E3.append ([x,y])
                                i+=1
        else:
            E3=[]
            y=random.randrange (0,10)
            i=0
            while i!=3:
                if i==0:
                    k=0
                    x=random.randrange (0,10)
                    g,h=x,x
                    x=chr (ord ("A")+x)
                    if [x,y] in E:
                        i+=0
                        k+=1
                    else:
                        E3.append ([x,y])
                        i+=1
                else:
                    x=random.randrange (g-1,g+2)
                    if x in [0,1,2,3,4,5,6,7,8,9]:
                        if [chr (ord ("A")+x),y] in E3 or [chr (ord ("A")+x),y] in E:
                            i+=0
                            if [chr (ord ("A")+x),y] in E:
                                k+=1
                            if k==2:
                                break
                        else:
                            g=x
                            x=chr (ord ("A")+x)
                            E3.append ([x,y])
                            i+=1
                    else:
                        k+=1
                        if k==2:
                            break
                        if E3[0][0]=="A" and x==g-1:
                            g,x=h+1,h+1
                            x=chr (ord ("A")+x)
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E3.append ([x,y])
                                i+=1
                        elif E3[0][0]=="J" and x==g+1:
                            g,x=h-1,h-1
                            x=chr (ord ("A")+x)
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E3.append ([x,y])
                                i+=1
                        elif E3[0][0]>E3[1][0]:
                            g,x=h+1,h+1
                            x=chr (ord ("A")+x)
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E3.append ([x,y])
                                i+=1
                        else:
                            g,x=h-1,h-1
                            x=chr (ord ("A")+x)
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E3.append ([x,y])
                                i+=1
        if k>=2:
            E8+=0
        else:
            E+=E3
            E8+=1
    elif E8==3:
        E4=[]
        E6=random.randrange (0,2)
        if E6==0:
            x=random.randrange (0,10)
            x=chr (ord ("A")+x)
            i=0
            while i!=3:
                if i==0:
                    k=0
                    y=random.randrange (0,10)
                    g,h=y,y
                    if [x,y] in E:
                        i+=0
                        k+=1
                    else:
                        E4.append ([x,y])
                        i+=1
                else:
                    y=random.randrange (g-1,g+2)
                    if y in [0,1,2,3,4,5,6,7,8,9]:
                        if [x,y] in E4 or [x,y] in E:
                            i+=0
                            if [x,y] in E:
                                k+=1
                            if k==2:
                                break
                        else:
                            E4.append ([x,y])
                            g=y
                            i+=1
                    else:
                        k+=1
                        if k==2:
                            break
                        if E4[0][1]==0 and y==g-1:
                            y,g=h+1,h+1
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E4.append ([x,y])
                                i+=1
                        elif E4[0][1]==9 and y==g+1:
                            y,g=h-1,h-1
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E4.append ([x,y])
                                i+=1
                        elif E4[0][1]>E4[1][1]:
                            g,y=h+1,h+1
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E4.append ([x,y])
                                i+=1
                        else:
                            g,y=h-1,h-1
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E4.append ([x,y])
                                i+=1
        else:
            E4=[]
            y=random.randrange (0,10)
            i=0
            while i!=3:
                if i==0:
                    k=0
                    x=random.randrange (0,10)
                    g,h=x,x
                    x=chr (ord ("A")+x)
                    if [x,y] in E:
                        i+=0
                        k+=1
                    else:
                        E4.append ([x,y])
                        i+=1
                else:
                    x=random.randrange (g-1,g+2)
                    if x in [0,1,2,3,4,5,6,7,8,9]:
                        if [chr (ord ("A")+x),y] in E4 or [chr (ord ("A")+x),y] in E:
                            i+=0
                            if [chr (ord ("A")+x),y] in E:
                                k+=1
                            if k==2:
                                break
                        else:
                            g=x
                            x=chr (ord ("A")+x)
                            E4.append ([x,y])
                            i+=1
                    else:
                        k+=1
                        if k==2:
                            break
                        if E4[0][0]=="A" and x==g-1:
                            g,x=h+1,h+1
                            x=chr (ord ("A")+x)
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E4.append ([x,y])
                                i+=1
                        elif E4[0][0]=="J" and x==g+1:
                            g,x=h-1,h-1
                            x=chr (ord ("A")+x)
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E4.append ([x,y])
                                i+=1
                        elif E4[0][0]>E4[1][0]:
                            g,x=h+1,h+1
                            x=chr (ord ("A")+x)
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E4.append ([x,y])
                                i+=1
                        else:
                            g,x=h-1,h-1
                            x=chr (ord ("A")+x)
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E4.append ([x,y])
                                i+=1
        if k>=2:
             E8+=0
        else:
             E+=E4
             E8+=1
    elif E8==4:
        E5=[]
        E6=random.randrange (0,2)
        if E6==0:
            x=random.randrange (0,10)
            x=chr (ord ("A")+x)
            i=0
            while i!=2:
                if i==0:
                    k=0
                    y=random.randrange (0,10)
                    g,h=y,y
                    if [x,y] in E:
                        i+=0
                        k+=1
                    else:
                        E5.append ([x,y])
                        i+=1
                else:
                    y=random.randrange (g-1,g+2)
                    if y in [0,1,2,3,4,5,6,7,8,9]:
                        if [x,y] in E5 or [x,y] in E:
                            i+=0
                            if [x,y] in E:
                                k+=1
                            if k==2:
                                break
                        else:
                            E5.append ([x,y])
                            g=y
                            i+=1
                    else:
                        k+=1
                        if k==2:
                            break
                        if E5[0][1]==0 and y==g-1:
                            y,g=h+1,h+1
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E5.append ([x,y])
                                i+=1
                        elif E5[0][1]==9 and y==g+1:
                            y,g=h-1,h-1
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E5.append ([x,y])
                                i+=1
                        elif E5[0][1]>E5[1][1]:
                            g,y=h+1,h+1
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E5.append ([x,y])
                                i+=1
                        else:
                            g,y=h-1,h-1
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E5.append ([x,y])
                                i+=1
        else:
            E5=[]
            y=random.randrange (0,10)
            i=0
            while i!=2:
                if i==0:
                    k=0
                    x=random.randrange (0,10)
                    g,h=x,x
                    x=chr (ord ("A")+x)
                    if [x,y] in E:
                        i+=0
                        k+=1
                    else:
                        E5.append ([x,y])
                        i+=1
                else:
                    x=random.randrange (g-1,g+2)
                    if x in [0,1,2,3,4,5,6,7,8,9]:
                        if [chr (ord ("A")+x),y] in E5 or [chr (ord ("A")+x),y] in E:
                            i+=0
                            if [chr (ord ("A")+x),y] in E:
                                k+=1
                            if k==2:
                                break
                        else:
                            g=x
                            x=chr (ord ("A")+x)
                            E5.append ([x,y])
                            i+=1
                    else:
                        k+=1
                        if k==2:
                            break
                        if E5[0][0]=="A" and x==g-1:
                            g,x=h+1,h+1
                            x=chr (ord ("A")+x)
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E5.append ([x,y])
                                i+=1
                        elif E5[0][0]=="J" and x==g+1:
                            g,x=h-1,h-1
                            x=chr (ord ("A")+x)
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E5.append ([x,y])
                                i+=1
                        elif E5[0][0]>E5[1][0]:
                            g,x=h+1,h+1
                            x=chr (ord ("A")+x)
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E5.append ([x,y])
                                i+=1
                        else:
                            g,x=h-1,h-1
                            x=chr (ord ("A")+x)
                            if [x,y] in E:
                                k+=1
                                if k==2:
                                    break
                            else:
                                E5.append ([x,y])
                                i+=1
        if k>=2:
            E8+=0
        else:
            E+=E5
            E8+=1 
K,L=0,0
for i in range (1,12):
    if i==1:
        for j in range (10):
            if L==9:
                print ("  9")
                break
            else:
                print (" ",chr (ord ("0")+L),end="")
                L+=1
        print ("  ",end="")
        for j in range (10):
            print ("___",end="")
    else:
        print (chr (ord ("A")+K),end="")
        K+=1
        for j in range (11):
            if j!=10:
                print ("|__",end="")
            else:
                print ("|",end="")
    print ()
D,SHOT,E1a,E2a,E3a,E4a,E5a=[],0,0,0,0,0,0
print ("Welcome to Battleship! There are five ships:")
print ("    One Carrier (5 tiles);\n    one Battleship (4 tiles);\n    one Destroyer (3 tiles);\n    one Submarine (3 tiles);\n    and one Patrol Boat (2 tiles).")
print ("You have 30 shots. Sink all ships to win!")
print ("\nIf you want to quit at any time, enter 'quit' with no quotes and no punctuation.")
while E7!=17 and SHOT<30:
    p=input ("Enter x-coordinate: ")
    while p.capitalize () not in ("A","B","C","D","E","F","G","H","I","J"):
        if p.capitalize ()=="List":
            print ("\nRemaining ships:")
            if E1a==0:
                print ("The Carrier (5 tiles).")
            if E2a==0:
                print ("The Battleship (4 tiles).")
            if E3a==0:
                print ("The Destroyer (3 tiles).")
            if E4a==0:
                print ("The Submarine (3 tiles).")
            if E5a==0:
                print ("The Patrol Boat (2 tiles).")
            p=input ("Enter x-coordinate: ")
        elif p.capitalize ()=="Quit":
            break
        else:
            p=input ("Incorrect input. Re-enter: ")
    if p.capitalize ()=="Quit":
        print ("Thank you for playing.")
        a=input ("Would you like to know where the remaining ships were located at? (Yes/No): ")
        if a.capitalize ()=="Yes":
            print ("\nThe remaining ships were: ")
            if E1a==0:
                print ("The Carrier, located at",E1,end=".\n")
            if E2a==0:
                print ("The Battleship, located at",E2,end=".\n")
            if E3a==0:
                print ("The Destroyer, located at",E3,end=".\n")
            if E4a==0:
                print ("The Submarine, located at",E4,end=".\n")
            if E5a==0:
                print ("The Patrol Boat, located at",E5,end=".\n")
            break
        else:
            print ("Good-bye.")
            break
    p=p.capitalize ()
    q=input ("Enter y-coordinate: ")
    while q not in ("0","1","2","3","4","5","6","7","8","9"):
        if q.capitalize ()=="List":
            print ("\nRemaining ships:")
            if E1a==0:
                print ("The Carrier (5 tiles).")
            if E2a==0:
                print ("The Battleship (4 tiles).")
            if E3a==0:
                print ("The Destroyer (3 tiles).")
            if E4a==0:
                print ("The Submarine (3 tiles).")
            if E5a==0:
                print ("The Patrol Boat (2 tiles).")
            q=input ("Enter y-coordinate: ")
        elif q.capitalize ()=="Quit":
            break
        else:
            q=input ("Incorrect input. Re-enter: ")
    if q.capitalize ()=="Quit":
        print ("Thank you for playing, you chicken!")
        a=input ("Would you like to know where the remaining ships were located at? (Yes/No): ")
        if a.capitalize ()=="Yes":
            print ("\nThe remaining ships were: ")
            if E1a==0:
                print ("The Carrier, located at",E1,end=".\n")
            if E2a==0:
                print ("The Battleship, located at",E2,end=".\n")
            if E3a==0:
                print ("The Destroyer, located at",E3,end=".\n")
            if E4a==0:
                print ("The Submarine, located at",E4,end=".\n")
            if E5a==0:
                print ("The Patrol Boat, located at",E5,end=".\n")
            break
        else:
            print ("Good-bye.")
            break
    q=int (q)
    d=[p,q]
    print ("Coordinates are as follows:",d,end=".\n")     
    if d in D:
        print ("The shot has been aborted!")
        SHOT+=0
    else:
        SHOT+=1
    if d in E:
        if d in D:
            E7+=0
        else:
            E7+=1
            SHOT-=2
            print ("You hit something!")
    D.append (d)
    a=input ()
    A,K,L=ord ("A"),0,0
    for j in range (1,12):
        if j==1:
            for k in range (10):
                if L==9:
                    print ("  9")
                    break
                else:
                    print (" ",chr (ord ("0")+L),end="")
                    L+=1
            print ("  ",end="")
            for l in range (10):
                print ("___",end="")
        else:
            B=0
            print (chr (ord ("A")+K),end="")
            K+=1
            for m in range (11):
                if m!=10:
                    if [chr (A),B] in D:
                        if [chr (A),B] in E:
                            print ("|_X",end="")
                            B+=1
                        else:
                            print ("|_O",end="")
                            B+=1
                    else:    
                        print ("|__",end="")
                        B+=1
                else:
                    print ("|",end="")
                    B+=1
            A+=1
        print ()
    if E1[0] in D and E1[1] in D and E1[2] in D and E1[3] in D and E1[4] in D and E1a!=1:
        print ("You sunk the Carrier!")
        E1a+=1
    if E2[0] in D and E2[1] in D and E2[2] in D and E2[3] in D and E2a!=1:
        print ("You sunk the Battleship!")
        E2a+=1
    if E3[0] in D and E3[1] in D and E3[2] in D and E3a!=1:
        print ("You sunk the Destroyer!")
        E3a+=1
    if E4[0] in D and E4[1] in D and E4[2] in D and E4a!=1:
        print ("You sunk the Submarine!")
        E4a+=1
    if E5[0] in D and E5[1] in D and E5a!=1:
        print ("You sunk the Patrol Boat!")
        E5a+=1
    if SHOT==30:
        if E7==17:
            print ("You sunk all the ships! You win!\nThank you for playing.")
            break
        else:
            print ("You are out of ammunition! You lose!\nThank you for playing.")
            print ("\nThe remaining ships were:")
            if E1a==0:
                print ("The Carrier, located at",E1,end=".\n")
            if E2a==0:
                print ("The Battleship, located at",E2,end=".\n")
            if E3a==0:
                print ("The Destroyer, located at",E3,end=".\n")
            if E4a==0:
                print ("The Submarine, located at",E4,end=".\n")
            if E5a==0:
                print ("The Patrol Boat, located at",E5,end=".\n")
            break
    if E7==17:
        print ("You sunk all the ships! You win!\nThank you for playing.")
        break
    if 30-SHOT!=1:
        print ("You have",30-SHOT,"shots left.")
    else:
        print ("You have 1 shot left.")
    if SHOT%5==0:
        if 0<SHOT<6:
            print ("If you wish to know which ships remain, type 'list' in the coordinates with no quotes and no punctuations.")
        elif 6<SHOT<11:
            print ("If you wish to abort a shot, simply shoot at coordinates you have already shot at.")
        elif 11<SHOT<16:
            print ("If you lose the game or quit, you can find out where the remaining ships were located.")