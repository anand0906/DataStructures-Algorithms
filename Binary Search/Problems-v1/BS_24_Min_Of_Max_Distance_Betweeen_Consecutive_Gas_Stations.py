def bruteForce(arr,k):
    n=len(arr)
    partions=[0]*(n-1)
    for te in range(k):
        maxDiff=-1
        maxInd=-1
        for j in range(n-1):
            diff=arr[j+1]-arr[j]
            sectionLength=diff/(partions[j]+1)
            if(sectionLength > maxDiff):
                maxDiff=sectionLength
                maxInd=j
            partions[maxInd]+=1
    final=float("-inf")
    for i in range(n-1):
        diff=arr[i+1]-arr[i]
        sectionLength=diff/(partions[i]+1)
        final=max(final,sectionLength)
    return final

import heapq
def betterApproach(arr,k):
    n=len(arr)
    partions=[0]*n
    heap=[]
    for i in range(n-1):
        heapq.heappush(heap,((-1)*(arr[i+1]-arr[i]),i))
    for i in range(k):
        temp=heapq.heappop(heap)
        maxInd=temp[1]
        partions[maxInd]+=1
        initialDiff=arr[maxInd+1]-arr[maxInd]
        newLen=initialDiff/(partions[maxInd]+1)
        heapq.heappush(heap,((newLen*(-1)),maxInd))
    return heap[0][0]*(-1)

def numberOfStationsRequired(arr,dist):
    cnt=0
    n=len(arr)
    for i in range(n-1):
        diff=arr[i+1]-arr[i]
        stations=diff//dist
        if(diff == (dist*stations)):
            stations-=1
        cnt+=stations
    return cnt

def binarySearch(arr,k):
    maxDiff=float('-inf')
    for i in range(len(arr)-1):
        maxDiff=max(maxDiff,arr[i+1]-arr[i])
    left,right=0,maxDiff
    final=float("inf")
    t=(1e-6)
    while((right-left)>t):
        mid=(left+right)/2.0
        temp=numberOfStationsRequired(arr,mid)
        if(temp > k):
            left=mid
        elif(temp==k):
            final=min(final,mid)
            right=mid
        else:
            right=mid
    return final


        
    
    


arr=list(map(int,input().split()))
k=int(input())
print(bruteForce(arr,k))
print(betterApproach(arr,k))
print(binarySearch(arr,k))
