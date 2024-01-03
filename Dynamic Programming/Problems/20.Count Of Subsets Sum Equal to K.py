'''
Base Cases :
------------
n=0 -> target-arr[i]==0 -> 1
       target-arr[i]==0 -> 0
target=0 -> 1

Recurrance Relation :
--------------------
f(n,target)=include+exclude
include=f(n-1,target-arr[n])
exclude=f(n-1,target)
'''

#TC : O(2^N)
#SC : O(N)
def recursive(arr,n,target):
    if(target==0):
        return 1
    if(n==0):
        if(target-arr[n]==0):
            return 1
        else:
            return 0
    exclude=recursive(arr,n-1,target)
    include=0
    if(arr[n]<=target):
        include=recursive(arr,n-1,target-arr[n])
    return include+exclude

#TC : O(target)
#SC : O(N)+O(target*N)
def memorization(arr,n,target,memo):
    key=(n,target)
    if key in memo:
        return memo[key]
    if(target==0):
        return 1
    if(n==0):
        if(target-arr[n]==0):
            return 1
        else:
            return 0
    exclude=memorization(arr,n-1,target,memo)
    include=0
    if(arr[n]<=target):
        include=memorization(arr,n-1,target-arr[n],memo)
    memo[key]=include+exclude
    return memo[key]

#TC : O(target*N)
#SC : O(target*N)
def tabulation(n,arr,target):
    dp=[[0]*(target+1) for i in range(n)]
    for i in range(n):
        dp[i][0]=1
    if(arr[0]<=target):
        dp[0][arr[0]]=1
    for i in range(1,n):
        for j in range(1,target+1):
            include,exclude=0,0
            exclude=dp[i-1][j]
            if(arr[i]<=j):
                include=dp[i-1][j-arr[i]]
            dp[i][j]=include+exclude
    return dp[n-1][target]

#TC : O(target*N)
#SC : O(target)
def optimization(n,arr,target):
    dp_prev=[0]*(target+1)
    dp_current=[0]*(target+1)
    dp_prev[0]=1
    dp_current[0]=1
    if(arr[0]<=target):
        dp_prev[arr[0]]=1
    for i in range(1,n):
        for j in range(1,target+1):
            include,exclude=0,0
            exclude=dp_prev[j]
            if(arr[i]<=j):
                include=dp_prev[j-arr[i]]
            dp_current[j]=include+exclude
        dp_prev=dp_current.copy()
    return dp_prev[target]

n=int(input())
arr=list(map(int,input().split()))
target=int(input())
print(recursive(arr,n-1,target))
memo={}
print(memorization(arr,n-1,target,memo))
print(tabulation(n,arr,target))
print(optimization(n,arr,target))
