def bruteForce(n,arr):
    return sorted(arr)

def better(n,arr):
    zeros,ones,twos=0,0,0
    for i in range(n):
        if(arr[i]==0):
            zeros+=1
        if(arr[i]==1):
            ones+=1
        if(arr[i]==2):
            twos+=1
    for i in range(zeros):
        arr[i]=0
    for j in range(zeros,zeros+ones):
        arr[j]=1
    for k in range(zeros+ones,n):
        arr[k]=2
    return arr

def optimized(n,arr):
    low,mid,high=0,0,n-1
    while mid<=high:
        if(arr[mid]==0):
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        if(arr[mid]==1):
            mid+=1
        if(arr[mid]==2):
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
            mid+=1
    return arr
        
        
arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(better(n,arr))
print(optimized(n,arr))
