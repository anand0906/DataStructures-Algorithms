def bruteForce(n,artifacts,dig):
    ans=0
    matrix=[[0]*n for i in range(n)]
    for i,j in dig:
        matrix[i][j]=1
    print(*matrix,sep="\n")
    for row1,col1,row2,col2 in artifacts:
        covered=True
        for i in range(row1,row2+1):
            for j in range(col1,col2+1):
                if(matrix[i][j]!=1):
                    covered=False
                    break
        if(covered):
            ans+=1
    return ans

def prefix(n,m,matrix):
    prefixSum=[[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            sum=matrix[i][j]
            if(i>0):
                sum+=prefixSum[i-1][j]
            if(j>0):
                sum+=prefixSum[i][j-1]
            if(i>0 and j>0):
                sum-=prefixSum[i-1][j-1]
            prefixSum[i][j]=sum
    return prefixSum

def optimized(n,artifacts,dig):
    ans=0
    matrix=[[0]*n for i in range(n)]
    for i,j in dig:
        matrix[i][j]=1
    prefixSum=prefix(n,n,matrix)
    for row1,col1,row2,col2 in artifacts:
        totalCells=(row2-row1+1)*(col2-col1+1)
        sum=prefixSum[row2][col2]
        if(row1>0):
            sum-=prefixSum[row1-1][col2]
        if(col1>0):
            sum-=prefixSum[row2][col1-1]
        if(row1>0 and col1>0):
            sum+=prefixSum[row1-1][col1-1]
        if(sum==totalCells):
            ans+=1
    return ans


n=int(input())
artifacts=[list(map(int,input().split())) for i in range(input())]
digs=[list(map(int,input().split())) for i in range(input())]
print(bruteForce(n,artifacts,dig))
print(optimized(n,artifacts,dig))
