def bruteForce(arr,n):
    maxi=0
    start,end=0,0
    for i in range(n):
        for j in range(i,n+1):
            currentSum=sum(arr[i:j])
            if(currentSum>maxi):
                maxi=currentSum
                start,end=i,j
    return arr[start:end]


def optimized(arr,n):
    maxi=0
    currentSum=0
    start,end=0,0
    for i in range(n):
        if(currentSum==0):
            start=i
        currentSum+=arr[i]
        if(currentSum>maxi):
            maxi=currentSum
            end=i
        if(currentSum<0):
            currentSum=0
    return arr[start:end+1]
    

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(arr,n))
print(optimized(arr,n))
