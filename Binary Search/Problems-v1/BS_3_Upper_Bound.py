# lowest index such that arr[index] > target
def myfunc(arr,n,target):
    left,right=0,n-1
    final=-1
    while(left<=right):
        mid=(left+right)//2
        if(arr[mid]==target):
            left=mid+1
        elif(arr[mid]>target):
            final=mid
            right=mid-1
        elif(arr[mid]<target):
            left=mid+1
    return final

arr=list(map(int,input().split()))
target=int(input())
n=len(arr)
print(myfunc(arr,n,target))
