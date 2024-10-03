def bruteForce(n,arr,k):
    final=[]
    for i in range(n-k+1):
        maxi=float('-inf')
        for j in range(i,i+k):
            maxi=max(maxi,arr[j])
        final.append(maxi)
    return final

from collections import deque
def optimized(n,arr,k):
    final=[]
    q=deque()
    for i in range(k):
        while q and arr[i]>=arr[q[-1]]:
            q.pop()
        q.append(i)
    for i in range(k,n):
        final.append(arr[q[0]])
        while q and q[0]<=i-k:
            q.popleft()
        while q and arr[i]>=arr[q[-1]]:
            q.pop()
        q.append(i)
    final.append(arr[q[0]])
    return final
        

arr=list(map(int,input().split()))
k=int(input())
n=len(arr)
print(bruteForce(n,arr,k))
print(optimized(n,arr,k))
