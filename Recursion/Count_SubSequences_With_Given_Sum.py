def myfunc(arr,n,sum,target,total_length):
    if(sum==target):
        return 1
    if(n==total_length):
        return 0
    include=myfunc(arr,n+1,sum+arr[n],target,total_length)
    exclude=myfunc(arr,n+1,sum,target,total_length)
    return include+exclude
arr=list(map(int,input().split()))
print(myfunc(arr,0,0,int(input()),len(arr)))
