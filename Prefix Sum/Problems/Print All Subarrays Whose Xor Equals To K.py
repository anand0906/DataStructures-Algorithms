def bruteForce(n,arr,k):
    ans=[]
    for i in range(n):
        for j in range(i,n):
            currentXor=0
            for t in range(i,j+1):
                currentXor^=arr[t]
            if(currentXor==k):
                ans.append(arr[i:j+1])
    return sorted(ans,key=len)

def better(n,arr,k):
    ans=[]
    for i in range(n):
        currentXor=0
        for j in range(i,n):
            currentXor^=arr[j]
            if(currentXor==k):
                ans.append(arr[i:j+1])
    return sorted(ans,key=len)

def optimized(n,arr,k):
    ans=[]
    prefixCnt={0:[-1]}
    currentXor=0
    for i in range(n):
        currentXor^=arr[i]
        rem=currentXor^k
        if rem in prefixCnt:
            for index in prefixCnt[rem]:
                ans.append(arr[index+1:i+1])
        if currentXor in prefixCnt:
            prefixCnt[currentXor].append(i)
        else:
            prefixCnt[currentXor]=[i]
    return sorted(ans,key=len)
arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteForce(n,arr,k))
print(better(n,arr,k))
print(optimized(n,arr,k))
