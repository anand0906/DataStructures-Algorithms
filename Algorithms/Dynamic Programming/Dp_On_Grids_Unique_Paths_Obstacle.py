def myfunc(arr,m,n):
    if(m==0 and n==0):
        return 1
    if(m<0 or n<0):
        return 0
    if(arr[m][n]==1):
        return 0
    left=myfunc(arr,m-1,n)
    right=myfunc(arr,m,n-1)
    return left+right
def myfunc(arr,m,n):
    global memo
    if (m,n) in memo:
        return memo[(m,n)]
    if(m==0 and n==0):
        return 1
    if(m<0 or n<0):
        return 0
    if(arr[m][n]==1):
        return 0
    left=myfunc(arr,m-1,n)
    right=myfunc(arr,m,n-1)
    memo[(m,n)]=left+right
    return memo[(m,n)]
def tabulation(arr):
    m=len(arr)
    n=len(arr[0])
    dp=[[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if(i==0 and j==0):
                dp[i][j]=1
            elif(arr[i][j]==1):
                dp[i][j]=0
            else:
                left=0
                right=0
                if(i>0):
                    left=dp[i-1][j]
                if(j>0):
                    right=dp[i][j-1]
                dp[i][j]=left+right
    return dp[m-1][n-1]
arr=[list(map(int,input().split())) for i in range(int(input()))]
memo={}
print(myfunc(arr,len(arr)-1,len(arr[0])-1))
print(tabulation(arr))
