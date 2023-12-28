'''
Base Cases :
f(n-1,j)=matrix[n-1][j]
f(i<0,j<0,i>=n,j>=n)=float('-inf')
Recurrance Relation :
f(i,j)=max(matrix[i][j]+f(i+1,j),matrix[i][j]+f(i+1,j-1),matrix[i][j]+f(i+1,j+1))

'''
#TC : O(3^(n*n))
#SC : O(n*n*n)
def recursive(n,i,j,matrix):
    if(i<0 or j<0 or i>n-1 or j>n-1):
        return float('-inf')
    if(i==n-1):
        return matrix[n-1][j]
    bottom=matrix[i][j]+recursive(n,i+1,j,matrix)
    bottomLeft=matrix[i][j]+recursive(n,i+1,j-1,matrix)
    bottomRight=matrix[i][j]+recursive(n,i+1,j+1,matrix)
    answer=max(bottom,bottomLeft,bottomRight)
    return answer

#TC : O(n*n)
#SC : O(n*n)
def memorization(n,i,j,matrix,memo):
    key=(i,j)
    if key in memo:
        return memo[key]
    if(i<0 or j<0 or i>n-1 or j>n-1):
        return float('-inf')
    if(i==n-1):
        return matrix[n-1][j]
    bottom=matrix[i][j]+memorization(n,i+1,j,matrix,memo)
    bottomLeft=matrix[i][j]+memorization(n,i+1,j-1,matrix,memo)
    bottomRight=matrix[i][j]+memorization(n,i+1,j+1,matrix,memo)
    answer=max(bottom,bottomLeft,bottomRight)
    memo[key]=answer
    return memo[key]


#TC : O(n*n)
#SC : O(n*n)
def tabulation(n,matrix):
    n=len(matrix)
    dp=[[0]*n for i in range(n)]
    for i in range(n):
        dp[n-1][i]=matrix[n-1][i]
    for i in range(n-2,-1,-1):
        for j in range(n):
            bottom,bottomRight,bottomLeft=float('-inf'),float('-inf'),float('-inf')
            bottom=matrix[i][j]+dp[i+1][j]
            if(j+1<n):
                bottomRight=matrix[i][j]+dp[i+1][j+1]
            if(j-1>=0):
                bottomLeft=matrix[i][j]+dp[i+1][j-1]
            dp[i][j]=max(bottom,bottomLeft,bottomRight)
    return max(dp[0])

#TC : O(n*n)
#SC : O(n)
def optimization(n,matrix):
    n=len(matrix)
    dp_next=[0]*n
    dp_current=[0]*n
    for i in range(n):
        dp_next[i]=matrix[n-1][i]
    for i in range(n-2,-1,-1):
        for j in range(n):
            bottom,bottomRight,bottomLeft=float('-inf'),float('-inf'),float('-inf')
            bottom=matrix[i][j]+dp_next[j]
            if(j+1<n):
                bottomRight=matrix[i][j]+dp_next[j+1]
            if(j-1>=0):
                bottomLeft=matrix[i][j]+dp_next[j-1]
            dp_current[j]=max(bottom,bottomLeft,bottomRight)
        dp_next=dp_current.copy()
    return max(dp_next)

n=int(input())
matrix=[list(map(int,input().split())) for i in range(n)]
final=float('-inf')
for i in range(n):
    temp=recursive(n,0,i,matrix)
    final=max(final,temp)
print(final)
final=float('-inf')
for i in range(n):
    memo={}
    temp=memorization(n,0,i,matrix,memo)
    final=max(final,temp)
print(final)
print(tabulation(n,matrix))
print(optimization(n,matrix))
