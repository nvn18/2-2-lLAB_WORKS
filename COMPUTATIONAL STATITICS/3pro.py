#lab program 3(rank correlation)

import numpy as np
import math

def mylength(n):
    c=0
    for i in n:
        c+=1
    return c
def sums(x):
    s=0
    for i in x:
        s+=i
    return s
def cov(x,y):
    
    n=mylength(x)
    s=0
    xbar = sums(x)/n
    
    ybar = sums(y)/n
    
    for i in range(n):
        s+=(x[i] - xbar)*(y[i] - ybar)
        
    covar=s/n
    
    return covar
def sd(a):
    
    xbar = sums(a)/mylength(a)
    s=0
    for i in a:
        s+=(i-xbar)**2
    var=s/mylength(a)
    
    return math.sqrt(var)

x=np.array(list(map(float,input("Enter x:").split())))
y=np.array(list(map(float,input("Enter y:").split())))

r=cov(x,y)/(sd(x)*sd(y))

print("r=",r)
print("Karl Pearson’s correlation coefficient (r):",round(r,4))
