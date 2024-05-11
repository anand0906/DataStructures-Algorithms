def bruteForce(arr,n):
    arr.sort()
    for i in range(n-1):
        if(arr[i]==arr[i+1]):
            return arr[i]
    return -1

def optimized(arr,n):
    count={i:0 for i in range(1,n+1)}
    for i in range(n):
        count[arr[i]]+=1
    for i in range(n):
        if(count[arr[i]]>1):
            return arr[i]
    return -1

def efficient(arr,n):
    slow=arr[0]
    fast=arr[0]
    while True:
        slow=arr[slow]
        fast=arr[arr[fast]]
        if(slow==fast):
            break
    fast=arr[0]
    while slow!=fast:
        slow=arr[slow]
        fast=arr[fast]
    return slow

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(arr,n))
print(optimized(arr,n))
print(efficient(arr,n))
