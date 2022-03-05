def myfunc(arr,n,k=[]):
    if(n<0):
        return [[]]
    final=[]
    for i in arr:
        k=k+[i]
        temp=myfunc(arr,n-1,k)
        temp=[j+[i] for j in temp if j not in k]
        final.extend(temp)
    return final
arr=list(map(int,input().split()))
print(myfunc(arr,len(arr)-1))
    
