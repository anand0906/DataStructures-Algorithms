'''
Base Cases :
-----------
index==n -> 0

Recurrance Relation :
-------------------
f(index,last_index) =

exclude=f(index+1,last_index)
include=0
if(last_index==-1 or arr[index] > arr[last_index]):
    include=1+f(index+1,index)
return max(exclude,include)
'''
#TC : O(2^N)
#SC : O(N)
def recursive(arr,n,index,last_index):
    if(index==n):
        return 0

    exclude=recursive(arr,n,index+1,last_index)
    include=0
    if(last_index==-1 or arr[index]>arr[last_index]):
        include=1+recursive(arr,n,index+1,index)
    return max(include,exclude)

#TC : O(N^2)
#SC : O(N^2)
def memorization(arr,n,index,last_index,memo):
    key=(index,last_index)
    if key in memo:
        return memo[key]
    if(index==n):
        return 0
    exclude=memorization(arr,n,index+1,last_index,memo)
    include=0
    if(last_index==-1 or arr[index]>arr[last_index]):
        include=1+memorization(arr,n,index+1,index,memo)
    memo[key]=max(include,exclude)
    return memo[key]

def tabulation(arr,n):
    dp=[[0]*(n) for i in range(n+1)]
    


arr=list(map(int,input().split()))
n=len(arr)
print(recursive(arr,n,0,-1))
memo={}
print(memorization(arr,n,0,-1,memo))
