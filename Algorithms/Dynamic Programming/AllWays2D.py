n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
def myfunc(arr,n):
    if(n<0):
        return [[]]
    k=[]
    for i in range(len(arr[n])):
        temp=myfunc(arr,n-1)
        temp=[j+[arr[n][i]] for j in temp]
        k.extend(temp)
    return k
def myfunc(arr,n):
    if(n<0):
        return 0
    final=1000000
    for i in range(len(arr[n])):
        temp=myfunc(arr,n-1)+arr[n][i]
        final=min(temp,final)
    return final
print(myfunc(arr,n-1))
