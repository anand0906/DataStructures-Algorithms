'''
Base Cases :
f(index,0)=True
f(0,target)=(target-arr[index])==0


Recurrance Relation :

f(index,target)=f(index-1,target-arr[index]) or f(index-1,target)

'''

def isSubsetSumEqualToK(n,arr,target):
    dp=[[False]*(target+1) for i in range(n)]
    for i in range(n):
        dp[i][0]=True
    if(target<=arr[0]):
        dp[0][arr[0]]=True
    for i in range(1,n):
        for j in range(1,target+1):
            include,exclude=False,False
            exclude=dp[i-1][j]
            if(arr[i]<=j):
                include=dp[i-1][j-arr[i]]
            dp[i][j]=include or exclude
    return dp[n-1][target]

n=int(input())
arr=list(map(int,input().split()))
totalSum=sum(arr)
if(totalSum & 1):
    print(False)
else:
    half=totalSum//2
    print(isSubsetSumEqualToK(n,arr,half))
    
