def myfunc(arr):
    mini=arr[0]
    profit=0
    for i in arr:
        current=i-mini
        profit=max(profit,current)
        mini=min(i,mini)
    return profit

arr=list(map(int,input().split()))
print(myfunc(arr))
    
