import math
def findTotalHours(arr,k):
    s=0
    for i in arr:
        s=s+math.ceil(i/k)
    return s
def bruteForce(arr,h):
    for i in range(1,max(arr)+1):
        temp=findTotalHours(arr,i)
        if(temp<=h):
            return i
    return -1
def binarySearch(arr,h):
    left,right=1,max(arr)
    final=float('inf')
    while(left<=right):
        mid=(left+right)//2
        temp=findTotalHours(arr,mid)
        if(temp<=h):
            final=min(final,mid)
            right=mid-1
        else:
            left=mid+1
    return final
arr=list(map(int,input().split()))
h=int(input())
print(bruteForce(arr,h))
print(binarySearch(arr,h))
