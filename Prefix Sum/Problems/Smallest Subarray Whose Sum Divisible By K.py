def bruteForce(n,arr,k):
    mini=float('inf')
    for i in range(n):
        for j in range(i,n):
            sum=0
            for t in range(i,j+1):
                sum+=arr[t]
            if(sum%k==0):
                length=j-i+1
                mini=min(mini,length)
    return -1 if mini==float('inf') else mini

def better(n,arr,k):
    mini=float('inf')
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            if(sum%k==0):
                length=j-i+1
                mini=min(mini,length)
    return -1 if mini==float('inf') else mini

def optimized(n,arr,k):
    mini=float('inf')
    modMap={0:-1}
    sum=0
    for i in range(n):
        sum+=arr[i]
        mod=sum%k
        mod=(mod+k)%k #for negative cases
        if(mod in modMap):
            length=i-modMap[mod]
            mini=min(mini,length)
        modMap[mod]=i
    return -1 if mini==float('inf') else mini


arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteForce(n,arr,k))
print(better(n,arr,k))
print(optimized(n,arr,k))
