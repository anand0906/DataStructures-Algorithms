def bruteForce(arr,n):
    arr.sort()
    return arr[n-1]

def optimized(arr,n):
    large=arr[0]
    for i in range(1,n):
        current=arr[i]
        if(current>large):
            large=current
    return large

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(arr,n))
print(optimized(arr,n))
