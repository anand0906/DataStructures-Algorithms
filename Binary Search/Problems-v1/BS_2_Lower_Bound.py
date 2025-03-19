#Smallest Index such that arr[index] >= target

def myfunc(arr,n,target):
    left=0
    right=n-1
    final=-1
    while left<=right:
        mid=(left+right)//2
        """if(arr[mid]>=target):
            final=mid
            right=mid-1
        else:
            left=mid+1"""
        if(arr[mid]==target):
            final=mid
            right=mid-1
        elif(arr[mid]>target):
            final=mid
            right=mid-1
        elif(arr[mid]<target):
            left=mid+1
    return final

def myfun(arr,left,right,target,final):
    if(left>right):
        return final
    else:
        mid=(left+right)//2
        if(arr[mid]>=target):
            return myfun(arr,left,mid-1,target,mid)
        else:
            return myfun(arr,mid+1,right,target,final)

arr=list(map(int,input().split()))
target=int(input())
n=len(arr)
final=-1
print(myfunc(arr,n,target))
print(myfun(arr,0,n-1,target,final))
