print("do you want to encrypt or decrypt")
y=input()
if y=='encrypt':
    
    d=dict(zip( ('a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z'),('§','/','?','¥',':',';','|','ƒ','>','<','œ','^','Ç','Š','þ','›','®','©','','Ø','•','~','`','±','µ')))
    x=input("give your message")
    for k in range(len(x)):
        print(d[x[k]],end='')
    
elif y=='decrypt':
    d1=dict(zip( ('§','/','?','¥',':',';','|','ƒ','>','<','œ','^','Ç','Š','þ','›','®','©','','Ø','•','~','`','±','µ'),('a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z')))
    p=input("give your message")
    for k in range(len(p)):
        print(d1[p[k]],end='')