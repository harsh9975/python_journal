from copy import deepcopy
def invert(X):
   
    X = deepcopy(X)
    rows = len(X)
    cols = len(X[0])
    identity = make_identity(rows,cols)
    for i in range(0,rows):
        X[i]+=identity[i]
    i = 0
    for j in range(0,cols):
        print("On col {0} and row {1}".format(j,i))  
        zero_sum, first_non_zero = check_for_all_zeros(X,i,j)   
        if zero_sum==0:
            if j==cols:
                return X
            raise Exception("Matrix is singular.")   
        if first_non_zero != i:
            X = swap_row(X,i,first_non_zero)    
        X[i] = [m/X[i][j] for m in X[i]]
        for q in range(0,rows):
            if q!=i:
                scaled_row = [X[q][j] * m for m in X[i]]
                X[q]= [X[q][m] - scaled_row[m] for m in range(0,len(scaled_row))]
        if i==rows or j==cols:
            break
        i+=1
    for i in range(0,rows):
        X[i] = X[i][cols:len(X[i])]
    return X

def check_for_all_zeros(X,i,j):
    non_zeros = []
    first_non_zero = -1
    for m in range(i,len(X)):
        non_zero = X[m][j]!=0
        non_zeros.append(non_zero)
        if first_non_zero==-1 and non_zero:
            first_non_zero = m
    zero_sum = sum(non_zeros)
    return zero_sum, first_non_zero

def swap_row(X,i,p):
    X[p], X[i] = X[i], X[p]
    return X

def make_identity(r,c):
    identity = []
    for i in range(0,r):
        row = []
        for j in range(0,c):
            elem = 0
            if i==j:
                elem = 1
            row.append(elem)
        identity.append(row)
    return identity
Q=[[1,2,3],[2,4,5],[3,5,6]]
C=invert(Q)
print("Inverse of the matrix: ",C)