def bruteForce(n,arr,k):
    maxi=0
    for i in range(n):
        for j in range(i,n):
            sum=0
            for t in range(i,j+1):
                sum+=arr[t]
            if(sum%k==0):
                length=j-i+1
                maxi=max(maxi,length)
    return maxi

def better(n,arr,k):
    maxi=0
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            if(sum%k==0):
                length=j-i+1
                maxi=max(maxi,length)
    return maxi

def optimized(n,arr,k):
    maxi=0
    modMap={}
    sum=0
    for i in range(n):
        sum+=arr[i]
        mod=sum%k
        mod=(mod+k)%k #for negative cases
        if(mod==0):
            length=i+1
            maxi=max(maxi,length)
        elif(mod not in modMap):
            modMap[mod]=i
        else:
            length=i-modMap[mod]
            maxi=max(maxi,length)
    return maxi


arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteForce(n,arr,k))
print(better(n,arr,k))
print(optimized(n,arr,k))
