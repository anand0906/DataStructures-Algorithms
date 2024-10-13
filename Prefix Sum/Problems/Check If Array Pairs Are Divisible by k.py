def bruteForce(n,arr,k):
    if(n&1):
        return False
    visited=[False]*n
    cnt=0
    for i in range(n):
        if(visited[i]):
            continue
        for j in range(i+1,n):
            if((arr[i]+arr[j])%k==0 and visited[j]==False):
                cnt+=1
                visited[j]=True
                break
    return cnt==n//2


import collections
def optimized(n,arr,k):
    if(n&1):
        return False
    prefixMod=collections.defaultdict(int)
    for i in range(n):
        mod=arr[i]%k
        mod=(mod+k)%k
        prefixMod[mod]+=1
    if(prefixMod[0]%2!=0):
        return False
    for i in range(1,k//2+1):
        if(prefixMod[i]!=prefixMod[k-i]):
            return False
    return True

arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteForce(n,arr,k))
print(optimized(n,arr,k))
