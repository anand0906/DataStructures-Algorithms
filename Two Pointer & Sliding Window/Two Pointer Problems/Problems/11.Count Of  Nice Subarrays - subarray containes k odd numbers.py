def bruteForce(n,arr,target):
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
        
        
def optimized(n,arr,target):
    return optimizedAtMostTarget(n,arr,target)-optimizedAtMostTarget(n,arr,target-1)
    


arr=list(map(int,input().split()))
arr=[i&1 for i in arr]
n=len(arr)
target=int(input())
print(bruteForce(n,arr,target))
print(better(n,arr,target))
print(optimized(n,arr,target))
