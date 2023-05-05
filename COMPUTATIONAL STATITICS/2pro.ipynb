import numpy as np
from matplotlib import pyplot as plt

def length(n):
    c=0
    for i in n:
        c+=1
    return c


def det(a):
    x=a[0]
    y=a[1]
    z=a[2]
    
    l1=x[0]*((y[1]*z[2]) - (y[2]*z[1]))
    l2=x[1]*((y[0]*z[2]) - (y[2]*z[0]))
    l3=x[2]*((y[0]*z[1]) - (y[1])*z[0])
    return l1-l2+l3
x=np.array(list(map(float,input("enter X:").split())))
y=np.array(list(map(float,input("enter Y:").split())))

p=length(x)
q=sum(x)
r=sum(x*x)
s=sum(x*x*x)
t=sum(x*x*x*x)
u=sum(y)
v=sum(x*y)
w=sum(x*x*y)

delta=det([[p,q,r],[q,r,s],[r,s,t]])
delta1=det([[u,q,r],[v,r,s],[w,s,t]])
delta2=det([[p,u,r],[q,v,s],[r,w,t]])
delta3=det([[p,q,u],[q,r,v],[r,s,w]])

a=delta1/delta
b=delta2/delta
c=delta3/delta

ycap=a+b*x+c*x**2

plt.title("parabola Line") 
plt.xlabel("x") 
plt.ylabel("y") 
plt.plot(x,ycap) 
plt.plot(x,y)
plt.show()

ybar=sum(y)/length(y)
print("Y=",round(a,5),"+",round(b,5),"X","+",round(c,5),"X2")

sse=0
sst=0
for i in range(length(y)):
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
