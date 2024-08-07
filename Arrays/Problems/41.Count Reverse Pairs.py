def bruteForce(n,arr):
    cnt=0
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i]>2*arr[j]):
                cnt+=1
    return cnt

import math
def merge(arr,low,mid,high):
    left=low
    right=mid+1
    temp=[]
    while(left<=mid and right<=high):
        if(arr[left] <= arr[right]):
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1

    while(left<=mid):
        temp.append(arr[left])
        left+=1

    while(right<=high):
        temp.append(arr[right])
        right+=1

    for i in range(low,high+1):
        arr[i]=temp[i-low]
def countPairs(arr,low,mid,high):
    cnt=0
    right=mid+1
    for i in range(low,mid+1):
        while (right<=high and (arr[i] > (2*arr[right]))):
            right+=1
        cnt+=(right-(mid+1))
    return cnt

def mergeSort(arr,low,high):
    cnt=0
    if(low>=high):
        return cnt
    mid=math.floor((low+high)/2)
    cnt+=mergeSort(arr,low,mid)
    cnt+=mergeSort(arr,mid+1,high)
    cnt+=countPairs(arr,low,mid,high)
    merge(arr,low,mid,high)
    return cnt

def optimized(n,arr):
    low,high=0,n-1
    return mergeSort(arr,low,high)


arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(optimized(n,arr))
