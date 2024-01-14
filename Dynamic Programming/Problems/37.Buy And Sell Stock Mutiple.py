'''
Base Cases :
------------
index == n -> 0

Recurrance Relation :
--------------------
if(buy):
    include=-arr[index]+f(index+1,~buy)
    exclude= 0 + f(index+1,buy)
else:
    include=arr[index]+f(index+1,~buy)
    exclude= 0 + f(index+1,buy)
return max(include,exclude)

'''
#TC : O(2^N)
#SC : O(N)
def recursive(arr,n,index,buy):
    if(index==n):
        return 0
    if(buy==1):
        include=-arr[index]+recursive(arr,n,index+1,0)
        exclude=recursive(arr,n,index+1,buy)
    else:
        include=arr[index]+recursive(arr,n,index+1,1)
        exclude=recursive(arr,n,index+1,buy)
    return max(include,exclude)

#TC : O(N*2)
#SC : O(N) + O(N*2)
def memorization(arr,n,index,buy,memo):
    key=(index,buy)
    if key in memo:
        return memo[key]
    if(index==n):
        return 0
    if(buy==1):
        include=-arr[index]+memorization(arr,n,index+1,0,memo)
        exclude=memorization(arr,n,index+1,buy,memo)
    else:
        include=arr[index]+memorization(arr,n,index+1,1,memo)
        exclude=memorization(arr,n,index+1,buy,memo)
    memo[key]=max(include,exclude)
    return memo[key]

#TC : O(N*2)
#SC : O(N*2)
def tabulation(arr,n):
    dp=[[0]*(n+1) for i in range(2)]
    dp[0][n]=0
    dp[1][n]=0
    for i in range(n-1,-1,-1):
        for buy in range(2):
            if(buy==1):
                include=-arr[i]+dp[0][i+1]
                exclude=dp[buy][i+1]
            else:
                include=arr[i]+dp[1][i+1]
                exclude=dp[buy][i+1]
            dp[buy][i]=max(include,exclude)
    return dp[1][0]

#TC : O(N*2)
#SC : O(2)
def optimization(arr,n):
    dp_next=[0]*2
    dp_curr=[0]*2
    for i in range(n-1,-1,-1):
        for buy in range(2):
            if(buy==1):
                include=-arr[i]+dp_next[0]
                exclude=dp_next[buy]
            else:
                include=arr[i]+dp_next[1]
                exclude=dp_next[buy]
            dp_curr[buy]=max(include,exclude)
        dp_next=dp_curr.copy()
    return dp_curr[1]


arr=list(map(int,input().split()))
n=len(arr)
print(recursive(arr,n,0,1))
memo={}
print(memorization(arr,n,0,1,memo))
print(tabulation(arr,n))
print(optimization(arr,n))

