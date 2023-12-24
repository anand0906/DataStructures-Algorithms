'''
Base Cases :
f(0,0)=matrix[0][0]
f(<0,<0)=float('inf')
Recurrance relation :
f(row,column)=min(matrix[row][column]+f(row-1,column),matrix[row][column]+f(row,column-1))
'''
#TC : O(2^(m*n))
#SC : O(m*n)
def recursive(row,column,matrix):
    if(row==0 and column==0):
        return matrix[0][0]
    if(row<0 or column<0):
        return float('inf')
    left=matrix[row][column]+recursive(row,column-1,matrix)
    top=matrix[row][column]+recursive(row-1,column,matrix)
    return min(left,top)

#TC : O(m*n)
#SC : O(m*n)
def memorization(row,column,matrix,memo):
    key=(row,column)
    if key in memo:
        return memo[key]
    if(row==0 and column==0):
        return matrix[0][0]
    if(row<0 or column<0):
        return float('inf')
    left=matrix[row][column]+memorization(row,column-1,matrix,memo)
    top=matrix[row][column]+memorization(row-1,column,matrix,memo)
    memo[key]=min(left,top)
    return memo[key]

#TC : O(m*n)
#SC : O(m*n)
def tabulation(m,n,matrix):
    dp=[[0]*n for i in range(m)]
    dp[0][0]=matrix[0][0]
    for i in range(m):
        for j in range(n):
            if(i==0 and j==0):
                continue
            left,top=float('inf'),float('inf')
            if(j-1>=0):
                left=matrix[i][j]+dp[i][j-1]
            if(i-1>=0):
                top=matrix[i][j]+dp[i-1][j]
            dp[i][j]=min(left,top)
    return dp[m-1][n-1]

#TC : O(m*n)
#SC : O(n)
def optimization(m,n,matrix):
    dp_prev=[0]*n
    dp_curr=[0]*n
    dp_curr[0]=matrix[0][0]
    for i in range(m):
        for j in range(n):
            if(i==0 and j==0):
                continue
            left,top=float('inf'),float('inf')
            if(j-1>=0):
                left=matrix[i][j]+dp_curr[j-1]
            if(i-1>=0):
                top=matrix[i][j]+dp_prev[j]
            dp_curr[j]=min(left,top)
        dp_prev=dp_curr.copy()
    return dp_prev[n-1]

m,n=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(m)]
print(recursive(m-1,n-1,matrix))
memo={}
print(memorization(m-1,n-1,matrix,memo))
print(tabulation(m,n,matrix))
print(optimization(m,n,matrix))
