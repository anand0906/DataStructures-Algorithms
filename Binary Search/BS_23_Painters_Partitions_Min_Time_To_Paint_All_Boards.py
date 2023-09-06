def countOfPainters(arr,time):
    cntOfPainters=1
    totalTime=0
    for i in range(len(arr)):
        if(totalTime+arr[i] <= time):
            totalTime+=arr[i]
        else:
            cntOfPainters+=1
            totalTime=arr[i]
    return cntOfPainters

def bruteForce(arr,k):
    minPossible=max(arr)
    maxPossible=sum(arr)
    for i in range(minPossible,maxPossible+1):
        temp=countOfPainters(arr,i)
        if(temp==k):
            return i
    return -1

def binarySearch(arr,k):
    left,right=max(arr),sum(arr)
    final=float('inf')
    while(left<=right):
        mid=(left+right)//2
        temp=countOfPainters(arr,mid)
        if(temp==k):
            right=mid-1
            final=min(final,mid)
        elif(temp > k):
            left=mid+1
        else:
            right=mid-1
    return final

arr=list(map(int,input().split()))
k=int(input())
print(bruteForce(arr,k))
print(binarySearch(arr,k))
            
            
    
