import numpy as np
import scipy.stats as sc
import pandas as pd

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

k=int(input("enter the number of K's values:"))
h=int(input("enter the number of H's values:"))
kname=input("enter the kname:")
hname=input("enter the hname:")

treat= []
for i in range(k):
    row = []
    while mylen(row) != h:
        row = np.array([float(i) for i in input(f"Enter {kname} {i+1} values: ").strip().split()])
    treat.append(row)
                       
treat = np.array(treat)
print(treat)

alpha =float(input("enter the level of significance:"))

N = h*k

Ti=[mysum(i) for i in treat]
Ti2 = np.square(Ti)
sumTi2 = mysum(Ti2)

bj=treat[0]
for i in range(1,k):
    bj=np.add(bj,treat[i])

bj2=np.square(bj)
sumbj2=mysum(bj2)

G=mysum(Ti)

RSS=0

for i in treat:
    for j in i:
        RSS+=j**2
CF = G**2 / N

SST = RSS - CF

SSTR = sumTi2/h - CF

SSB = sumbj2/k - CF

SSE = SST - SSTR - SSB 

MeanSSTR = SSTR/(k-1)
MeanSSB = SSB/(h-1)

MeanSSE = SSE/((k-1)*(h-1))


F_Tr_cal = MeanSSTR / MeanSSE

F_B_cal = MeanSSB / MeanSSE

if(F_Tr_cal < 1):
    F_Tr_cal = 1 / F_Tr_cal

if(F_B_cal < 1):
    F_B_cal = 1 / F_B_cal

F_Tr_Table = sc.f.ppf(1-alpha, k-1, (k-1)*(h-1))

F_B_Table = sc.f.ppf(1-alpha, h-1, (k-1)*(h-1))

print("\nTi values: ",Ti)
print("Ti2 values: ",Ti2)
print("Sum of Ti2: ",sumTi2)

print("\nBj values: ",bj)
print("Bj2 values: ",bj2)
print("Sum of Bj2: ",sumbj2)

print("\nGrand Total (G): ",G)
print("Row Sum of Squares (RSS): ",RSS)
print("Correction Factor (CF): {:.4f}".format(CF))

print("\nSum of Squares due to Total (SST): {:.4f}".format(SST))
print("Sum of Squares due to Treatments (SSTr): {:.4f}".format(SSTR))
print("Sum of Squares due to Blocks (SSB): {:.4f}".format(SSB))
print("Sum of Squares due to Error (SSE): {:.4f}".format(SSE))

print("\nMean Sum of Squares due to Treatments (Mean SSTr): {:.4f}".format(MeanSSTR))
print("Mean Sum of Squares due to Blocks (Mean SSB): {:.4f}".format(MeanSSB))
print("Mean Sum of Squares due to Error (Mean SSE): {:.4f}\n".format(MeanSSE))

print("---------------------------------------------------------------------------------------------")

print("--------------- ANOVA TWO WAY CLASSIFICATION---------------------------------")

ANOVA_Two_Way_Classification_Table = {
    "S O V": [kname+'s', hname+'s', "Error", "Total"],
    "S O S": ["{:.4f}".format(SSTR), "{:.4f}".format(SSB), "{:.4f}".format(SSE), "{:.4f}".format(SST)],
    "D O F": [k-1, h-1, (k-1)*(h-1), (k*h)-1],
    "M S O S": ["{:.4f}".format(MeanSSTR), "{:.4f}".format(MeanSSB), "{:.4f}".format(MeanSSE), " - "],
    "V R": ["F(Tr)-cal = {:.4f}".format(F_Tr_cal), "~ F(k-1, (k-1)(h-1))", "F(B)-cal = {:.4f}".format(F_B_cal),"~ F(h-1, (k-1)(h-1))"]
    
}

data_frame = pd.DataFrame(ANOVA_Two_Way_Classification_Table)

print(data_frame) 

print(f"\nInference Related to {kname}s:")
print("F(Tr)-Calculated Value: {:.4f}".format(F_Tr_cal))
print("F(Tr)-Table Value: {:.4f}".format(F_Tr_Table))

if(F_Tr_cal < F_Tr_Table):
    print(f"We Accept H0(Tr)\nThere is Homogeneity among the {kname}s")
else:
    print(f"We Reject H0(Tr)\nThere is Heterogeneity among the {kname}s")
    
print(f"\nInference Related to {hname}s:")
print("F(B)-Calculated Value: {:.4f}".format(F_B_cal))
print("F(B)-Table Value: {:.4f}".format(F_B_Table))

if(F_B_cal < F_B_Table):
    print(f"We Accept H0(B)\nThere is Homogeneity among the {hname}s")
else:
    print(f"We Reject H0(B)\nThere is Heterogeneity among the {hname}s")

