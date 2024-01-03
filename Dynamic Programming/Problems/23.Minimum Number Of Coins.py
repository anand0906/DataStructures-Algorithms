'''
Base Cases :
target=0 ->0
n=0 -> target % arr[0]==0 -> target//arr[0]
    -> target % arr[0]==0 -> float('inf')

Recurrance Relation :
f(index,target)=min(include,exclude)
include=1+f(index,target-arr[index])
exclude=f(index-1,target)
'''
#TC : O(2^(N*Target))
#SC : O(N*Target)
def recursive(index,arr,target):
    if(target==0):
        return 0
    if(index==0):
        if(target%arr[0]==0):
            return target//arr[0]
        else:
            return float('inf')
    exclude=recursive(index-1,arr,target)
    include=float('inf')
    if(arr[index]<=target):
        include=1+recursive(index,arr,target-arr[index])
    return min(include,exclude)

#TC : O(N*Target)
#SC : O(N*Target)
def memorization(index,arr,target,memo):
    key=(index,target)
    if key in memo:
        return memo[key]
    if(target==0):
        return 0
    if(index==0):
        if(target%arr[0]==0):
            return target//arr[0]
        else:
            return float('inf')
    exclude=recursive(index-1,arr,target)
    include=float('inf')
    if(arr[index]<=target):
        include=1+recursive(index,arr,target-arr[index])
    memo[key]=min(include,exclude)
    return memo[key]

#TC : O(N*Target)
#SC : O(N*Target)
def tabulation(n,arr,target):
    dp=[[0]*(target+1) for i in range(n)]
    for i in range(1,target+1):
        if(i%arr[0]==0):
            dp[0][i]=(i//arr[0])
        else:
            dp[0][i]=float('inf')
    for i in range(1,n):
        for j in range(1,target+1):
            include,exclude=float('inf'),float('inf')
            exclude=dp[i-1][j]
            if(arr[i]<=j):
                include=1+dp[i][j-arr[i]]
            dp[i][j]=min(include,exclude)
    return dp[n-1][target]


#TC : O(N*Target)
#SC : O(Target)
def optimization(n,arr,target):
    dp_prev=[0]*(target+1)
    dp_curr=[0]*(target+1)
    for i in range(1,target+1):
        if(i%arr[0]==0):
            dp_prev[i]=(i//arr[0])
        else:
            dp_prev[i]=float('inf')
    for i in range(1,n):
        for j in range(1,target+1):
            include,exclude=float('inf'),float('inf')
            exclude=dp_prev[j]
            if(arr[i]<=j):
                include=1+dp_curr[j-arr[i]]
            dp_curr[j]=min(include,exclude)
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
