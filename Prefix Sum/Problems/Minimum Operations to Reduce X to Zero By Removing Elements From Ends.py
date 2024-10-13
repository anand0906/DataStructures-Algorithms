def longestSubarrayWithGivenSum(n,arr,target):
    prefix={}
    maxi=-1
    currentSum=0
    for i in range(n):
        currentSum+=arr[i]
        rem=currentSum-target
        if(rem==0):
            length=i+1
            maxi=max(maxi,length)
        if rem in prefix:
            length=i-prefix[rem]
            maxi=max(maxi,length)
        if currentSum not in prefix:
            prefix[currentSum]=i
    return maxi

def longestSubarrayWithGivenSumOptimized(n,arr,target):
    maxi=-1
    left,right=0,0
    currentSum=0
    while right<n:
        currentSum+=arr[right]
        while currentSum>target and left<=right:
            currentSum-=arr[left]
            left+=1
        if(currentSum==target):
            length=right-left+1
            maxi=max(maxi,length)
        right+=1
    return maxi



def better(n,arr,x):
    total=sum(arr)
    if(total==x):
        return n
    target=total-x
    length=longestSubarrayWithGivenSum(n,arr,target)
    if(length==-1):
        return -1
    ans=n-length
    return ans

def optimized(n,arr,x):
    total=sum(arr)
    if(total==x):
        return n
    target=total-x
    length=longestSubarrayWithGivenSumOptimized(n,arr,target)
    if(length==-1):
        return -1
    ans=n-length
    return ans

arr=list(map(int,input().split()))
n=len(arr)
x=int(input())
print(better(n,arr,x))
print(optimized(n,arr,x))
