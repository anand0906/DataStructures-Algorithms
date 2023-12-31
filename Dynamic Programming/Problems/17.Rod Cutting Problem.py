'''
Base Cases :
------------
n==0 -> cost[0]*(rodSize//length[0])

Recurrance Relation :
-------------------
f(ind,rodSize) -> max(f(ind-1,rodSize),cost[ind]+f(ind,rodSize-length[ind]))

'''

#TC : O(2^rodSize)
#SC : O(N)
def recursive(ind,cost,length,rodSize):
    if(ind==0):
        return cost[0]*(rodSize//length[0])
    exclude=recursive(ind-1,cost,length,rodSize)
    include=float('-inf')
    if(length[ind]<=rodSize):
        include=cost[ind]+recursive(ind,cost,length,rodSize-length[ind])
    return max(include,exclude)

#TC : O(n*rodSize)
#SC : O(N)+O(n*rodSize)
def memorization(ind,cost,length,rodSize,memo):
    key=(ind,rodSize)
    if key in memo:
        return memo[key]
    if(ind==0):
        return cost[0]*(rodSize//length[0])
    exclude=memorization(ind-1,cost,length,rodSize,memo)
    include=float('-inf')
    if(length[ind]<=rodSize):
        include=cost[ind]+memorization(ind,cost,length,rodSize-length[ind],memo)
    memo[key]=max(include,exclude)
    return memo[key]

#TC : O(n*rodSize)
#SC : O(n*rodSize)
def tabulation(n,cost,length,rodSize):
    dp=[[0 for i in range(rodSize+1)] for i in range(n)]
    for i in range(rodSize+1):
        dp[0][i]=cost[0]*(i//length[0])
    for i in range(1,n):
        for j in range(1,rodSize+1):
            include,exclude=float('-inf'),float('-inf')
            exclude=dp[i-1][j]
            if(length[i]<=j):
                include=cost[i]+dp[i][j-length[i]]
            dp[i][j]=max(include,exclude)
    return dp[n-1][rodSize]

#TC : O(n*rodSize)
#SC : O(rodSize)
def optimization(n,cost,length,rodSize):
    dp_prev=[0 for i in range(rodSize+1)]
    dp_curr=[0 for i in range(rodSize+1)]
    for i in range(rodSize+1):
        dp_prev[i]=cost[0]*(i//length[0])
    for i in range(1,n):
        for j in range(1,rodSize+1):
            include,exclude=float('-inf'),float('-inf')
            exclude=dp_prev[j]
            if(length[i]<=j):
                include=cost[i]+dp_curr[j-length[i]]
            dp_curr[j]=max(include,exclude)
        dp_prev=dp_curr.copy()
    return dp_prev[rodSize]

n=int(input())
length=list(map(int,input().split()))
cost=list(map(int,input().split()))
rodSize=int(input())
print(recursive(n-1,cost,length,rodSize))
memo={}
print(memorization(n-1,cost,length,rodSize,memo))
print(tabulation(n,cost,length,rodSize))
print(optimization(n,cost,length,rodSize))
        
        
