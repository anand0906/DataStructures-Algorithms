def bruteForce(n,arr,k):
    maxi=-1
    for i in range(n-k):
        currentSum=0
        for j in range(i,i+k):
            currentSum+=arr[j]
        maxi=max(maxi,currentSum)
    return maxi

def optimized(n,arr,k):
    maxi=-1
    currentSum=0
    left,right=0,0
    while right<k:
        currentSum+=arr[right]
        right+=1
    maxi=max(maxi,currentSum)
    while right<n:
        currentSum+=arr[right]
        currentSum-=arr[left]
        maxi=max(maxi,currentSum)
        right+=1
        left+=1
    return maxi
    

arr=list(map(int,input().split()))
k=int(input())
n=len(arr)
print(bruteForce(n,arr,k))
print(optimized(n,arr,k))
