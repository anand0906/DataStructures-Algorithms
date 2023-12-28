'''
Base Cases :
f(n-1,j)=matrix[n-1][j]
f(i<0,j<0)=float('inf')
f(i,j)=min(matrix[i][j]+f(i+1,j),matrix[i][j]+f(i+1,j+1))
'''
#TC : o(2^(n^2))
#Sc : O(n^2)
def recursive(n,i,j,matrix):
    if(i==n-1):
        return matrix[i][j]
    if(i<0 or j<0 or j>(i+1)):
        return float('inf')
    bottom=matrix[i][j]+recursive(n,i+1,j,matrix)
    bottomRight=matrix[i][j]+recursive(n,i+1,j+1,matrix)
    return min(bottom,bottomRight)

#Tc : O(n^2)
#Sc : O(n^2)
def memorization(n,i,j,matrix,memo):
    key=(i,j)
    if key in memo:
        return memo[key]
    if(i==n-1):
        return matrix[i][j]
    if(i<0 or j<0 or j>(i+1)):
        return float('inf')
    bottom=matrix[i][j]+memorization(n,i+1,j,matrix,memo)
    bottomRight=matrix[i][j]+memorization(n,i+1,j+1,matrix,memo)
    memo[key]=min(bottom,bottomRight)
    return memo[key]

#Tc : O(n^2)
#Sc : O(n^2)
def tabulation(n,matrix):
    dp=[[0]*i for i in range(1,n+1)]
    for i in range(n):
        dp[n-1][i]=matrix[n-1][i]
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            bottom,bottomRight=float('inf'),float('inf')
            if(i+1>0 and j<=(i+1)):
                bottom=matrix[i][j]+dp[i+1][j]
            if(i+1>0 and (j+1)<=(i+1)):
                bottomRight=matrix[i][j]+dp[i+1][j+1]
            dp[i][j]=min(bottom,bottomRight)
    return dp[0][0]

#Tc : O(n^2)
#Sc : O(n)
def optimization(n,matrix):
    dp_next=[0]*n
    dp_current=[0]*(n-1)
    for i in range(n):
        dp_next[i]=matrix[n-1][i]
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            bottom,bottomRight=float('inf'),float('inf')
            if((i+1)>0 and j<=(i+1)):
                bottom=matrix[i][j]+dp_next[j]
            if((i+1)>0 and (j+1)<=(i+1)):
                bottomRight=matrix[i][j]+dp_next[j+1]
            dp_current[j]=min(bottom,bottomRight)
        dp_next=dp_current.copy()
    return dp_next[0]
    
n=int(input())
matrix=[list(map(int,input().split())) for i in range(n)]
print(recursive(n,0,0,matrix))
memo={}
print(memorization(n,0,0,matrix,memo))
print(tabulation(n,matrix))
print(optimization(n,matrix))
    

