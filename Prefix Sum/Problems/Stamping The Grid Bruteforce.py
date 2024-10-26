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

def checkAndFill(matrix,row1,row2,col1,col2):
    for i in range(row1,row2+1):
        for j in range(col1,col2+1):
            if(matrix[i][j]):
                return False
    for i in range(row1,row2+1):
        for j in range(col1,col2+1):
            matrix[i][j]=None
    return True

def checkAndFill(matrix,prefix,row1,row2,col1,col2):
    sum=prefix[row2][col2]
    if(row1>0):
        sum-=prefix[row1-1][col2]
    if(col1>0):
        sum-=prefix[row2][col1-1]
    if(row1>0 and col1>0):
        sum+=prefix[row1-1][col1-1]
    if(sum!=0):
        return False
    for i in range(row1,row2+1):
        for j in range(col1,col2+1):
            matrix[i][j]=None
    return True

def bruteForce(n,m,matrix,height,width):
    prefix=prefixSum(n,m,matrix)
    for i in range(n):
        for j in range(m):
            if(matrix[i][j]):
                continue
            if(j+width>m):
                continue
            if(i+height>n):
                continue
            # checkAndFill(matrix,i,i+height,j,j+width)
            checkAndFill(matrix,prefix,i,i+height-1,j,j+width-1)
    for i in range(n):
        for j in range(m):
            if(matrix[i][j]!=1 and matrix[i][j]!=None):
                return False
    return True

n,m=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(n)]
height=int(input())
width=int(input())
print(bruteForce(n,m,matrix,height,width))
