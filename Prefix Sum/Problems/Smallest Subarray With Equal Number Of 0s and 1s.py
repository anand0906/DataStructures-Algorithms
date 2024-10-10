def bruteForce(n,arr):
    mini=n+1
    for i in range(n):
        for j in range(i,n):
            zeros=0
            ones=0
            for k in range(i,j+1):
                if(arr[k]==0):
                    zeros+=1
                elif(arr[k]==1):
                    ones+=1
            if(zeros==ones):
                length=j-i+1
                mini=min(mini,length)
    return -1 if mini==n+1 else mini
                    

def better(n,arr):
    mini=n+1
    for i in range(n):
        zeros=0
        ones=0
        for j in range(i,n):
            if(arr[j]==0):
                zeros+=1
            elif(arr[j]==1):
                ones+=1
            if(zeros==ones):
                length=j-i+1
                mini=min(mini,length)
    return -1 if mini==n+1 else mini

def optimized(n,arr):
    mini=n+1
    arr=[-1 if(arr[i]==0) else arr[i] for i in range(n)]
    targetSum=0
    prefixSum={}
    currentSum=0
    for i in range(n):
        currentSum+=arr[i]
        rem=currentSum-targetSum
        if(currentSum==targetSum):
            length=i+1
            mini=min(mini,length)
        if rem in prefixSum:
            length=i-prefixSum[rem]
            mini=min(mini,length)
        prefixSum[currentSum]=i
    return -1 if mini==n+1 else mini

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(better(n,arr))
print(optimized(n,arr))
