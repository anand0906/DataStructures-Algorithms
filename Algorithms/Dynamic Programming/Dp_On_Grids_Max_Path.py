def myfunc(arr,m,n,sum=0):
    if(m==0 and n==0):
        return sum+arr[m][n]
    if(m<0 or n<0):
        return -float('inf')
    left=myfunc(arr,m,n-1,sum+arr[m][n])
    right=myfunc(arr,m-1,n,sum+arr[m][n])
    return max(left,right)
def myfunc(arr,m,n,sum=0):
    global memo
    key=(m,n)
    if key in memo:
        return memo[key]
    if(m==0 and n==0):
        return sum+arr[m][n]
    if(m<0 or n<0):
        return -float('inf')
    left=myfunc(arr,m,n-1,sum+arr[m][n])
    right=myfunc(arr,m-1,n,sum+arr[m][n])
    memo[key]=max(left,right)
    return memo[key]
def tabulation(arr):
    m=len(arr)
    n=len(arr[0])
    dp=[[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            if(i==0 and j==0):
                dp[i][j]=arr[i][j]
            else:
                left=-float('inf')
                right=-float('inf')
                if(j>0):
                    left=dp[i][j-1]+arr[i][j]
                if(i>0):
                    right=dp[i-1][j]+arr[i][j]
                dp[i][j]=max(left,right)
    return dp[m-1][n-1]

arr=[list(map(int,input().split())) for i in range(int(input()))]
memo={}
print(myfunc(arr,len(arr)-1,len(arr[0])-1))
print(tabulation(arr))
