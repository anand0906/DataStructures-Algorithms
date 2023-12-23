'''
Base Cases : f(0,0)=1 , f(<0,<0)=0
Recurrance Relation : f(row,column)=f(row-1,column)+f(row,column-1)
'''
#TC : O(2^n)
#SC : O(m*n)
def recursive(row,column):
    if(row==0 and column==0):
        return 1
    if(row<0 or column<0):
        return 0
    left=recursive(row-1,column)
    top=recursive(row,column-1)
    return top+left

#TC : O(m*n)
#SC : O(m+n)+O(m*n)
def memorization(row,column,memo):
    key=(row,column)
    if key in memo:
        return memo[key]
    if(row==0 and column==0):
        return 1
    if(row<0 or column<0):
        return 0
    left=memorization(row-1,column,memo)
    top=memorization(row,column-1,memo)
    memo[key]=top+left
    return memo[key]

#TC : O(m*n)
#SC : O(m*n)
def tabulation(m,n):
    dp=[[0]*n for i in range(m)]
    dp[0][0]=1
    for i in range(m):
        for j in range(n):
            if(i==0 and j==0):
                continue
            left,right=0,0
            if(i-1>=0):
                left=dp[i-1][j]
            if(j-1>=0):
                right=dp[i][j-1]
            dp[i][j]=left+right
    return dp[m-1][n-1]

#TC : O(m*n)
#SC : O(n)
def optimization(m,n):
    dp_prev=[0]*n
    dp_curr=[0]*n
    dp_curr[0]=1
    for i in range(m):
        for j in range(n):
            if(i==0 and j==0):
                continue
            left,top=0,0
            if(j-1>=0):
                left=dp_curr[j-1]
            if(i-1>=0):
                top=dp_prev[j]
            dp_curr[j]=left+top
        dp_prev=dp_curr.copy()
    return dp_prev[n-1]
m,n=list(map(int,input().split()))
print(recursive(m-1,n-1))
memo={}
print(memorization(m-1,n-1,memo))
print(tabulation(m,n))
print(optimization(m,n))

