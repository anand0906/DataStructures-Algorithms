'''
Base Cases :
-----------
index == n -> 0
Recurrance Relation :
-------------------
f(index,last_index) =
exclude=f(index+1,last_index)
include=0
if(last_index==-1 or arr[index]>arr[last_index]):
    include=1+f(index+1,index)
return max(include,exclude)
'''

#TC : O(2^N)
#SC : O(N)
def recursive(arr,n,index,last_index):
    if(index==n):
        return 0
    exclude=recursive(arr,n,index+1,last_index)
    include=0
    if(last_index==-1 or arr[index]>arr[last_index]):
        include=1+recursive(arr,n,index+1,index)
    return max(include,exclude)

#TC : O(N^2)
#SC : O(N^2)+O(N)
def memorization(arr,n,index,last_index,memo):
    key=(index,last_index)
    if key in memo:
        return memo[key]
    if(index==n):
        return 0
    exclude=memorization(arr,n,index+1,last_index,memo)
    include=0
    if(last_index==-1 or arr[index]>arr[last_index]):
        include=1+memorization(arr,n,index+1,index,memo)
    memo[key]=max(include,exclude)
    return memo[key]

#TC : O(N^2)
#SC : O(N^2)
def tabulation(arr,n):
    dp=[[0]*(n+1) for i in range(n+1)]
    for index in range(n-1,-1,-1):
        for last_index in range(n-1,-2,-1):
            include,exclude=0,0
            exclude=dp[index+1][last_index+1]
            if(last_index==-1 or arr[index] > arr[last_index]):
                include=1+dp[index+1][index+1]
            dp[index][last_index+1]=max(include,exclude)
    return dp[0][0]

#TC : O(N^2)
#SC : O(2N)
def optmization(arr,n):
    dp_curr=[0]*(n+1)
    dp_next=[0]*(n+1)
    for index in range(n-1,-1,-1):
        for last_index in range(n-1,-2,-1):
            include,exclude=0,0
            exclude=dp_next[last_index+1]
            if(last_index==-1 or arr[index]>arr[last_index]):
                include=1+dp_next[index+1]
            dp_curr[last_index+1]=max(include,exclude)
        dp_next=dp_curr.copy()
    return dp_curr[0]

#TC : O(N^2)
#SC : O(N)
def algorithmic(arr,n):
    dp=[0]*n
    for i in range(n):
        dp[i]=1
    for index in range(1,n):
        for last_index in range(index):
            if(arr[index] > arr[last_index]):
                temp=1+dp[last_index]
                dp[index]=max(dp[index],temp)
    final=0
    for i in dp:
        final=max(final,i)
    return final

arr=list(map(int,input().split()))
n=len(arr)
print(recursive(arr,n,0,-1))
memo={}
print(memorization(arr,n,0,-1,memo))
print(tabulation(arr,n))
print(optmization(arr,n))
print(algorithmic(arr,n))

                
    
