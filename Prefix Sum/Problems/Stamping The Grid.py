def prefixSum(n,m,matrix):
    prefix=[[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            sum=matrix[i][j]
            if(i>0):
                sum+=prefix[i-1][j]
            if(j>0):
                sum+=prefix[i][j-1]
            if(i>0 and j>0):
                sum-=prefix[i-1][j-1]
            prefix[i][j]=sum
    return prefix

def getSum(n,m,prefix,row1,col1,row2,col2):
    sum=prefix[row2][col2]
    if(row1>0):
        sum-=prefix[row1-1][col2]
    if(col1>0):
        sum-=prefix[row2][col1-1]
    if(row1>0 and col1>0):
        sum+=prefix[row1-1][col1-1]
    return sum

def optimized(n,m,matrix,height,width):
    prefix=prefixSum(n,m,matrix)
    mat=[[0]*(m+1) for i in range(n+1)]
    for i in range(n):
        for j in range(m):
            if(i+height>n):
                continue
            if(j+width>m):
                continue
            if(getSum(n,m,prefix,i,j,i+height-1,j+width-1)==0):
                mat[i][j]+=1
                mat[i][j+width]-=1
                mat[i+height][j]-=1
                mat[i+height][j+width]+=1
    prefixMat=prefixSum(n+1,m+1,mat)
    print(*prefixMat,sep="\n")
    for i in range(n):
        for j in range(m):
            if(prefixMat[i][j]==0 and matrix[i][j]!=1):
                return False
    return True


n,m=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(n)]
height=int(input())
width=int(input())
print(optimized(n,m,matrix,height,width))
