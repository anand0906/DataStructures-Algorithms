def myfunc(arr,check,final,temp):
    if(len(temp)==len(arr)):
        final.append(temp)
        return
    else:
        for i in range(len(arr)):
            if(not check[i]):
                check[i]=True
                myfunc(arr,check,final,temp+[arr[i]])
                check[i]=False
    return final

arr=input().split()
print(myfunc(arr,[False]*len(arr),[],[]))
