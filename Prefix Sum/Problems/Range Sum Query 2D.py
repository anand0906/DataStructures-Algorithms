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

def bruteForce(n,m,matrix,q,queries):
    ans=[]
    for row1,col1,row2,col2 in queries:
        sum=0
        for i in range(row1,row2+1):
            for j in range(col1,col2+1):
                sum+=matrix[i][j]
        ans.append(sum)
    return ans

def optimized(n,m,matrix,q,queries):
    ans=[]
    prefix=prefixSum(n,m,matrix)
    for row1,col1,row2,col2 in queries:
        sum=prefix[row2][col2]
        if(col1>0):
            sum-=prefix[row2][col1-1]
        if(row1>0):
            sum-=prefix[row1-1][col2]
        if(row1>0 and col1>0):
            sum+=prefix[row1-1][col1-1]
        ans.append(sum)
    return ans


n,m=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(n)]
q=int(input())
queries=[list(map(int,input().split())) for i in range(q)]
print(bruteForce(n,m,matrix,q,queries))
print(optimized(n,m,matrix,q,queries))
