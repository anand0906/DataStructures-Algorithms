def myfunc(arr,m,n):
    if(m==len(arr)-1):
        return arr[m][n]
    down=arr[m][n]+myfunc(arr,m+1,n)
    diag=arr[m][n]+myfunc(arr,m+1,n+1)
    return min(down,diag)
def myfunc(arr,m,n):
    global memo
    if (m,n) in memo:
        return memo[(m,n)]
    if(m==len(arr)-1):
        return arr[m][n]
    down=arr[m][n]+myfunc(arr,m+1,n)
    diag=arr[m][n]+myfunc(arr,m+1,n+1)
    memo[(m,n)]=min(down,diag)
    return memo[(m,n)]
def tabulation(arr):
    dp=[[0 for j in range(i+1)] for i in range(len(arr))]
    for i in range(len(arr[-1])):
        dp[-1][i]=arr[-1][i]
    for i in range(len(arr)-2,-1,-1):
        for j in range(i,-1,-1):
            down=dp[i+1][j]+arr[i][j]
            diag=dp[i+1][j+1]+arr[i][j]
            dp[i][j]=min(down,diag)
    return dp[0][0]
            
            
arr=[list(map(int,input().split())) for i in range(int(input()))]
memo={}
print(myfunc(arr,0,0))
print(tabulation(arr))
