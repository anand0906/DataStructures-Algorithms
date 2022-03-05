#print all subsequences
def myfunc(arr,n,sum,total_length,target,temp):
    if(n==total_length):
        if(sum==target):
            print(temp)
        return
    else:
        include=myfunc(arr,n+1,sum+arr[n],total_length,target,temp+[arr[n]])
        exclude=myfunc(arr,n+1,sum,total_length,target,temp)
#print one any one subsequencs
def myfunc(arr,n,sum,total_length,target,temp):
    if(n==total_length):
        if(sum==target):
            print(temp)
            return True
        return False
    else:
        include=myfunc(arr,n+1,sum+arr[n],total_length,target,temp+[arr[n]])
        if(include):
            return True
        exclude=myfunc(arr,n+1,sum,total_length,target,temp)
        if exclude:
            return True
        return False
arr=list(map(int,input().split()))
myfunc(arr,0,0,len(arr),int(input()),[])
