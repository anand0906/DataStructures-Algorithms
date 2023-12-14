#reccurance relation -> f(n)=f(n-1)+f(n-2)
#base cases -> f(0)=0, f(1)=1
#n is zero based

#TC : O(2^n)
#SC : O(n)
def recursion(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    a=recursion(n-1)
    b=recursion(n-2)
    answer=a+b
    return a+b

#TC : O(n)
#SC : O(n)
def memorization(n,memo):
    if n in memo:
        return memo[n]
    if(n<=1):
        return n
    a=memorization(n-1,memo)
    b=memorization(n-2,memo)
    answer=a+b
    memo[n]=answer
    return answer

#TC : O(n)
#SC : O(n)
def tabulation(n):
    dp=[0]*(n+1) #it is zero based indexing and we need to find nth position value
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

#TC : O(n)
#SC : O(1)
def optimization(n):
    a=0
    b=1
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c
    return b
n=int(input())
memo={}
print(recursion(n))
print(memorization(n,memo))
print(tabulation(n))
print(optimization(n))
