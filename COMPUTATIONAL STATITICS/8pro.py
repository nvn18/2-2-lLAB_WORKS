def multi(a,b):
    res=[[0 for j in range(b[0])] for i in range(len(a))]
    for i in range(len(a)):
         for j in range(len(b[0])):
               for k in range(len(b)):
                      res[i][j] = a[i][k]*b[k][j]
       return res

    return mat3

def tran(mat):
    result = np.zeros((mat.shape[1], mat.shape[0]), dtype=float)

    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            result[j][i] = mat[i][j]

    return result

Y_dim = int(input("Enter number of Y variables: "))
X_dim = int(input("Enter number of X variables: "))

Y = []
X = []

for i in range(Y_dim):
    Y_row = np.array([float(j) for j in input(f"Enter Y{i} values: ").strip().split()])
    Y.append(Y_row)

X.append(np.array([1 for i in range(len(Y[0]))]))
for i in range(1, X_dim):
    X_row =  np.array([float(j) for j in input(f"Enter X{i} values: ").strip().split()])
    X.append(X_row)

Y = np.array(Y)
X = np.array(X)

XTX = multi(X, tran(X))
XTX_inv = np.linalg.inv(XTX)
XTY = multi(X,tran(Y))
Beta = tran(multi(XTX_inv,XTY))
print("The Multi Variate Linear Regression Models for the given data:")
for i in range(len(Y)):
    output = f"Y{i} = ({round(Beta[i][0],4)})"
    for j in range(1, len(X)):
        output += f" + ({round(Beta[i][j],4)})X{j}"
    print(output)