'''
Base cases : f(0)=0
Recurrence Relation :
f(n)=min(f(n-1)+abs(height[n-1]-height[n]),
         f(n-2)+abs(height[n-2]-height[n])
         f(n-3)+abs(height[n-3]-height[n])
         ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '
         ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '
         f(n-k)+abs(height[n-k]-height[n])
         )
'''
#TC : O((k^n))
#SC : O(n)
def recursive(n,k,height):
    if(n==0):
        return 0
    minEnergy=float('inf')
    for i in range(1,k+1):
        if((n-i)>=0):
            temp=recursive(n-i,k,height)+abs(height[n-i]-height[n])
            minEnergy=min(minEnergy,temp)
    return minEnergy

#TC : O(n*k)
#SC : O(n)
def memorization(n,k,height,memo):
    if n in memo:
        return memo[n]
    if(n==0):
        return 0
    minEnergy=float('inf')
    for i in range(1,k+1):
        if((n-i)>=0):
            temp=memorization(n-i,k,height,memo)+abs(height[n-i]-height[n])
            minEnergy=min(minEnergy,temp)
    memo[n]=minEnergy
    return minEnergy

#TC : O(n*k)
#SC : O(n)
def tabulation(n,k,height):
    dp=[0]*n
    dp[0]=0
    for i in range(1,n):
        minEnergy=float('inf')
        for j in range(1,k+1):
            if(i-j >=0):
                temp=dp[i-j]+abs(height[i-j]-height[i])
                minEnergy=min(temp,minEnergy)
            dp[i]=minEnergy
    return dp[n-1]
n=int(input())
k=int(input())
height=list(map(int,input().split()))
print(recursive(n-1,k,height))
memo={}
print(memorization(n-1,k,height,memo))
print(tabulation(n,k,height))
