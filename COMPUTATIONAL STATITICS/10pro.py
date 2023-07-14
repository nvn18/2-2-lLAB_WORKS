import numpy as np
from math import log as ln

def mymean(data):
    Sum = 0
    for i in data:
        Sum += i
    return Sum/len(data)

#a = np.array([float(i) for i in input("Enter a values: ").strip().split()])
#b = np.array([float(i) for i in input("Enter b values: ").strip().split()])
#c = np.array([float(i) for i in input("Enter c values: ").strip().split()])

#a = np.array([2.95,2.53,3.57,3.16,2.58,2.16,3.27])
#b = np.array([6.63,7.79,5.65,5.47,4.46,6.22,3.52])
#c = np.array([1,1,1,1,0,0,0])

a = np.array([4,2,2,3,4,9,6,9,8,10])
b = np.array([2,4,3,6,4,10,8,5,7,8])
c = np.array([1,1,1,1,1,0,0,0,0,0])

X = np.array([a,b])

#Given_data = np.array([float(i) for i in input("Enter the data to test: ").strip().split()])
#Given_data = np.array([2.81, 5.46])
Given_data = np.array([5,6])

m = []
n = []
p = []
q = []
count_1 = 0
count_0 = 0

for i in range(len(c)):
    if c[i] == 1:
        m.append(a[i])
        n.append(b[i])
        count_1 += 1
    elif c[i] == 0:
        p.append(a[i])
        q.append(b[i])
        count_0 += 1

X1 = [m, n]
X2 = [p, q]

Mu = [mymean(a), mymean(b)]
Mu1 = [mymean(m), mymean(n)]
Mu2 = [mymean(p), mymean(q)]

X_Mu = [a-Mu[0], b-Mu[1]]

# Pooled Covariance Matrix:
PCM = [[sum(X_Mu[0]**2)/len(c), sum(X_Mu[0]*X_Mu[1])/len(c)],
       [sum(X_Mu[1]*X_Mu[0])/len(c), sum(X_Mu[1]**2)/len(c)]]

PCM_inv = np.linalg.inv(PCM)

# Fisher's LDA:
F1_Term1 = sum(np.array([sum(Mu1*PCM_inv[0]), sum(Mu1*PCM_inv[1])]) * Given_data)
F1_Term2 = sum(np.array([sum(Mu1*PCM_inv[0]), sum(Mu1*PCM_inv[1])]) * Mu1)
F1_Term3 = ln(count_1/len(c))

F1 = F1_Term1 - 0.5*F1_Term2 + F1_Term3

F2_Term1 = sum(np.array([sum(Mu2*PCM_inv[0]), sum(Mu2*PCM_inv[1])]) * Given_data)
F2_Term2 = sum(np.array([sum(Mu2*PCM_inv[0]), sum(Mu2*PCM_inv[1])]) * Mu2)
F2_Term3 = ln(count_0/len(c))

F2 = F2_Term1 - 0.5*F2_Term2 + F2_Term3

max_val = F1 if F1>F2 else F2

print(Mu)
print(Mu1)
print(Mu2)

print(X_Mu)

print(PCM)
print(PCM_inv)

print(F1)
print(F2)

if max_val == F1:
    print("The Given Data Belongs to First Group.")
else:
    print("The Given Data Belongs to Second Group.")