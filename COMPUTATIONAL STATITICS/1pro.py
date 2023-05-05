# program 1:

import numpy as np
from matplotlib import pyplot as plt
def lenght(n):
    c=0
    for i in n:
        c+=1
    return c
def mean(n):
    s=0
    for i in n:
        s+=i
    return s/lenght(n)


x=np.array(list(map(float,input("enter the X:").split())))
y=np.array(list(map(float,input("enter the Y:").split())))

xy = x*y
xsq = x*x

n=0
xy=x*y
xsq=x*x

for i in x:
    n+=1

X=sum(x)
Y=sum(y)
M=sum(xy)
N=sum(xsq)

print(X)
print(Y)
print(M)
print(N)

a=(Y*N - X*M)/(N*n - X*X)
b=(n*M - X*Y)/(N*n - X*X)

print(a)
print(b)

ycap=a+b*x

plt.title("Straight Line") 
plt.xlabel("x") 
plt.ylabel("y") 
plt.plot(x,ycap) 
plt.plot(x,y)
plt.show()

ybar=sum(y)/lenght(y)
print("Y=",round(a,5),"+",round(b,5),"X")

sse=0
sst=0
for i in range(lenght(x)):
    sse+=(y[i] - ycap[i])**2
    sst+=(y[i] - ybar)**2
r2 = (1-sse/sst)
print(sst)
print(sse)
print("r2=",r2,"%")
if(r2>=0.9):
    print("it is a best fit")
else:
    print("it is not a best fit")

