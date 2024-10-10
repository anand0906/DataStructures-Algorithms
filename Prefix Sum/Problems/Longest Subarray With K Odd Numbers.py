def bruteForce(n,arr,target):
    maxi=0
    arr=[i%2 for i in arr]
    for i in range(n):
        for j in range(i,n):
            sum=0
            for k in range(i,j+1):
                sum+=arr[k]
            if(sum==target):
                length=j-i+1
                maxi=max(maxi,length)
    return maxi

def better(n,arr,target):
    maxi=0
    arr=[i%2 for i in arr]
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            if(sum==target):
                length=j-i+1
                maxi=max(maxi,length)
    return maxi

def optimized(n,arr,target):
    maxi=0
    arr=[i%2 for i in arr]
    targetSum=target
    prefixSum={}
    currentSum=0
    for i in range(n):
        currentSum+=arr[i]
        rem=currentSum-targetSum
        if(rem==0):
            length=i+1
            maxi=max(maxi,length)
        if rem in prefixSum:
            length=i-prefixSum[rem]
            maxi=max(maxi,length)
        if currentSum not in prefixSum:
            prefixSum[currentSum]=i
    return maxi
    

def optimized2(n,arr,target):
    maxi=0
    if(target<0):
        return 0
    left,right=0,0
    currentSum=0
    oddCnt=0
    while (right<n):
        if(arr[right]%2!=0):
            oddCnt+=1
        while oddCnt>target and left<=right:
            if(arr[left]%2!=0):
                oddCnt-=1
            left+=1
        if(oddCnt==target):
            length=right-left+1
            maxi=max(maxi,length)
        right+=1
    return maxi
        
        


arr=list(map(int,input().split()))
n=len(arr)
target=int(input())
print(bruteForce(n,arr,target))
print(better(n,arr,target))
print(optimized(n,arr,target))
print(optimized2(n,arr,target))
