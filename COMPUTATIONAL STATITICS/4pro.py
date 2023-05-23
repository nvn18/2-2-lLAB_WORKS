import numpy as np

def mylen(a):
    c=0
    for i in a:
        c+=1
    return c
def ranks(e):
    
    N=mylen(e)
    ranke=[None for _ in range(N)]
    for i in range(N):
        ran=1
        n=1
        for j in range(i):
            
            if(e[j] > e[i]):
                ran+=1
            if(e[j] == e[i]):
                n+=1
        
        for j in range(i+1,N):
            
            if(e[j] > e[i]):
                ran+=1
            if(e[j] == e[i]):
                n+=1
        
        ranke[i] = ran+n/2
    return ranke
def RemDups(data):
    RemDups = []
    
    for i in data:
        if i not in RemDups:
            RemDups.append(i)
            
    return RemDups

def CF(x,y):
    cf = 0
    
    x = list(x)
    y = list(y)
    
    RemDups_x = RemDups(x)
    RemDups_y = RemDups(y)
    
    for i in RemDups_x:
        count = x.count(i)
        if count > 1:
            cf += (count * (count**2 - 1)) / 12
            
    for i in RemDups_y:
        count = y.count(i)
        if count > 1:
            cf += (count * (count**2 - 1)) / 12
    
    return cf

x=np.array(list(map(float,input("enter the X:").split())))
y=np.array(list(map(float,input("enter the Y:").split())))
n=mylen(x)
A=ranks(x)
B=ranks(y)
print(A)
print(B)

di=np.subtract(A,B)
print(di)
disq=np.square(di)
print(disq)
s=sum(disq)
cf=CF(x,y)
s+=cf
sp=1-((6*s)/(n*(n**2-1)))
print(sp)
print(cf)
