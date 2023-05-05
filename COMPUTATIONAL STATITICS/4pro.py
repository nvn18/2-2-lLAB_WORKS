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
        
        ranke[i] = ran+(n-1)/2
    return ranke

x=np.array(list(map(float,input("enter the X:").split())))
y=np.array(list(map(float,input("enter the Y:").split())))
n=mylen(x)
A=ranks(x)
B=ranks(y)
print(A)
print(B)

di=np.subtract(A,B)
print(di)
di2=di**2
print(di2)
s=sum(di2)
den=n*(n**2-1)
sp=(1-6*(s)/den)
print(sp)
