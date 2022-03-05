def myfunc(arr,m,n):
    if(n<0 or n>=len(arr[0])):
        return -float('inf')
    if(m==0):
        return arr[0][n]
    up=arr[m][n]+myfunc(arr,m-1,n)
    up_left=arr[m][n]+myfunc(arr,m-1,n-1)
    up_right=arr[m][n]+myfunc(arr,m-1,n+1)
    return max(up,up_left,up_right)
def myfunc(arr,m,n):
    global memo
    if (m,n) in memo:
        return memo[(m,n)]
    if(n<0 or n>=len(arr[0])):
        return -float('inf')
    if(m==0):
        return arr[0][n]
    up=arr[m][n]+myfunc(arr,m-1,n)
    up_left=arr[m][n]+myfunc(arr,m-1,n-1)
    up_right=arr[m][n]+myfunc(arr,m-1,n+1)
    memo[(m,n)]=max(up,up_left,up_right)
    return memo[(m,n)]
def tabulation(arr):
    m=len(arr)
    n=len(arr[0])
    dp=[[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        dp[0][i]=arr[0][i]
    for i in range(1,m):
        for j in range(n):
            down=arr[i][j]+dp[i-1][j]
            down_left=-float('inf')
            down_right=-float('inf')
            if(j+1<n):
                down_left=arr[i][j]+dp[i-1][j+1]
            if(j-1>=0):
                down_right=arr[i][j]+dp[i-1][j-1]
            dp[i][j]=max(down,down_left,down_right)
    return max(dp[-1])
                
arr=[list(map(int,input().split())) for i in range(int(input()))]
memo={}
final=-float('inf')
for j in range(len(arr[0])):
    k=myfunc(arr,len(arr)-1,j)
    final=max(k,final)
print(final)
print(tabulation(arr))

    
