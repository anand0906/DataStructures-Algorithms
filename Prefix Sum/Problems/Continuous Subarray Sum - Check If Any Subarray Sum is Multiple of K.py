def bruteForce(n,arr,k):
    for i in range(n):
        for j in range(i,n):
            sum=0
            for t in range(i,j+1):
                sum+=arr[t]
            if(sum%k==0 and j-i+1>=2):
                return True
    return False

def better(n,arr,k):
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            if(sum%k==0 and j-i+1>=2):
                return True
    return False

def optimized(n,arr,k):
    prefixMod={}
    currentSum=0
    for i in range(n):
        currentSum+=arr[i]
        mod=currentSum%k
        mod=(mod+k)%k
        if(mod==0 and (i+1>=2)):
            return True
        if mod in prefixMod and (i-prefixMod[mod]>=2):
            return True
        if mod not in prefixMod:
            prefixMod[mod]=i
    return False

arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteForce(n,arr,k))
print(better(n,arr,k))
print(optimized(n,arr,k))
