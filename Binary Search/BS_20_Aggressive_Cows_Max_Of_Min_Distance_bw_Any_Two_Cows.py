def canCowsPlaced(arr,distance,cows):
    c=1
    current=arr[0]
    for i in range(1,len(arr)):
        if(abs(arr[i]-current)>=distance):
            c+=1
            current=arr[i]
        if(c>=cows):
            return True
    return False

def bruteForce(arr,cows):
    if(len(arr)<cows):
        return -1
    minPossible=1
    maxPossible=max(arr)-min(arr)
    arr=sorted(arr)
    for k in range(minPossible,maxPossible+1):
        temp=canCowsPlaced(arr,k,cows)
        if(not temp):
            return k-1
    return maxPossible

def BinarySearch(arr,cows):
    if(len(arr)<cows):
        return -1
    left,right=1,max(arr)-min(arr)
    final=float("-inf")
    arr=sorted(arr)
    while(left<=right):
        mid=(left+right)//2
        temp=canCowsPlaced(arr,mid,cows)
        if(temp):
            left=mid+1
            final=max(final,mid)
        else:
            right=mid-1
    return final

arr=list(map(int,input().split()))
cows=int(input())
print(bruteForce(arr,cows))
print(BinarySearch(arr,cows))
        
