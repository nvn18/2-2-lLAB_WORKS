import pandas as pd
import numpy as np
import scipy.stats as sc
from math import sqrt

def mysum(n):
    s=0
    for i in n:
        s+=i
    return s
def lenght(n):
    c=0
    for i in n:
        c+=1
    return c
def mymean(n):
    s=0
    for i in n:
        s+=i
    return s/lenght(n)
def sq(n):
    p=0
    for i in n:
        p+=i**2
    return p  
#def inverse()

p = int(input("Enter no. of variables in the model:"))

if p == 2:
    y = np.array([float(i) for i in input("Enter y values: ").strip().split()])
    x1 = np.array([float(i) for i in input("Enter x1 values: ").strip().split()])
    #y = np.array([10,20,30,40,50])
    #x1 = np.array([5,7,10,12,20])
    
    leny = len(y)
    lenx1 = len(x1)
    
    if lenx1 != leny:
        print("Invalid Data!")
    else:
        x0 = np.array([1 for i in range(lenx1)])
        X = [x0,x1]
        
        XTX = np.array([[mysum(x0**2),mysum(x0*x1)],[mysum(x1*x0),mysum(x1**2)]])
        
        print(XTX)
        
        XTX_inv = np.linalg.inv(XTX)
        print(XTX_inv)
        
        XTY = np.array([mysum(x0 * y), mysum(x1 * y)])
        print(XTY)
        
        bcap = [mysum(XTX_inv[0] * XTY), mysum(XTX_inv[1] * XTY)]
        print(bcap)
        
        print("Y=",bcap[0],"+",bcap[1],"X")
        yfit = np.array([bcap[0] + bcap[1]*x1])
        
if p == 3:
    y = np.array([float(i) for i in input("Enter y values: ").strip().split()])
    x1 = np.array([float(i) for i in input("Enter x1 values: ").strip().split()])
    x2 = np.array([float(i) for i in input("Enter x2 values: ").strip().split()])
    
    #y=np.array([11,11,8,2,5,5,4])
    #x1=np.array([-5,-4,-1,2,2,3,3])
    #x2=np.array([5,4,1,-3,-2,-2,-3])
    
    leny = len(y)
    lenx1 = len(x1)
    lenx2 = len(x2)

    if leny != lenx1 or leny != lenx2 or lenx1 != lenx2:
        print("Invalid Data!")
    else:
        x0 = np.array([1 for i in range(lenx1)])
        X = [x0,x1,x2]
        
        XTX = np.array([[mysum(x0**2),mysum(x0*x1),mysum(x0*x2)],[mysum(x1*x0),mysum(x1**2),mysum(x1*x2)],[mysum(x2*x0),mysum(x2*x1),mysum(x2**2)]])
        print("the matrix is:",XTX)
        
        XTX_inv = np.linalg.inv(XTX)
        print("the inverse of the matrix:",XTX_inv)

        
        XTY = np.array([mysum(x0 * y), mysum(x1 * y),mysum(x2 * y)])
        print("the X Transpose Y matrix is:",XTY)
       
        
        bcap = [mysum(XTX_inv[0] * XTY), mysum(XTX_inv[1] * XTY), mysum(XTX_inv[2] * XTY)]
        print(bcap)
        
        print("the Y's Equation is:")
        
        print("Y=",bcap[0],"+",bcap[1],"X1","+",bcap[2],"X2")

        yfit = np.array(bcap[0] + bcap[1]*x1 + bcap[2]*x2)
        print("the YFitted values:",yfit)
        
        print("-------------------------------------------------------")
        
        print("to test the goodness of the fit of the(R2):")
        
        E = y - yfit
        print(E)
        
        ybar=mymean(y)
        print(ybar)
        
        Ytran = y - ybar
        print(Ytran)
        
        print("---------------------------------------------------------------")
        data =({
            "yvalues": y,
             "Y fit": yfit,
            "E=y-yfit": E,
             "y-ybar": Ytran
        })
        dataframe = pd.DataFrame(data)
        print(dataframe)
        print("---------------------------------------------------------------")
        
        SSE = mysum(E**2)
        print("Sum of sqaures due to error:",SSE) 
        SST = mysum(Ytran**2)
        print("Sum of square due to total:",SST)
        SSR = SST - SSE
        print("Sum of squares due to regression:",SSR)
        
        R2 = SSR/SST
        print("Co-efficient of determination:",R2)
        
        if(R2>=0.90):
            print("we Conclude that, MLR is a good fit")
        else:
            print("we conclude that, MLR is not a good fit")
            
            
        print("--------------------------------------------------------------------------------------")
        
        print("to test the goodness of fit using the ANOVA:")
        
        alpha = float(input("enter the level of siginifance:"))
        
        n = len(y)
        print(n)
        print(p)
        
        MSSR = SSR/(p-1)
        MSSE = SSE/(n-p)
        
        print("The MSSR value:",MSSR)
        print("The MSSE value:",MSSE)
        
        Fcal = MSSR / MSSE
        print("the Fcal value is:",Fcal)
        
        Ftable = sc.f.ppf(1-alpha,(n-1),(n-p))
        print("the Ftable value:",Ftable)
        
        ANOVA_Table = {
            "S O V": ['REGRESSION', 'ERROR', "Total"],
            "S O S": ["{:.4f}".format(SSR), "{:.4f}".format(SSE), "{:.4f}".format(SST)],
            "D O F": [p-1, n-p, n-1],
            "M S O S": ["{:.4f}".format(MSSR),"{:.4f}".format(MSSE),"-"],
            "V R": ["Fcal = {:.4f}".format(Fcal), f"~ Fcal({p-1},{n-p})","-"]
        }
        df = pd.DataFrame(ANOVA_Table)
        print(df)
        
        if(Fcal > Ftable):
            print("we reject H0")
            print("we accept H1")
            print("The MLR is a good fit")
        else:
            print("we accept H0")
            print("we accept H1")
            print("The MLR is not a good fit")
        print("---------------------------------------------------------------------")
        print("TEST FOR INDIVIDUAL PARAMETER BASED ON T-TEST:")
        
        ttable = sc.t.ppf(1-alpha/2,(n-p))
        print(ttable) 
        
        se1=sqrt(MSSE*XTX_inv[0][0])
        se2=sqrt(MSSE*XTX_inv[1][1])
        se3=sqrt(MSSE*XTX_inv[2][2])
        
        tcal1=bcap[0] / se1
        tcal2=bcap[1] / se2
        tcal3=bcap[2] / se3
        
        parameter_table = {
            "predictor":['B0','B1','B2'],
            "co-effiecent":[bcap[0],bcap[1],bcap[2]],
            "SE":["{:.4f}".format(se1),"{:.4f}".format(se2),"{:.4f}".format(se3)],
            "SE":["{:.4f}".format(tcal1),"{:.4f}".format(tcal2),"{:.4f}".format(tcal3)]
        }
        pff = pd. DataFrame(parameter_table)
        print( pff)
        
        if(abs(tcal1) >= ttable):
            print("we reject H0 and we can conclude that B0 is contributing")
        else:
             print("we accept H0 and we can conclude that B0 is not contributing")
        if(abs(tcal2) >= ttable):
            print("we reject H0 and we can conclude that B1 is contributing")
        else:
             print("we accept H1 and we can conclude that B1 is not contributing")
        if(abs(tcal3) >= ttable):
            print("we reject H0 and we can conclude that B2 is contributing")
        else:
            print("we accept H1 and we can conclude that B2 is not contributing")