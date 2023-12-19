#reccurance relation -> f(n)=f(n-1)+f(n-2)
#base cases -> f(0)=0, f(1)=1, f(2)=1
#n is zero based

#TC : O(2^n)
#SC : O(n)
def recursion(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    if(n==2):
        return 1
    prev=recursion(n-1)
    prev2=recursion(n-2)
    answer=prev+prev2
    return answer

#TC : O(n)
#SC : O(n)
def memorization(n,memo):
    if n in memo:
        return memo[n]
    if(n<=1):
        return n
    if(n==2):
        return 1
    prev=memorization(n-1,memo)
    prev2=memorization(n-2,memo)
    answer=prev+prev2
    memo[n]=answer
    return memo[n]

#TC : O(n)
#SC : O(n)
def tabulation(n):
    dp=[0]*(n+1) #it is zero based indexing and we need to find nth position value
    dp[0]=0
    dp[1]=1
    dp[2]=1
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

#TC : O(n)
#SC : O(1)
def optimization(n):
    prev2=1 #f(1)
    prev=1 #f(2)
    for i in range(3,n+1):
        answer=prev+prev2
        prev2=prev
        prev=answer
    return prev
n=int(input())
memo={}
print(recursion(n))
print(memorization(n,memo))
print(tabulation(n))
print(optimization(n))
