import numpy as np
import pandas as pd
import scipy.status as s.f.ppf()

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


pos1=np.array(list(map(float,input("enter the pos1 values:").split())))
pos2=np.array(list(map(float,input("enter the pos2 values:").split())))
pos3=np.array(list(map(float,input("enter the pos3 values:").split())))
pos4=np.array(list(map(float,input("enter the pos3 values:").split())))


#pos1=np.array([90,82,79,98,83,91])
#pos2=np.array([105,89,93,104,89,95,86])
#pos3=np.array([83,89,80,94])


p=np.array(['pos1','pos2','pos3','pos4'])
k=mylen(p)
print('the k value is:',k)

N=mylen(pos1)+mylen(pos2)+mylen(pos3)+mylen(pos4)
print('the length of no.of observation:',N)

Ti = np.sum(pos1) + np.sum(pos2) + np.sum(pos3) +np.sum(pos4)
print('the total sum of Ti:',Ti)


Ti2=(np.square(np.sum(pos1))/mylen(pos1))+(np.square(np.sum(pos2))/mylen(pos2))+(np.square(np.sum(pos3))/mylen(pos3)) + (np.square(np.sum(pos4))/mylen(pos4))
print("the total sum of Ti^2/Ni:",Ti2)


RSS=sq(pos1)+sq(pos2)+sq(pos3)+sq(pos4)
print("the RSS value:",RSS)

CF=(Ti)**2 /N
print("the CF value is:",CF)

SST=(RSS-CF)
print("the SST value is:",SST)

SSTR = (Ti2 - CF)
print("the SSTR value is:",round(SSTR,3))

SSE=(SST-SSTR)
print("the SSE value is:",round(SSE,3))


n1=k-1
n2=N-k
total=N-1
T1=SSTR+SSE

tr=round(SSTR/n1,3)
er=round(SSE/n2,3)
print("the means of treatment:",tr)
print("the means of errors:",er)

F=tr/er
if(F>1):
    print(F)
elif(F<1):
    F=1/F
    print(F)
else:
    print('none')

print("---------------------------------------------------------------------------------------------------------------------------")

d={}

d={1:["treatment",round(SSTR,3),n1,tr,''],
   2:["error",round(SSE,5),n2,er,F],
   3:["TOTAL",round(T1,3),total,'',''],
}
print("{:<10} {:<10} {:<10} {:<10} {:<10}".format('SOV','SOS','DOF','MOS','VR'))

for key,value in d.items():
    sourceofvarition, sumsofsquares, degreeoffreedom, meansofsquare, varianceration = value
    print("{:<10} {:<10} {:<10} {:<10} {:<10}".format(sourceofvarition,sumsofsquares,degreeoffreedom,meansofsquare,varianceration))
print("------------------------------------------------------------------------------------------------------------------------------")



\
