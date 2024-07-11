import copy
def bruteForce(n,m,matrix):
    def markRow(row):
        nonlocal matrix
        for i in range(m):
            if(matrix[row][i]!=0):
                matrix[row][i]=-1
    def markCol(col):
        nonlocal matrix
        for i in range(n):
            if(matrix[i][col]!=0):
                matrix[i][col]=-1
    for i in range(n):
        for j in range(m):
            if(matrix[i][j]==0):
                markRow(i)
                markCol(j)
    for i in range(n):
        for j in range(m):
            if(matrix[i][j]==-1):
                matrix[i][j]=0
    return matrix

def better(n,m,matrix):
    row=[0]*n
    col=[0]*m
    for i in range(n):
        for j in range(m):
            if(matrix[i][j]==0):
                row[i]=1
                col[j]=1
    for i in range(n):
        for j in range(m):
            if(row[i] or col[j]):
                matrix[i][j]=0
    return matrix

def optimized(n,m,matrix):
    c0=1
    for i in range(n):
        for j in range(m):
            if(matrix[i][j]==0):
                matrix[i][0]=0

                if(j!=0):
                    matrix[0][j]=0
                else:
                    c0=0
    for i in range(1,n):
        for j in range(1,m):
            if(matrix[i][0]==0 or matrix[0][j]==0):
                matrix[i][j]=0

    if(matrix[0][0]==0):
        for j in range(m):
            matrix[0][j]=0
    if(c0==0):
        for i in range(n):
            matrix[i][0]=0

    return matrix




n,m=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(n)]
print(bruteForce(n,m,copy.deepcopy(matrix)))
print(better(n,m,copy.deepcopy(matrix)))
print(optimized(n,m,copy.deepcopy(matrix)))
