def bruteForce_1(vec, k):
    c=0
    p=0
    for i in vec:
        missed=i-p-1
        c+=missed
        if(k<=c):
            temp=c-k
            return p+(missed-temp)
            break
        else:
            p=i
def bruteForce_2(arr,k):
    for i in arr:
        if(i<=k):
            k+=1
        else:
            break
    return k

def binarySearch(arr,k):
    left,right=0,len(arr)-1
    final=float("-inf")
    while(left<=right):
        mid=(left+right)//2
        missing=arr[mid]-(mid+1)
        if(missing < k):
            left=mid+1
            final=max(mid,final)
        elif(missing > k):
            right=mid-1
        elif(missing == k):
            right=mid-1
    return arr[final]+(k-(arr[final]-(final+1)))
            
            
    


vec = list(map(int,input().split()))
k = int(input())
ans = bruteForce_1(vec,k)
print(bruteForce_1(vec,k))
print(binarySearch(vec,k))
