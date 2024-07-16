def bruteForce(n,arr):
    total=0
    for i in range(n):
        leftMax,rightMax=0,0
        for j in range(0,i):
            leftMax=max(leftMax,arr[j])
        for j in range(i+1,n):
            rightMax=max(rightMax,arr[j])
        currentWater=min(leftMax,rightMax)-arr[i]
        if(currentWater<0):
            continue
        total+=currentWater
    return total

def better(n,arr):
    total=0
    rightMax=[0]*n
    maxi=0
    for i in range(n-1,-1,-1):
        rightMax[i]=maxi
        maxi=max(maxi,arr[i])
    leftMax=0
    for i in range(n):
        currentWater=min(leftMax,rightMax[i])-arr[i]
        leftMax=max(leftMax,arr[i])
        if(currentWater<0):
            continue
        total+=currentWater
    return total

def optimized(n,arr):
    left,right=0,n-1
    leftMax,rightMax=0,0
    total=0
    while left<right:
        if(arr[left]<=arr[right]):
            if(arr[left] > leftMax):
                leftMax=arr[left]
            else:
                currentWater=(leftMax-arr[left])
                total+=currentWater
            left+=1
        else:
            if(arr[right]>rightMax):
                rightMax=arr[right]
            else:
                currentWater=(rightMax-arr[right])
                total+=currentWater
            right-=1
    return total
        
arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(better(n,arr))
print(optimized(n,arr))

