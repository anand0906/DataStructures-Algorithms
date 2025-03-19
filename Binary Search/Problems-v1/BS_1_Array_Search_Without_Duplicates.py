def myfunc(arr,n,target):
    left=0
    right=n-1
    while (left<=right):
        mid=(left+right)//2
        #mid=(left)-((left-right)//2) #overFlow Condition
        if(target==arr[mid]):
            return mid
        elif(target > arr[mid]):
            left=mid+1
        elif(target < arr[mid]):
            right=mid-1
    return -1

def myfun(arr,left,right):
    if(left>right):
        return -1
    mid=(left+right)//2
    #mid=(left)-((left-right)//2) #overFlow Condition
    if(arr[mid]==target):
        return mid
    elif(target>arr[mid]):
        return myfun(arr,mid+1,right)
    elif(target<arr[mid]):
        return myfun(arr,left,right-1)

arr=list(map(int,input().split()))
n=len(arr)
target=int(input())
print(myfunc(arr,n,target))
print(myfun(arr,0,n-1))
