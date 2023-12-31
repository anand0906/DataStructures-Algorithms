'''
Base Cases :
-----------
n==0 -> target-arr[0]==0
target==0 -> True
target < 0 False

Recurrance Relation
-------------------
f(ind,target) -> f(ind-1,target-arr[ind]) or f(ind-1,target)

'''
#TC : O(2^n)
#SC : O(n)
def recursive(arr,ind,target):
    if(target==0):
        return True
    if(ind==0):
        return target-arr[0]==0
    exclude=recursive(arr,ind-1,target)
    include=False
    if(target>=arr[ind]):
        include=recursive(arr,ind-1,target-arr[ind])
    return exclude or include

#TC : O(n*k)
#SC : O(n)+O(n*k)
def memorization(arr,ind,target,memo):
    key=(ind,target)
    if key in memo:
        return memo[key]
    if(target==0):
        return True
    if(ind==0):
        return target-arr[0]==0
    exclude=memorization(arr,ind-1,target,memo)
    include=False
    if(target>=arr[ind]):
        include=memorization(arr,ind-1,target-arr[ind],memo)
    memo[key]=exclude or include
    return memo[key]

#TC : O(n*k)
#SC : O(n*k)
def tabulation(n,arr,target):
    dp=[[False for i in range(target+1)] for i in range(n)]
    for i in range(n):
        dp[i][0]=True
    if(arr[0]<=target):
        dp[0][arr[0]]=True
    for i in range(1,n):
        for j in range(1,target+1):
            exclude=dp[i-1][j]
            include=False
            if(arr[i]<=j):
                include=dp[i-1][j-arr[i]]
            dp[i][j]=include or exclude
    return dp[n-1][target]

#TC : O(n*k)
#SC : O(k)
def optimization(n,arr,target):
    dp_prev=[False for i in range(target+1)]
    dp_current=[False for i in range(target+1)]
    dp_prev[0]=True
    dp_current[0]=True
    if(arr[0]<=target):
        dp_prev[arr[0]]=True
    for i in range(1,n):
        for j in range(1,target+1):
            include,exclude=False,False
            exclude=dp_prev[j]
            if(arr[i]<=target):
                include=dp_prev[j-arr[i]]
            dp_current[j]=include or exclude
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

   
