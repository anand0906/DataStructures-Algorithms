'''
Base Cases :
target=0 -> 1
n=0 -> target % arr[0]==0 -> 1
    -> target % arr[0]==0 -> 0

Recurrance Relation :
f(index,target)=include+exclude
include=1+f(index,target-arr[index])
exclude=f(index-1,target)
'''
#TC : O(2^(N*Target))
#SC : O(N*Target)
def recursive(index,arr,target):
    if(target==0):
        return 1
    if(index==0):
        if(target%arr[0]==0):
            return 1
        else:
            return 0
    exclude=recursive(index-1,arr,target)
    include=0
    if(arr[index]<=target):
        include=recursive(index,arr,target-arr[index])
    return include+exclude

#TC : O(N*Target)
#SC : O(N*Target)
def memorization(index,arr,target,memo):
    key=(index,target)
    if key in memo:
        return memo[key]
    if(target==0):
        return 1
    if(index==0):
        if(target%arr[0]==0):
            return 1
        else:
            return 0
    exclude=recursive(index-1,arr,target)
    include=0
    if(arr[index]<=target):
        include=recursive(index,arr,target-arr[index])
    memo[key]=include+exclude
    return memo[key]

#TC : O(N*Target)
#SC : O(N*Target)
def tabulation(n,arr,target):
    dp=[[0]*(target+1) for i in range(n)]
    for i in range(n):
        dp[i][0]=1
    for i in range(1,target+1):
        if(i%arr[0]==0):
            dp[0][i]=1
        else:
            dp[0][i]=0
    for i in range(1,n):
        for j in range(1,target+1):
            include,exclude=0,0
            exclude=dp[i-1][j]
            if(arr[i]<=j):
                include=dp[i][j-arr[i]]
            dp[i][j]=include+exclude
    return dp[n-1][target]


#TC : O(N*Target)
#SC : O(Target)
def optimization(n,arr,target):
    dp_prev=[0]*(target+1)
    dp_curr=[0]*(target+1)
    dp_prev[0]=1
    dp_curr[0]=1
    for i in range(1,target+1):
        if(i%arr[0]==0):
            dp_prev[i]=1
        else:
            dp_prev[i]=0
    for i in range(1,n):
        for j in range(1,target+1):
            include,exclude=0,0
            exclude=dp_prev[j]
            if(arr[i]<=j):
                include=dp_curr[j-arr[i]]
            dp_curr[j]=include+exclude
        dp_prev=dp_curr.copy()
    return dp_prev[target]

n=int(input())
arr=list(map(int,input().split()))
target=int(input())
print(recursive(n-1,arr,target))
memo={}
print(memorization(n-1,arr,target,memo))
print(tabulation(n,arr,target))
print(optimization(n,arr,target))
