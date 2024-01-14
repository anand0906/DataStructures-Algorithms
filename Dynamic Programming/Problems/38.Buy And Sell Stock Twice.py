'''
Base Cases :
------------
index==n -> 0
capacity==0 -> 0

Recurrance Relation :
-------------------
if(buy==1):
    include=-arr[index]+f(index+1,0,cap)
    exclude=f(index+1,buy,cap)
else:
    include=arr[index]+f(index+1,1,cap-1)
    exclude=f(index+1,buy,cap)
return max(include,exclude)
'''
#Tc : O(2^(n*3))
#SC : O(n)
def recursive(arr,n,index,buy,cap):
    if(index==n):
        return 0
    if(cap==0):
        return 0
    if(buy==1):
        include=-arr[index]+recursive(arr,n,index+1,0,cap)
        exclude=recursive(arr,n,index+1,buy,cap)
    else:
        include=arr[index]+recursive(arr,n,index+1,1,cap-1)
        exclude=recursive(arr,n,index+1,buy,cap)
    return max(include,exclude)

#Tc : O(2*n*3)
#SC : O(n)+O(n*2*3)
def memorization(arr,n,index,buy,cap,memo):
    key=(index,buy,cap)
    if key in memo:
        memo[key]
    if(index==n):
        return 0
    if(cap==0):
        return 0
    if(buy==1):
        include=-arr[index]+memorization(arr,n,index+1,0,cap,memo)
        exclude=memorization(arr,n,index+1,buy,cap,memo)
    else:
        include=arr[index]+memorization(arr,n,index+1,1,cap-1,memo)
        exclude=memorization(arr,n,index+1,buy,cap,memo)
    memo[key]=max(include,exclude)
    return memo[key]

#Tc : O(n*2*3)
#SC : O(n*2*3)
def tabulation(arr,n,capacity):
    dp=[[[0]*(capacity+1) for i in range(2)] for i in range(n+1)]
    for i in range(2):
        for j in range(1,capacity+1):
            dp[n][i][j]=0
    for i in range(1,n+1):
        for j in range(2):
            dp[i][j][0]=0
    for index in range(n-1,-1,-1):
        for buy in range(2):
            for cap in range(1,capacity+1):
                if(buy==1):
                    include=-arr[index]+dp[index+1][0][cap]
                    exclude=dp[index+1][buy][cap]
                else:
                    include=arr[index]+dp[index+1][1][cap-1]
                    exclude=dp[index+1][buy][cap]
                dp[index][buy][cap]=max(include,exclude)
    return dp[0][1][2]

#Tc : O(n*2*3)
#SC : O(2*3)
def optimization(arr,n,capacity):
    dp_prev=[[0]*(capacity+1) for i in range(2)]
    dp_curr=[[0]*(capacity+1) for i in range(2)] 
    for index in range(n-1,-1,-1):
        for buy in range(2):
            for cap in range(1,capacity+1):
                if(buy==1):
                    include=-arr[index]+dp_prev[0][cap]
                    exclude=dp_prev[buy][cap]
                else:
                    include=arr[index]+dp_prev[1][cap-1]
                    exclude=dp_prev[buy][cap]
                dp_curr[buy][cap]=max(include,exclude)
        dp_prev=dp_curr.copy()
    return dp_curr[1][2]

arr=list(map(int,input().split()))
n=len(arr)
cap=2
print(recursive(arr,n,0,1,cap))
memo={}
print(memorization(arr,n,0,1,cap,memo))
print(tabulation(arr,n,cap))
print(optimization(arr,n,cap))
