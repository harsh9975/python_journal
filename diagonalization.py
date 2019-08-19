from sympy import Matrix
M=Matrix([[2,6],[0,-1]])
print("Matrix M=",M)
print(M.eigenvals())
print(M.eigenvects())
P,D=M.diagonalize()
print(P)
print(D)
print(P*D*P**-1)
print(P*D*P**-1==M)