def bruteForceLeftShift(arr,n,k):
    k=k%n
    for j in range(k):
        temp=arr[0]
        for i in range(n-1):
            arr[i]=arr[i+1]
        arr[n-1]=temp
    return arr

def bruteForceRightShift(arr,n,k):
    k=k%n
    for j in range(k):
        temp=arr[n-1]
        for i in range(n-1,0,-1):
            arr[i]=arr[i-1]
        arr[0]=temp
    return arr

def betterLeftShift(arr,n,k):
    temp=[]
    k=k%n
    for i in range(k):
        temp.append(arr[i])
    for i in range(k,n):
        arr[i-k]=arr[i]
    j=0
    for i in range(n-k,n):
        arr[i]=temp[j]
        j+=1
    return arr

def betterRightShift(arr,n,k):
    temp=[]
    k=k%n
    for i in range(n-k,n):
        temp.append(arr[i])
    for i in range(n-1,n-k-1,-1):
        arr[i]=arr[i-k]
    j=0
    for i in range(k):
        arr[i]=temp[j]
        j+=1
    return arr
        
    
    
    

arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteForceLeftShift(arr.copy(),n,k))
print(bruteForceRightShift(arr.copy(),n,k))
print(betterLeftShift(arr.copy(),n,k))
print(betterRightShift(arr.copy(),n,k))
