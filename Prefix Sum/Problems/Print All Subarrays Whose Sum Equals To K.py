def bruteForce(n,arr,k):
    ans=[]
    for i in range(n):
        for j in range(i,n):
            currentSum=0
            for t in range(i,j+1):
                currentSum+=arr[t]
            if(currentSum==k):
                ans.append(arr[i:j+1])
    return ans

def better(n,arr,k):
    ans=[]
    for i in range(n):
        currentSum=0
        for j in range(i,n):
            currentSum+=arr[j]
            if(currentSum==k):
                ans.append(arr[i:j+1])
    return ans

def optimized(n,arr,k):
    ans=[]
    prefixCnt={0:[-1]}
    currentSum=0
    for i in range(n):
        currentSum+=arr[i]
        rem=currentSum-k
        if rem in prefixCnt:
            for index in prefixCnt[rem]:
                ans.append(arr[index+1:i+1])
        if currentSum in prefixCnt:
            prefixCnt[currentSum].append(i)
        else:
            prefixCnt[currentSum]=[i]
    return ans
arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteForce(n,arr,k))
print(better(n,arr,k))
print(optimized(n,arr,k))
