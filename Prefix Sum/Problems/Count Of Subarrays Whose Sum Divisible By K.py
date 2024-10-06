def bruteForce(n,arr,k):
    cnt=0
    for i in range(n):
        for j in range(i,n):
            sum=0
            for t in range(i,j+1):
                sum+=arr[t]
            if(sum%k==0):
                cnt+=1
    return cnt

def better(n,arr,k):
    cnt=0
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            if(sum%k==0):
                cnt+=1
    return cnt

def optimized(n,arr,k):
    cnt=0
    modMap={0:1}
    sum=0
    for i in range(n):
        sum+=arr[i]
        mod=sum%k
        mod=(mod+k)%k #for negative cases
        if mod in modMap:
            cnt+=(modMap[mod])
            modMap[mod]+=1
        else:
            modMap[mod]=1
    return cnt


arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteForce(n,arr,k))
print(better(n,arr,k))
print(optimized(n,arr,k))
