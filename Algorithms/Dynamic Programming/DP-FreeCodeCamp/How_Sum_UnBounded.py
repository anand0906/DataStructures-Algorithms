def myfunc(arr,target):
    if target==0:
        return []
    if(target<0):
        return False
    for i in arr:
        temp=target-i
        ans=myfunc(arr,temp)
        if(ans!=False):
            ans.append(i)
            return ans
    return False
def myfunc(arr,target,my=[]):
    if target==0:
        return my
    if(target<0):
        return False
    for i in arr:
        temp=target-i
        ans=myfunc(arr,temp,my+[i])
        if(ans!=False):
            return ans
    return False
def myfunc(arr,target):
    global memo
    if target in memo:
        return memo[target]
    if target==0:
        return []
    if(target<0):
        return False
    for i in arr:
        temp=target-i
        ans=myfunc(arr,temp)
        if(ans!=False):
            ans.append(i)
            memo[target]=ans
            return ans
    memo[target]=False
    return False
arr=list(map(int,input().split()))
target=int(input())
memo={}
print(myfunc(arr,target))
