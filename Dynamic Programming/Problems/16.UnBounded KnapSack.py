'''
Base Cases :
n==0 -> (cost[0])*(currentWeight//weight[0])

Recurrance Relation :
f(ind,weight) -> max(f(ind-1,currentWeight),cost[ind]+f(ind-1,currentWeight-weight[ind]))

'''

#TC : O(2^n)
#SC : O(N)
def recursive(ind,cost,weight,currentWeight):
    if(ind==0):
        return (cost[0])*(currentWeight//weight[ind])
    exclude=recursive(ind-1,cost,weight,currentWeight)
    include=float('-inf')
    if(weight[ind]<=currentWeight):
        include=cost[ind]+recursive(ind,cost,weight,currentWeight-weight[ind])
    return max(exclude,include)

#TC : O(N*W)
#SC : O(N)+O(N*W)
def memorization(ind,cost,weight,currentWeight,memo):
    key=(ind,currentWeight)
    if key in memo:
        return memo[key]
    if(ind==0):
        return (cost[0])*(currentWeight//weight[ind])
    exclude=memorization(ind-1,cost,weight,currentWeight,memo)
    include=float('-inf')
    if(weight[ind]<=currentWeight):
        include=cost[ind]+memorization(ind,cost,weight,currentWeight-weight[ind],memo)
    memo[key]=max(exclude,include)
    return memo[key]

#TC : O(N*W)
#SC : O(N*W)
def tabulation(n,weight,cost,currentWeight):
    dp=[[0 for i in range(currentWeight+1)] for i in range(n)]
    for i in range(1,currentWeight+1):
        dp[0][i]=(i//weight[0])*cost[0]
    for i in range(1,n):
        for j in range(1,currentWeight+1):
            include,exclude=float('-inf'),float('-inf')
            exclude=dp[i-1][j]
            if(weight[i]<=j):
                include=cost[i]+dp[i][j-weight[i]]
            dp[i][j]=max(include,exclude)
    return dp[n-1][currentWeight]

#TC : O(N*W)
#SC : O(W)
def optimization(n,weight,cost,currentWeight):
    dp_prev=[0 for i in range(currentWeight+1)]
    dp_curr=[0 for i in range(currentWeight+1)]
    for i in range(1,currentWeight+1):
        dp_prev[i]=(i//weight[0])*cost[0]
    for i in range(1,n):
        for j in range(1,currentWeight+1):
            include,exclude=float('-inf'),float('-inf')
            exclude=dp_prev[j]
            if(weight[i]<=j):
                include=cost[i]+dp_curr[j-weight[i]]
            dp_curr[j]=max(include,exclude)
        dp_prev=dp_curr.copy()
    return dp_prev[currentWeight]
            
    

n=int(input())
weight=list(map(int,input().split()))
cost=list(map(int,input().split()))
currentWeight=int(input())
print(recursive(n-1,cost,weight,currentWeight))
memo={}
print(memorization(n-1,cost,weight,currentWeight,memo))
print(tabulation(n,weight,cost,currentWeight))
print(optimization(n,weight,cost,currentWeight))
