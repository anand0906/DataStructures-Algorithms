def bruteForce(n,arr,k):
    n=len(arr)
    maxi=0
    for i in range(k+1):
        leftSum=0
        for j in range(k-i):
            leftSum+=arr[j]
        rightSum=0
        for j in range(n-i,n):
            rightSum+=arr[j]
        total=leftSum+rightSum
        maxi=max(maxi,total)
    return maxi

def optimized(n,arr,k):
    leftSum,rightSum=0,0
    left,right=-1,n-1
    maxi=0
    total=0
    for i in range(k):
        left+=1
        leftSum+=arr[left]
    maxi=max(maxi,leftSum)
    for i in range(k):
        leftSum-=arr[left]
        rightSum+=arr[right]
        right-=1
        left-=1
        total=leftSum+rightSum
        maxi=max(maxi,total)
    return maxi
        
        


arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteForce(n,arr,k))
print(optimized(n,arr,k))
