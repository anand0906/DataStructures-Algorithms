def findFirst(arr,n,target):
    left,right=0,n-1
    final=-1
    while (left<=right):
        mid=(left+right)//2
        if(arr[mid]==target):
            right=mid-1
            final=mid
        elif(arr[mid] > target):
            right=mid-1
        elif(arr[mid] < target):
            left=mid+1
    return final

def findLast(arr,n,target):
    left,right=0,n-1
    final=-1
    while (left<=right):
        mid=(left+right)//2
        if(arr[mid]==target):
            left=mid+1
            final=mid
        elif(arr[mid] > target):
            right=mid-1
        elif(arr[mid] < target):
            left=mid+1
    return final

arr=list(map(int,input().split()))
n=len(arr)
target=int(input())
print((findFirst(arr,n,target),findLast(arr,n,target)))
