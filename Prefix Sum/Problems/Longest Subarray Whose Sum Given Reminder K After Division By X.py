def bruteForce(n,arr,x,k):
    maxi=-1
    for i in range(n):
        for j in range(i,n):
            sum=0
            for t in range(i,j+1):
                sum+=arr[t]
            if(sum%x==k):
                length=j-i+1
                maxi=max(maxi,length)
    return maxi

def better(n,arr,x,k):
    maxi=-1
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            if(sum%x==k):
                length=j-i+1
                maxi=max(maxi,length)
    return maxi

def optimized(n,arr,x,k):
    prefixMod={}
    currentSum=0
    maxi=-1
    for i in range(n):
        currentSum+=arr[i]
        mod=currentSum%x
        mod=(mod+x)%x #for negative cases
        target=(mod-k)%x
        target=(target+x)%x #for negative cases
        if mod==target:
            length=i+1
            maxi=max(maxi,length)
        if target in prefixMod:
            length=i-prefixMod[target]
            maxi=max(maxi,length)
        if mod not in prefixMod:
            prefixMod[mod]=i
    return maxi

arr=list(map(int,input().split()))
n=len(arr)
x=int(input())
k=int(input())
print(bruteForce(n,arr,x,k))
print(better(n,arr,x,k))
print(optimized(n,arr,x,k))
