def bruteForce(n,arr,k):
    cnt=0
    for i in range(n):
        for j in range(i,n):
            xr=0
            for l in range(i,j+1):
                xr^=arr[l]
            if(xr==k):
                cnt+=1
    return cnt

def better(n,arr,k):
    cnt=0
    for i in range(n):
        xr=0
        for j in range(i,n):
            xr^=arr[j]
            if(xr==k):
                cnt+=1
    return cnt


def optimized(n,arr,k):
    prefixCnt={0:1}
    xr=0
    cnt=0
    for i in range(n):
        xr^=arr[i]
        x=xr^k
        if x in prefixCnt:
            cnt+=prefixCnt[x]
        if xr in prefixCnt:
            prefixCnt[xr]+=1
        else:
            prefixCnt[xr]=1

    return cnt




arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteForce(n,arr,k))
print(better(n,arr,k))
print(optimized(n,arr,k))
