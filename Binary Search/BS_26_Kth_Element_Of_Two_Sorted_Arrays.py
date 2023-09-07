def bruteForce(arr1,arr2,k):
    n1=len(arr1)
    n2=len(arr2)
    if(n1>n2):
        return bruteForce(arr2,arr1,k)
    p1=0
    p2=0
    current=-1
    final=-1
    while(p1<n1 and p2<n2):
        if(arr1[p1]<=arr2[p2]):
            current+=1
            final=arr1[p1]
            p1+=1
        else:
            current+=1
            final=arr2[p1]
            p2+=1
        if(current==k-1):
            return final
    while(p1<n1):
        final=arr1[p1]
        current+=1
        p1+=1
        if(current==k-1):
            return final

    while(p2<n2):
        final=arr2[p2]
        current+=1
        p2+=1
        if(current==k-1):
            return final
    return final


def binarySearch(arr1, arr2, k):
    n1=len(arr1)
    n2=len(arr2)
    if(n1>n2):
        return binarySearch(arr2,arr1,k)
    left,right=0,n1
    while(left<=right):
        mid=(left+right)//2
        p1=mid
        p2=k-p1
        l1,l2,r1,r2=float("-inf"),float("-inf"),float("inf"),float("inf")
        if(p1-1<n1):
            l1=arr1[p1-1]
        if(p2-1<n2):
            l2=arr2[p2-1]
        if(p1<n1):
            r1=arr1[p1]
        if(p2<n2):
            r2=arr2[p2]
        if(l1<=r2 and l2<=r1):
            return max(l1,l2)
        if(l2>r1):
            left=mid+1
        else:
            right=mid-1
    return arr2[k-1]

arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
k=int(input())
print(bruteForce(arr1,arr2,k))
print(binarySearch(arr1,arr2,k))
