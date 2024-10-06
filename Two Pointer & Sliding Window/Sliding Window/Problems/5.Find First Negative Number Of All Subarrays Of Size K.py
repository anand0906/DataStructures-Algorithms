
def bruteForce(n,arr,k):
    ans=[]
    for i in range(n-k+1):
        neg=0
        for j in range(i,i+k):
            if(arr[j]<0):
                neg=arr[j]
                break
        ans.append(neg)
    return ans

from collections import deque
def optimized(n,arr,k):
    ans=[]
    q=deque()
    for i in range(k):
        if(arr[i]<0):
            q.append(i)

    for i in range(k,n):
        if(q):
            ans.append(arr[q[0]])
        else:
            ans.append(0)

        while q and q[0]<=i-k:
            q.popleft()

        if(arr[i]<0):
            q.append(i)
    ans.append(arr[q[0]] if q else 0)
    return ans
        

arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteForce(n,arr,k))
print(optimized(n,arr,k))
