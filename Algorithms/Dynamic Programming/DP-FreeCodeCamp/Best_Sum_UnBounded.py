def myfunc(arr,target):
    if(target==0):
        return []
    if(target<0):
        return False
    best=False
    for i in arr:
        temp=target-i
        check=myfunc(arr,temp)
        if(check!=False):
            check.append(i)
            if(best==False):
                best=check
            elif(best and len(best)>len(check)):
                best=check
    return best

arr=list(map(int,input().split()))
target=int(input())
memo={}
print(myfunc(arr,target))

    
