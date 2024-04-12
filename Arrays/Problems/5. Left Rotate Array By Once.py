def bruteForce(arr,n):
    temp=[0]*n
    for i in range(1,n):
        temp[i-1]=arr[i]
    temp[n-1]=arr[0]
    return temp
    

def optimized(arr,n):
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp
    return arr
    

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(arr,n))
print(optimized(arr,n))
