def countOfPartians(arr,sum):
    count=1
    currentSum=arr[0]
    for i in range(1,len(arr)):
        if(currentSum+arr[i] <=sum):
            currentSum+=arr[i]
        else:
            count+=1
            currentSum=arr[i]
    return count

def bruteForce(arr,k):
    minPossible=max(arr)
    maxPossible=sum(arr)
    for i in range(minPossible,maxPossible+1):
        cnt=countOfPartians(arr,i)
        if(cnt==k):
            return i
    return -1

def binarySearch(arr,k):
    left,right=max(arr),sum(arr)
    final=float('inf')
    while(left<=right):
        mid=(left+right)//2
        cnt=countOfPartians(arr,mid)
        if(cnt == k):
            final=min(final,mid)
            right=mid-1
        elif(cnt > k):
            left=mid+1
        elif(cnt < k):
            right=mid-1
    return final

arr=list(map(int,input().split()))
k=int(input())
print(bruteForce(arr,k))
print(binarySearch(arr,k))
