def myfunc(arr,n):
    left,right=0,n-1
    if(arr[left]<=arr[right]):
        return arr[left]
    final=float('inf')
    while(left<=right):
        mid=(left+right)//2
        if(arr[left]<=arr[mid]):
            final=min(arr[left],final)
            left=mid+1
        else:
            final=min(arr[mid],final)
            right=mid-1
    return final

arr=list(map(int,input().split()))
n=len(arr)
print(myfunc(arr,n))
