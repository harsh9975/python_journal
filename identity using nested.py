n=int(input('enter the order of the matrix'))
def identity(n):
    m=[[0 for x in range(n)]for y in range(n)]
    for i in range(n):
        m[i][i]=1
    return m
print(identity(n))
