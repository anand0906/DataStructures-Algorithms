#reccurance relation : f(n)=f(n-1)+f(n-2)
#Base Cases : f(0)=1, f(1)=1, f(2)=2

#TC : O(2^n)
#SC : O(n)
def recursive(n):
    if(n<=1):
        return 1
    if(n==2):
        return 2
    a=recursive(n-1)
    b=recursive(n-2)
    answer=a+b
    return a+b

#TC : O(n)
#SC : O(n)
def memorization(n,memo):
    if(n in memo):
        return memo[n]
    if(n<=1):
        return 1
    if(n==2):
        return 2
    a=memorization(n-1,memo)
    b=memorization(n-2,memo)
    answer=a+b
    memo[n]=a+b
    return answer

#TC : O(n)
#SC : O(n)
def tabulation(n):
    dp=[0]*(n+1) #it is zero based indexing and we need to find nth position value
    dp[0]=1
    dp[1]=1
    dp[2]=2
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

#TC : O(n)
#SC : O(1)
def optimization(n):
    a=1
    b=1
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c
    return b

n=int(input())
memo={}
print(recursive(n))
print(memorization(n,memo))
print(tabulation(n))
print(optimization(n))
