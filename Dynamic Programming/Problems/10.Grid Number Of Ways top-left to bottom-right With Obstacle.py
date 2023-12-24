'''
Base Cases :
f(0,0)=1
f(<0,<0)=0
f(row,column)=0 if(matrix[row][column]=-1)
Recurrance Relation :
f(row,column)=f(row-1,column)+f(row,column-1)
'''
#TC : O(2^(m*n))
#SC : O(m+n) + O(m*n)
def recursive(row,column,matrix):
    if(row==0 and column==0 and matrix[row][column]==0):
        return 1
    if(row<0 or column<0):
        return 0
    if(matrix[row][column]==-1):
        return 0
    left=recursive(row,column-1,matrix)
    top=recursive(row-1,column,matrix)
    return left+top

#TC : O(m*n)
#SC : O(m*n)
def memorization(row,column,matrix,memo):
    key=(row,column)
    if key in memo:
        return memo[key]
    if(row==0 and column==0 and matrix[row][column]==0):
        return 1
    if(row<0 or column<0):
        return 0
    if(matrix[row][column]==-1):
        return 0
    left=memorization(row,column-1,matrix,memo)
    top=memorization(row-1,column,matrix,memo)
    memo[key]=left+top
    return memo[key]

#TC : O(m*n)
#SC : O(m*n)
def tabulation(m,n,matrix):
    dp=[[0]*n for i in range(m)]
    dp[0][0]=1
    for i in range(m):
        for j in range(n):
            if(i==0 and j==0):
                continue
            left,top=0,0
            if(j-1>=0 and matrix[i][j-1]==0):
                left=dp[i][j-1]
            if(i-1>=0 and matrix[i-1][j]==0):
                top=dp[i-1][j]
            dp[i][j]=left+top
    return dp[m-1][n-1]

#TC : O(m*n)
#SC : O(n)
def optimization(m,n,matrix):
    dp_prev=[0]*n
    dp_curr=[0]*n
    dp_curr[0]=1
    for i in range(m):
        for j in range(n):
            if(i==0 and j==0):
                continue
            left,top=0,0
            if(j-1>=0 and matrix[i][j-1]==0):
                left=dp_curr[j-1]
            if(i-1>=0 and matrix[i-1][j]==0):
                top=dp_prev[j]
            dp_curr[j]=left+top
        dp_prev=dp_curr.copy()
    return dp_prev[n-1]
m,n=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(m)]
print(recursive(m-1,n-1,matrix))
memo={}
print(memorization(m-1,n-1,matrix,memo))
print(tabulation(m,n,matrix))
print(optimization(m,n,matrix))
