import math
def findTotalBouquets(arr,k,size):
    totalBoq=0
    count=0
    for i in arr:
        if(i<=k):
            count+=1
        else:
            totalBoq+=(math.floor(count/size))
            count=0
    else:
         totalBoq+=(math.floor(count/size))
    return totalBoq

def bruteForce(arr,m,size):
    minDays,maxDays=min(arr),max(arr)
    for k in range(minDays,maxDays+1):
        temp=findTotalBouquets(arr,k,size)
        if(temp>=m):
            return k
    return -1

def binarySearch(arr,m,size):
    left,right=min(arr),max(arr)
    final=float('inf')
    while(left<=right):
        mid=(left+right)//2
        temp=findTotalBouquets(arr,mid,size)
        if(temp==m):
            final=min(final,mid)
            right=mid-1
        elif(temp>m):
            final=min(final,mid)
            right=mid-1
        else:
            left=mid+1
    return final

arr=list(map(int,input().split()))
m=int(input())
size=int(input())
print(bruteForce(arr,m,size),binarySearch(arr,m,size))
    
