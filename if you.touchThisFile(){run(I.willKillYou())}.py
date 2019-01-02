#%%        
t=()
x=int(input('Enter a number\n>>>'))
for i in range(1,11):
  t+=(x*i,)
print(t)
#%%
t=()
x=int(input('Enter a number\n>>>'))
for i in range(1,4):
  t+=(x*i,)
print(t)
#%%
t,t1=(),()
s=0
for a in range(3):
  t+=((input("enter a name..."),int(input('Enter age...'))),)
for i in t:
  s+=i[1]
print(s)