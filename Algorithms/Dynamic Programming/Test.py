def memorize(arr,n):
    if(n<0):
        return [[]]
    else:
        include=[i+[arr[n]] for i in memorize(arr,n-1)]
        exclude=memorize(arr,n-1)
        return include+exclude
arr=list(map(int,input().split()))
print(memorize(arr,len(arr)-1))
