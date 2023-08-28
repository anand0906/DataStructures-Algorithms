import math
def findSum(arr,divisor):
    s=0
    for i in arr:
        s+=(math.ceil(i/divisor))
    return s

def bruteForce(arr,limit):
    for i in range(1,max(arr)+1):
        temp=findSum(arr,i)
        if(temp<=limit):
            return i
    return -1

def binarySearch(arr,limit):
    left,right=1,max(arr)
    final=float('inf')
    while(left<=right):
        mid=(left+right)//2
        temp=findSum(arr,mid)
        if(temp==limit):
            right=mid-1
            final=min(final,mid)
        elif(temp<limit):
            right=mid-1
            final=min(final,mid)
        else:
            left=mid+1
    return final

arr=list(map(int,input().split()))
limit=int(input())
print(bruteForce(arr,limit),binarySearch(arr,limit))
            
    
    
