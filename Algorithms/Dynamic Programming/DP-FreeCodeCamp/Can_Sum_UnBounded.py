def myfunc(arr,target):
    if(target==0):
        return True
    if(target<0):
        return False
    for i in arr:
        temp=myfunc(arr,target-i)
        if(temp==True):
            return True
    return False
def myfunc(arr,target):
    global memo
    if target in memo:
        return memo[target]
    if(target==0):
        return True
    if(target<0):
        return False
    for i in arr:
        temp=myfunc(arr,target-i)
        if(temp==True):
            memo[target]=True
            return memo[target]
    memo[target]=False
    return memo[target]
        
arr=list(map(int,input().split()))
target=int(input())
memo={}
print(myfunc(arr,target))
