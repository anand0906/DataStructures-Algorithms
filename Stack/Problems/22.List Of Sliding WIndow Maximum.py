
def bruteForce(n,arr,k):
    ans=[]
    for i in range(n-k+1):
        maxi=float('-inf')
        for j in range(i,i+k):
            maxi=max(maxi,arr[j])
        ans.append(maxi)
    return ans

from collections import deque 
def optimized(n,arr,k):
    if(k==1):
        return arr
    ans=[]
    dq=deque([])
    for i in range(n):
        if(dq and dq[0]<=(i-k)):
            dq.popleft()
        while dq and arr[i] > arr[dq[-1]]:
            dq.pop()
        dq.append(i)
        if(i>=k-1):
            ans.append(arr[dq[0]])
    return ans    






arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteForce(n,arr,k))
print(optimized(n,arr,k))
