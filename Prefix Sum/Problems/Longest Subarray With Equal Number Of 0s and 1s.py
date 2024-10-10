def bruteForce(n,arr):
    maxi=0
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
                maxi=max(maxi,length)
    return maxi
                    

def better(n,arr):
    maxi=0
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
                maxi=max(maxi,length)
    return maxi

def optimized(n,arr):
    maxi=0
    arr=[-1 if(arr[i]==0) else arr[i] for i in range(n)]
    targetSum=0
    prefixSum={}
    currentSum=0
    for i in range(n):
        currentSum+=arr[i]
        rem=currentSum-targetSum
        if(currentSum==targetSum):
            length=i+1
            maxi=max(maxi,length)
        if rem in prefixSum:
            length=i-prefixSum[rem]
            maxi=max(maxi,length)
        if currentSum not in prefixSum:
            prefixSum[currentSum]=i
    return maxi

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(better(n,arr))
print(optimized(n,arr))
