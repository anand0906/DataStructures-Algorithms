def myfunc(arr,n,total_length,final,temp):
    if(n==total_length):
        final.append(sum(temp))
        return
    include=myfunc(arr,n+1,total_length,final,temp+[arr[n]])
    exclude=myfunc(arr,n+1,total_length,final,temp)
    return final
arr=list(map(int,input().split()))
print(*sorted(myfunc(arr,0,len(arr),[],[])))
        
