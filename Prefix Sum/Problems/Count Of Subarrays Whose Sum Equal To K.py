def bruteForce(n,arr,k):
    cnt=0
    for i in range(n):
        for j in range(i,n):
            s=0
            for l in range(i,j+1):
                s+=arr[l]
            if(s==k):
                cnt+=1
    return cnt

def better(n,arr,k):
    cnt=0
    for i in range(n):
        s=0
        for j in range(i,n):
            s+=arr[j]
            if(s==k):
                cnt+=1
    return cnt


def optimized(n,arr,k):
    prefixCnt={0:1}
    s=0
    cnt=0
    for i in range(n):
        s+=arr[i]
        rem=s-k
        if rem in prefixCnt:
            cnt+=prefixCnt[rem]
        if s in prefixCnt:
            prefixCnt[s]+=1
        else:
            prefixCnt[s]=1

    return cnt




arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteForce(n,arr,k))
print(better(n,arr,k))
print(optimized(n,arr,k))
