'''
Base Cases : f(0)=arr[0], f(1)=max(arr[0],arr[1))
Recurrance Relation : f(n)=max(arr[n]+f(n-2),f(n-1))
'''

#TC : O(2^n)
#SC : o(n)
def recursive(n,arr):
    if(n==0):
        return arr[0]
    if(n==1):
        return max(arr[0],arr[1])
    include=arr[n]+recursive(n-2,arr)
    exclude=recursive(n-1,arr)
    answer=max(include,exclude)
    return answer

#TC : O(n)
#SC : o(n)
def memorization(n,arr,memo):
    if n in memo:
        return memo[n]
    if(n==0):
        return arr[0]
    if(n==1):
        return max(arr[0],arr[1])
    include=arr[n]+memorization(n-2,arr,memo)
    exclude=memorization(n-1,arr,memo)
    answer=max(include,exclude)
    memo[n]=answer
    return memo[n]

#TC : O(n)
#SC : o(n)
def tabulation(n,arr):
    dp=[0]*n
    dp[0]=arr[0]
    dp[1]=max(arr[0],arr[1])
    for i in range(2,n):
        include=arr[i]+dp[i-2]
        exclude=dp[i-1]
        dp[i]=max(include,exclude)
    return dp[n-1]

#TC : O(n)
#SC : o(1)
def optimization(n,arr):
    prev2=arr[0]
    prev=max(arr[0],arr[1])
    for i in range(2,n):
        include=arr[i]+prev2
        exclude=prev
        answer=max(include,exclude)
        prev2=prev
        prev=answer
    return prev


n=int(input())
arr=list(map(int,input().split()))
print(recursive(n-1,arr))
memo={}
print(memorization(n-1,arr,memo))
print(tabulation(n,arr))
print(optimization(n,arr))
