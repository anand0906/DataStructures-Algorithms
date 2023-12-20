'''
Base cases  : f(0)=0 , f(1)=abs(height[1]-height[0])
Recurrance Relation : f(n)=min(f(n-1)+abs(height[n-1]-height[n]),
                                f(n-2)+abs(height[n-2]-height[n]))
'''
#TC : O(n^2)
#SP : O(n)
def recursive(n,height):
    if(n==0):
        return 0
    if(n==1):
        return abs(height[1]-height[0])
    prev=recursive(n-1,height)+abs(height[n-1]-height[n])
    prev2=recursive(n-2,height)+abs(height[n-2]-height[n])
    answer=min(prev,prev2)
    return answer

#TC : O(n)
#SP : O(n+n) height+stack
def memorization(n,height,memo):
    if n in memo:
        return memo
    if(n==0):
        return 0
    if(n==1):
        return abs(height[1]-height[0])
    prev=memorization(n-1,height,memo)+abs(height[n-1]-height[n])
    prev2=memorization(n-2,height,memo)+abs(height[n-2]-height[n])
    answer=min(prev,prev2)
    memo[n]=answer
    return answer

#TC : O(n)
#SC : O(n+n) height+dp
def tabulation(n,height):
    dp=[0]*(n)
    dp[0]=0
    dp[1]=abs(height[0]-height[1])
    for i in range(2,n):
        prev=dp[i-1]+abs(height[i-1]-height[i])
        prev2=dp[i-2]+abs(height[i-2]-height[i])
        dp[i]=min(prev,prev2)
    return dp[n-1]

#TC : O(n)
#SC : O(n) height
def optimization(n,height):
    prev2=0
    prev=abs(height[0]-height[1])
    for i in range(2,n):
        a=prev+abs(height[i-1]-height[i])
        b=prev2+abs(height[i-2]-height[i])
        answer=min(a,b)
        prev2=prev
        prev=answer
    return prev

n=int(input())
height=list(map(int,input().split()))
print(recursive(n-1,height))
memo={}
print(memorization(n-1,height,memo))
print(tabulation(n,height))
print(optimization(n,height))
