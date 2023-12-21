#TC : O(n)
#SC : O(1)
def maxNonAdjSum(n,arr):
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
excludeFirst=maxNonAdjSum(n-2,arr[1:])
excludeLast=maxNonAdjSum(n-2,arr[:-1])
print(max(excludeFirst,excludeLast))
