import numpy as np
import pandas as pd
from numpy.linalg import eig

def inverse(n):
    return np.linalg.inv(n)


#a=np.array([float(i) for i in input("enter the a vales:").strip().split()])
#b=np.array([float(i) for i in input("enter the b vales:").strip().split()])
#c=np.array([float(i) for i in input("enter the c vales:").strip().split()])

a=np.array([90,90,60,60,30])
b=np.array([60,90,60,60,30])
c=np.array([90,30,60,90,30])

X=[a,b,c]
MU=[sum(X[0])/len(a) , sum(X[1])/len(b) , sum(X[2])/len(c)]
print(MU)

XMU=[a-MU[0],b-MU[1],c-MU[2]]
print(XMU)




PCM = [[sum(XMU[0]**2)/len(c), sum(XMU[0]*XMU[1])/len(c),sum(XMU[0]*XMU[2])/len(c)],
       [sum(XMU[1]*XMU[0])/len(c), sum(XMU[1]**2)/len(c) ,sum(XMU[1]*XMU[2])/len(c)],
       [sum(XMU[2]*XMU[0])/len(c), sum(XMU[1]*XMU[2])/len(c), sum(XMU[2]**2)/len(c)]]
print(PCM)

invv = inverse(PCM)
print(invv)
    

w,v = eig(PCM)
print("e the eigne values:",w)
print("eiegn  vectors :",v)

u=-v[:,1]
y=-v[:,2]
print("the z1 values of eigne vaectors:",u)
print("______________________________________________--")

print("Z1=",u[0],"X1","+",u[1],"X2","+",u[2],"X3")
print("Z2=",y[0],"X1","+",y[1],"X2","+",y[2],"X3")
print("_________________________________________________________________________________")
print("the z1 values are:",u[0]*a+u[1]*b+u[2]*c)
print("the z2 values are:",y[0]*a+y[1]*b+y[2]*c)

Z1=u[0]*a+u[1]*b+u[2]*c
Z2=y[0]*a+y[1]*b+y[2]*c

data={
     "z1 values":Z1,
     "Z2 values":Z2
 }

pf = pd.DataFrame(data)
print(pf)
