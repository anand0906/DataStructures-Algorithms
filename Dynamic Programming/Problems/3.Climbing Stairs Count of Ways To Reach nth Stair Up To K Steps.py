'''
Base Cases : 0->1 , 1->1
Recurrance Relation : f(n)=f(n-1)+f(n-2)+...+f(n-k)
'''

#TC : O(n^k)
#SC : O(n)
def recursive(n,k):
    if(n==0):
        return 1
    if(n==1):
        return 1
    total=0
    for i in range(1,k+1):
        if(n-i >= 0):
            total+=recursive(n-i,k)
    return total

#TC : O(n*k)
#SC : O(n)
def memorization(n,k,memo):
    if(n in memo):
        return memo[n]
    if(n<=1):
        return 1
    totalWays=0
    for i in range(1,k+1):
        if(n-i>=0):
            totalWays+=memorization(n-i,k,memo)
    memo[n]=totalWays
    return memo[n]

#TC : O(n*k)
#SC : O(n)
def tabulation(n,k):
    dp=[0]*(n+1)
    dp[0],dp[1]=1,1
    for i in range(2,n+1):
        totalWays=0
        for j in range(1,k+1):
            if(i-j>=0):
                totalWays+=dp[i-j]
        dp[i]=totalWays
    return dp[n]

    
n=int(input())
k=int(input())
print(recursive(n,k))
memo={}
print(memorization(n,k,memo))
print(tabulation(n,k))
