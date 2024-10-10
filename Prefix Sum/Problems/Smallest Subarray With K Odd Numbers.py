def bruteForce(n,arr,target):
    mini=n+1
    arr=[i%2 for i in arr]
    for i in range(n):
        for j in range(i,n):
            sum=0
            for k in range(i,j+1):
                sum+=arr[k]
            if(sum==target):
                length=j-i+1
                mini=min(mini,length)
    return -1 if mini==n+1 else mini

def better(n,arr,target):
    mini=n+1
    arr=[i%2 for i in arr]
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            if(sum==target):
                length=j-i+1
                mini=min(mini,length)
    return -1 if mini==n+1 else mini

def optimized(n,arr,target):
    mini=n+1
    arr=[i%2 for i in arr]
    targetSum=target
    prefixSum={}
    currentSum=0
    for i in range(n):
        currentSum+=arr[i]
        rem=currentSum-targetSum
        if(rem==0):
            length=i+1
            mini=min(mini,length)
        if rem in prefixSum:
            length=i-prefixSum[rem]
            mini=min(mini,length)
        prefixSum[currentSum]=i
    return -1 if mini==n+1 else mini
    

def optimized2(n,arr,target):
    mini=n+1
    if(target<0):
        return 0
    left,right=0,0
    currentSum=0
    oddCnt=0
    while (right<n):
        if(arr[right]%2!=0):
            oddCnt+=1
        while oddCnt>=target and left<=right:
            length=right-left+1
            mini=min(mini,length)
            if(arr[left]%2!=0):
                oddCnt-=1
            left+=1
        right+=1
    return -1 if mini==n+1 else mini
        
        


arr=list(map(int,input().split()))
n=len(arr)
target=int(input())
print(bruteForce(n,arr,target))
print(better(n,arr,target))
print(optimized(n,arr,target))
print(optimized2(n,arr,target))
