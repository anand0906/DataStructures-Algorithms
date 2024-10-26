def prefixSum(n,m,matrix):
    prefix=[[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if(i==0 and j==0):
                prefix[i][j]=matrix[i][j]
            elif(i==0 and j!=0):
                prefix[i][j]=prefix[i][j-1]+matrix[i][j]
            elif(i!=0 and j==0):
                prefix[i][j]=prefix[i-1][j]+matrix[i][j]
            else:
                prefix[i][j]=prefix[i][j-1]+prefix[i-1][j]+matrix[i][j]-prefix[i-1][j-1]
    return prefix

def prefixSum2(n,m,matrix):
    for i in range(n):
        for j in range(m):
            if(i==0 and j==0):
                matrix[i][j]=matrix[i][j]
            elif(i==0 and j!=0):
                matrix[i][j]=matrix[i][j-1]+matrix[i][j]
            elif(i!=0 and j==0):
                matrix[i][j]=matrix[i-1][j]+matrix[i][j]
            else:
                matrix[i][j]=matrix[i][j-1]+matrix[i-1][j]+matrix[i][j]-matrix[i-1][j-1]
    return matrix

n,m=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(n)]
print(prefixSum(n,m,matrix))
print(prefixSum2(n,m,matrix))
