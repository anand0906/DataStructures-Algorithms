def bruteForce(n,arr,target):
    arr=[i%2 for i in arr]
    cnt=0
    for i in range(n):
        for j in range(i,n):
            sum=0
            for k in range(i,j+1):
                sum+=arr[k]
            if(sum==target):
                cnt+=1
    return cnt

def better(n,arr,target):
    arr=[i%2 for i in arr]
    cnt=0
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            if(sum==target):
                cnt+=1
            if(sum>target):
                break
    return cnt

def optimized(n,arr,target):
    arr=[i%2 for i in arr]
    cnt=0
    targetSum=target
    prefixSumCnt={0:1}
    currentSum=0
    for i in range(n):
        currentSum+=arr[i]
        rem=currentSum-targetSum
        if rem in prefixSumCnt:
            cnt+=prefixSumCnt[rem]
        if currentSum in prefixSumCnt:
            prefixSumCnt[currentSum]+=1
        else:
            prefixSumCnt[currentSum]=1
    return cnt
    

def optimizedAtMostTarget(n,arr,target):
    if(target<0):
        return 0
    cnt=0
    left,right=0,0
    currentSum=0
    while (right<n):
        currentSum+=arr[right]
        while currentSum>target and left<=right:
            currentSum-=arr[left]
            left+=1
        cnt+=(right-left+1)
        right+=1
    return cnt
        
        
def optimized2(n,arr,target):
    return optimizedAtMostTarget(n,arr,target)-optimizedAtMostTarget(n,arr,target-1)
    


arr=list(map(int,input().split()))
n=len(arr)
target=int(input())
print(bruteForce(n,arr,target))
print(better(n,arr,target))
print(optimized(n,arr,target))
print(optimized2(n,arr,target))
