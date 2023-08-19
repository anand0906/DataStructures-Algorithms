def myfunc(arr,n):
    if(n==1):
        return arr[0]
    if(arr[0]>arr[1]):
        return arr[0]
    if(arr[n-1]>arr[n-2]):
        return arr[n-1]
    left,right=1,n-2
    while(left<=right):
        mid=(left+right)//2
        if(arr[mid-1]<arr[mid]>arr[mid+1]):
            return arr[mid]
        if(arr[mid]>arr[mid-1]):
            left=mid+1
        #if(arr[mid]<arr[mid-1]):
        else:
            right=mid-1
    return -1

arr=list(map(int,input().split()))
n=len(arr)
print(myfunc(arr,n))
