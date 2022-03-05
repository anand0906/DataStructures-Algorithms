def myfunc(arr,n,temp,k):
    if(n==k):
        print(temp)
        return
    else:
        exclude=myfunc(arr,n+1,temp,k)
        include=myfunc(arr,n+1,temp+[arr[n]],k)
arr=input().split()
myfunc(arr,0,[],len(arr))
def myfunc(arr,n,temp,k):
    if(n==k):
        return [[]]
    else:
        exclude=myfunc(arr,n+1,temp,k)
        include=myfunc(arr,n+1,temp+[arr[n]],k)
        for i in include:
            i.append(arr[n])
        return include+exclude
print(myfunc(arr,0,[],len(arr)))
