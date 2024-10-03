def bruteForce(n,arr,k):
    total=0
    for i in range(n-k+1):
        mini,maxi=float('inf'),float('-inf')
        for j in range(i,i+k):
            mini=min(mini,arr[j])
            maxi=max(maxi,arr[j])
        total+=(mini+maxi)
    return total

from collections import deque
def optimized(n,arr,k):
    total=0
    smaller=deque()
    greater=deque()
    for i in range(k):
        while smaller and arr[i]<=arr[smaller[-1]]:
            smaller.pop()
        while greater and arr[i]>=arr[greater[-1]]:
            greater.pop()
        smaller.append(i)
        greater.append(i)
    for i in range(k,n):
        total+=(arr[smaller[0]]+arr[greater[0]])
        while smaller and smaller[0]<=i-k:
            smaller.popleft()

        while greater and greater[0]<=i-k:
            greater.popleft()
            
        while smaller and arr[i]<=arr[smaller[-1]]:
            smaller.pop()
        while greater and arr[i]>=arr[greater[-1]]:
            greater.pop()
        smaller.append(i)
        greater.append(i)
    total+=(arr[smaller[0]]+arr[greater[0]])
    return total
    
    

arr=list(map(int,input().split()))
k=int(input())
n=len(arr)
print(bruteForce(n,arr,k))
print(optimized(n,arr,k))
