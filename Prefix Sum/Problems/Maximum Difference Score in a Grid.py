
def optimized(n,m,matrix):
    ans=-float('inf')
    dp=[[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            top,left=float('inf'),float('inf')
            if(i>0):
                top=matrix[i-1][j]
            if(j>0):
                left=matrix[i][j-1]
            includeTop=dp[i-1][j]+matrix[i][j]-top
            excludeTop=matrix[i][j]-top
            includeLeft=dp[i][j-1]+matrix[i][j]-left
            excludeLeft=matrix[i][j]-left
            dp[i][j]=max(max(includeTop,excludeTop),max(includeLeft,excludeLeft))
            ans=max(ans,dp[i][j])
    return ans

n,m=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(n)]
print(optimized(n,m,matrix))
