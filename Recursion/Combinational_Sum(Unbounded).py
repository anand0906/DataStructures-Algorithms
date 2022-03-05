def myfunc(arr,n,target,temp,total_length,sum):
    if(sum==target):
        print(temp)
        return
    if(n==total_length):
        return
    if(sum>target):
        return
    else:
        include=myfunc(arr,n,target,temp+[arr[n]],total_length,sum+arr[n])
        exclude=myfunc(arr,n+1,target,temp,total_length,sum)

arr=list(map(int,input().split()))
myfunc(arr,0,int(input()),[],len(arr),0)








def myfunc(arr,n,target,total_length,sum):
    if(sum==target):
        return [[]]
    if(sum>target):
        return False
    if(n==total_length):
        return False
    include=myfunc(arr,n,target,total_length,sum+arr[n])
    if(include!=False):
        for i in include:
            i.append(arr[n])
    exclude=myfunc(arr,n+1,target,total_length,sum)
    return include+exclude if include and exclude else include or exclude
arr=list(map(int,input().split()))
print(myfunc(arr,0,int(input()),len(arr),0))
    
