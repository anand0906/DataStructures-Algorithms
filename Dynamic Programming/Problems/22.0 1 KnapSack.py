'''
Base Cases :
-------------
n=0 -> w[0] <= weight -> v[0]
Recurrance Relation :
---------------------
f(index,weight) = max(include,exclude)
include=v[index]+f(index-1,weight-w[index])
exclude=f(index-1,weight)
'''

#TC : O(2^(N*Weight))
#SC : O(N)
def recursive(index,weight,w,v):
    if(index==0):
        if(w[index]<=weight):
            return v[index]
    exclude=recursive(index-1,weight,w,v)
    include=float('-inf')
    if(w[index]<=weight):
        include=v[index]+recursive(index-1,weight-w[index],w,v)
    return max(include,exclude)

#TC : O(N*weight)
#SC : O(N)+O(N*Weight)
def memorization(index,weight,w,v,memo):
    key=(index,weight)
    if key in memo:
        return memo[key]
    if(index==0):
        if(w[index]<=weight):
            return v[index]
    exclude=memorization(index-1,weight,w,v,memo)
    include=float('-inf')
    if(w[index]<=weight):
        include=v[index]+memorization(index-1,weight-w[index],w,v,memo)
    memo[key]=max(include,exclude)
    return memo[key]

#TC : O(N*Weight)
#SC : O(N*Weight)
def tabulation(n,weight,w,v):
    dp=[[0]*(weight+1) for i in range(n)]
    for j in range(1,weight+1):
        if(w[0]<=j):
            dp[0][j]=v[0]
    for i in range(1,n):
        for j in range(1,weight+1):
            include,exclude=float('-inf'),float('-inf')
            exclude=dp[i-1][j]
            if(w[i]<=j):
                include=v[i]+dp[i-1][j-w[i]]
            dp[i][j]=max(include,exclude)
    return dp[n-1][weight]

#TC : O(N*Weight)
#SC : O(Weight)
def optimization(n,weight,w,v):
    dp_prev=[0]*(weight+1)
    dp_curr=[0]*(weight+1)
    for j in range(1,weight+1):
        if(w[0]<=j):
            dp_prev[j]=v[0]
    for i in range(1,n):
        for j in range(1,weight+1):
            include,exclude=float('-inf'),float('-inf')
            exclude=dp_prev[j]
            if(w[i]<=j):
                include=v[i]+dp_prev[j-w[i]]
            dp_curr[j]=max(include,exclude)
        dp_prev=dp_curr.copy()
    return dp_prev[weight]
n=int(input())
w=list(map(int,input().split()))
v=list(map(int,input().split()))
weight=int(input())
print(recursive(n-1,weight,w,v))
memo={}
print(memorization(n-1,weight,w,v,memo))
print(tabulation(n,weight,w,v))
print(optimization(n,weight,w,v))
