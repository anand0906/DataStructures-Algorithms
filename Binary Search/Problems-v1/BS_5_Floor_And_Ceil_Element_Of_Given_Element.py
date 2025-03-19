"""The floor of x is the largest element in the array which is smaller than or equal to x.
The ceiling of x is the smallest element in the array greater than or equal to x."""
def getCeil(arr,n,target):
    left,right=0,n-1
    floor=float('inf')
    while(left<=right):
        mid=(left+right)//2
        if(arr[mid]>=target):
            right=mid-1
            floor=arr[mid]
        else:
            left=mid+1
    return floor

def getFloor(arr,n,target):
    left,right=0,n-1
    ceil=float('inf')
    while (left<=right):
        mid=(left+right)//2
        if(arr[mid]<=target):
            ceil=arr[mid]
            left=mid+1
        else:
            right=mid-1
    return ceil

arr=list(map(int,input().split()))
target=int(input())
n=len(arr)
print("Floor of",target,getFloor(arr,n,target))
print("Ceil of",target,getCeil(arr,n,target))

    
