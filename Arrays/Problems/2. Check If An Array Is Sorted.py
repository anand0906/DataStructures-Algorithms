def bruteForce(arr,n):
    for i in range(n):
        for j in range(i,n):
            if(arr[i]>arr[j]):
                return 0
    return 1

def optimized(arr,n):
    for i in range(1,n):
        if(arr[i-1]>arr[i]):
            return 0
    return 1

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(arr,n))
print(optimized(arr,n))
