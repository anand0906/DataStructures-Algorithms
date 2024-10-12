def bruteForce(n,arr1,arr2,k):
    ans=0
    for i in range(n):
        for j in range(i+1,n):
            if(arr1[i]-arr1[j]<=arr2[i]-arr2[j]+k):
                ans+=1
    return ans


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
def countPairs(arr,low,mid,high,k):
    cnt=0
    l=low
    r=mid+1
    while l<=mid and r<=high:
        if arr[l]<=arr[r]+k:
            cnt+=high-r+1
            l+=1
        else:
            r+=1
    return cnt

def mergeSort(arr,low,high,k):
    cnt=0
    if(low>=high):
        return cnt
    mid=(low+high)//2
    cnt+=mergeSort(arr,low,mid,k)
    cnt+=mergeSort(arr,mid+1,high,k)
    cnt+=countPairs(arr,low,mid,high,k)
    merge(arr,low,mid,high)
    return cnt
    


def optimized(n,arr1,arr2,k):
    diffArr=[arr1[i]-arr2[i] for i in range(n)]
    ans=mergeSort(diffArr,0,n-1,k)
    return ans
    

arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
n=len(arr1)
k=int(input())
print(bruteForce(n,arr1,arr2,k))
print(optimized(n,arr1,arr2,k))
