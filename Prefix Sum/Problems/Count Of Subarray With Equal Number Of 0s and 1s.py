def bruteForce(n,arr):
    cnt=0
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
                cnt+=1
    return cnt
                    

def better(n,arr):
    cnt=0
    for i in range(n):
        zeros=0
        ones=0
        for j in range(i,n):
            if(arr[j]==0):
                zeros+=1
            elif(arr[j]==1):
                ones+=1
            if(zeros==ones):
                cnt+=1
    return cnt

def optimized(n,arr):
    cnt=0
    arr=[-1 if(arr[i]==0) else arr[i] for i in range(n)]
    targetSum=0
    prefixSum={0:1}
    currentSum=0
    for i in range(n):
        currentSum+=arr[i]
        rem=currentSum-targetSum
        if rem in prefixSum:
            cnt+=prefixSum[rem]
        if(currentSum in prefixSum):
            prefixSum[currentSum]+=1
        else:
            prefixSum[currentSum]=1
    return cnt

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(better(n,arr))
print(optimized(n,arr))
