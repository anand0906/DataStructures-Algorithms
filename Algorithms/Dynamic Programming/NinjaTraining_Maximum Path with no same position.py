n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
dp={}
def myfunc(arr,n,k):
    global dp
    if (n,k) in dp:
        return dp[(n,k)]
    if(n==0):
        temp=-float('inf')
        for i in range(len(arr[n])):
            if(i!=k):
                temp=max(temp,arr[n][i])
        return temp
    else:
        final=-float('inf')
        for i in range(len(arr[n])):
            if(i!=k):
                temp=arr[n][i]+myfunc(arr,n-1,i)
                final=max(final,temp)
        dp[(n,k)]=final
        return final
print(myfunc(arr,n-1,-1))
