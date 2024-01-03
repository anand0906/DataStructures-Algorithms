'''
Base Cases :
------------
target=0 -> 1
n=0 -> target-arr[0]==0 -> 1
    -> target-arr[0]!=0 -> 1

Recurrance Relation :
---------------------
f(index,target)=include+exclude
include=f(index-1,target-arr[index])
exclude=f(index-1,target)
'''

#TC : O(target*N)
#SC : O(target)
def optimization(n,arr,target):
    dp_prev=[0]*(target+1)
    dp_current=[0]*(target+1)
    dp_prev[0]=1
    dp_current[0]=1
    if(arr[0]<=target):
        dp_prev[arr[0]]=1
    for i in range(1,n):
        for j in range(1,target+1):
            include,exclude=0,0
            exclude=dp_prev[j]
            if(arr[i]<=j):
                include=dp_prev[j-arr[i]]
            dp_current[j]=include+exclude
        dp_prev=dp_current.copy()
    return dp_prev[target]

n=int(input())
arr=list(map(int,input().split()))
target=int(input())
totalSum=sum(arr)
if((totalSum-target)<0 or (totalSum-target)&1):
    print(0)
else:
    temp=(totalSum-target)//2
    print(optimization(n,arr,temp))
