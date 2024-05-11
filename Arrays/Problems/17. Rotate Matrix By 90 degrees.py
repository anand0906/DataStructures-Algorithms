def bruteForce(matrix,n,m):
    final=[[0]*m for i in range(n)]
    for i in range(n):
        for j in range(n):
            final[j][n-i-1]=matrix[i][j]
    return final

def optimized(matrix,n,m):
    for i in range(n):
        for j in range(i):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(n):
        matrix[i]=matrix[i][::-1]
    return matrix

n,m=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(n)]
print(bruteForce(matrix,n,m))
print(optimized(matrix,n,m))
