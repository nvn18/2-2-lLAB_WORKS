#week 5:
#Write a python program to classify the data based on one way ANOVA.


import numpy as np
import scipy.stats as s

def sq(n):
    
    p=0
    for i in n:
        p+=i**2
    return p
def mylen(n):
    c=0
    for i in n:
        c+=1
    return c
def mysum(n):
    s=0
    for i in n:
        s+=i
    return s


name=input("enter the name of the treatment:")
k=int(input("enter the number of inputs:"))
treat=[]
for i in range(k):
    a=np.array(list(map(float,input(f"enter the {name}{i+1}").split())))
    treat.append(a)
alpha=float(input("enter the level of siginificance:"))

Ti=Ti2=N=RSS=0

for i in treat:
    RSS+=mysum(i*i)
    N+=mylen(i)
    Ti+=mysum(i)
    Ti2+=((mysum(i)**2)/mylen(i))

CF=(Ti**2)/N
SST=RSS-CF
SSTR=Ti2-CF
SSE = SST-SSTR


print('the total sum of Ti:',Ti)
print("the total sum of Ti^2/Ni:",Ti2)
print("the RSS value:",RSS)
print("the CF value is:",CF)

print("the SST value is:",SST)
print("the SSTR value is:",round(SSTR,3))
print("the SSE value is:",round(SSE,3))
n1=k-1
n2=N-k
total=N-1
T1=SSTR+SSE

tr=round(SSTR/n1,3)
er=round(SSE/n2,3)
print("the means of treatment:",tr)
print("the means of errors:",er)

Fcal=tr/er
if(Fcal>1):
    print("The Fcal value is:",Fcal)
elif(Fcal<1):
    Fcal=1/Fcal
    print("The Fcal value is:",Fcal)
else:
    print('none')

Ftable = s.f.ppf(1-alpha,k-1,N-k)
print("The Ftable value is:",Ftable)

    
print("---------------------ANOVA ONE WAY CLASSIFICATION TABLE------")
print("---------------------------------------------------------------------------------------------------------------------------")

d={}

d={1:["treatment",round(SSTR,3),n1,tr,''],
   2:["error",round(SSE,5),n2,er,Fcal],
   3:["TOTAL",round(T1,3),total,'',''],
}
print("{:<10} {:<10} {:<10} {:<10} {:<10}".format('SOV','SOS','DOF','MOS','VR'))

for key,value in d.items():
    sourceofvarition, sumsofsquares, degreeoffreedom, meansofsquare, varianceration = value
    print("{:<10} {:<10} {:<10} {:<10} {:<10}".format(sourceofvarition,sumsofsquares,degreeoffreedom,meansofsquare,varianceration))
print("------------------------------------------------------------------------------------------------------------------------------")

print("-----------INFERNCE:------")

if(Fcal > Ftable):
    print(f"We reject h0 and there is no homogenity among:{name}")
else:
    print(f"We accpet h0 and there is homogenity among:{name}")





