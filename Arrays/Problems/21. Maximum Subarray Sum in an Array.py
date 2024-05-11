def bruteForce(arr,n):
    maxi=0
    for i in range(n):
        for j in range(i,n+1):
            currentSum=sum(arr[i:j])
            maxi=max(maxi,currentSum)
    return maxi

def better(arr,n):
    maxi=0
    for i in range(n):
        currentSum=0
        for j in range(i,n):
            currentSum+=arr[j]
            maxi=max(maxi,currentSum)
    return maxi

def optimized(arr,n):
    maxi=0
    currentSum=0
    for i in range(n):
        currentSum+=arr[i]
        if(currentSum>maxi):
            maxi=currentSum
        if(currentSum<0):
            currentSum=0
    return maxi
    

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(arr,n))
print(better(arr,n))
print(optimized(arr,n))
