import scipy.stats as s;
import pandas as pd;
#det
def det(x):
    return (x[0][0]*x[1][1] - x[1][0]*x[0][1])

nt=int(input("enter the no of treatments"))
lis=[]
yi_bar=[]
y_dob_bar=[]
N,sum3,sum4=0,0,0

for i in range(nt):
    sum1,sum2=0,0
    n=int(input("enter the no of observations in treatment "))
    N+=n
    l1=[]
    for j in range(n):
        l=[int(x) for x in input().split()]
        sum1+=l[0]
        sum2+=l[1]
        l1.append(l)
       
    yi_bar.append([sum1/n,sum2/n])
    lis.append(l1)
    sum3+=sum1
    sum4+=sum2

y_dob_bar.extend([sum3/N,sum4/N])
los=int(input("enter level of significance"))
print(lis)
print('yibar values = ',yi_bar)
print('y double bar values = ',y_dob_bar)

#calculations for y1
sst_y1,sse_y1,sstr_y1=0,0,0
for i in range(nt):
    for j in range(len(lis[i])):
        sst_y1+=(lis[i][j][0]-y_dob_bar[0])**2
        sse_y1+=(lis[i][j][0]-yi_bar[i][0])**2
       
sstr_y1=round(sst_y1-sse_y1,5)
sst_y1=round(sst_y1,5)
sse_y1=round(sse_y1,5)

#calculations for y2
sst_y2,sse_y2,sstr_y2=0,0,0
for i in range(nt):
    for j in range(len(lis[i])):
        sst_y2+=(lis[i][j][1]-y_dob_bar[1])**2
        sse_y2+=(lis[i][j][1]-yi_bar[i][1])**2
       
sstr_y2=round(sst_y2-sse_y2,5)
sst_y2=round(sst_y2,5)
sse_y2=round(sse_y2,5)


#calculations for y1*y2
sst_pr,sse_pr,sstr_pr=0,0,0
for i in range(nt):
    for j in range(len(lis[i])):
        sst_pr+=(lis[i][j][0]*lis[i][j][1])-(y_dob_bar[0]*y_dob_bar[1])
        sse_pr+=(lis[i][j][0]*lis[i][j][1])-(yi_bar[i][0]*yi_bar[i][1])
       
sstr_pr=round(sst_pr-sse_pr,5)
sst_pr=round(sst_pr,5)
sse_pr=round(sse_pr,5)

print("calculated values for y1")
print('Sum of suares due to total = ',sst_y1)
print('Sum of suares due to error = ',sse_y1)
print('Sum of suares due to treatments = ',sstr_y1)
print()
print("calculated values for y2")
print('Sum of suares due to total = ',sst_y2)
print('Sum of suares due to error = ',sse_y2)
print('Sum of suares due to treatments = ',sstr_y2)
print()
print("calculated values for y1*y2")
print('Sum of suares due to total = ',sst_pr)
print('Sum of suares due to error = ',sse_pr)
print('Sum of suares due to treatments = ',sstr_pr)
print()

#manova table
B,W,T=[[sstr_y1,sstr_pr],[sstr_pr,sstr_y2]],[[sse_y1,sse_pr],[sse_pr,sse_y2]],[[sst_y1,sst_pr],[sst_pr,sst_y2]]
lamda=det(W)/det(T)
Fcal=((N-nt-1)/(nt-1))*((1-lamda**0.5)/(lamda**0.5))
Ftab=s.f.ppf(1-los/100,2*(nt-1),2*(N-nt-1))

print('__________________________________________________________________________________________________')
d={'source of variation':['treatments','error','total'],'Sum os squares':[B,W,T],'degrees of freedom':[nt-1,N-nt,N-1],
    'Mean sum of squares':[lamda,'--','--'],'Variance ratio':[Fcal,'--','--']}
t=pd.DataFrame(d)
print(t)
print('__________________________________________________________________________________________________')
print()
print('  Inference  ')
print('_____________')
if(Fcal > Ftab):
    print("We reject h0 and there is no homogenity among treatments")
else:
    print(Fcal ,' < ', Ftab)
    print("We accpet h0 and there is homogenity among treatments")