
def bruteForce(n,arr,k):
    total=sum(arr)
    if(total%k==0):
        return 0
    mini=n
    for i in range(n):
        for j in range(i,n):
            subSum=0
            for t in range(i,j+1):
                subSum+=arr[t]
            if((total-subSum)%k==0):
                length=j-i+1
                print(arr[i:j+1])
                mini=min(mini,length)
    if(mini==n):
        return -1
    else:
        return mini

def better(n,arr,k):
    total=sum(arr)
    if(total%k==0):
        return 0
    mini=n
    for i in range(n):
        subSum=0
        for j in range(i,n):
            subSum+=arr[j]
            if((total-subSum)%k==0):
                length=j-i+1
                mini=min(mini,length)
    if(mini==n):
        return -1
    else:
        return mini

def optimized(n,arr,k):
    total=sum(arr)
    targetSum=total%k
    if(targetSum==0):
        return 0
    mini=n
    prefixMod={0:-1}
    currentSum=0
    for i in range(n):
        currentSum+=arr[i]
        mod=currentSum%k
        mod=(mod+k)%k
        neededMod=(currentSum-targetSum)%k
        neededMod=(neededMod+k)%k
        if neededMod in prefixMod:
            length=i-prefixMod[neededMod]
            mini=min(mini,length)
        prefixMod[mod]=i
    if(mini==n):
        return -1
    else:
        return mini
        
      


arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteForce(n,arr,k))
print(better(n,arr,k))
print(optimized(n,arr,k))
