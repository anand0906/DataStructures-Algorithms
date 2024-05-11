def bruteForce(arr,n,target):
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i]+arr[j]==target):
                return "YES"
    return "NO"


def better(arr,n,target):
    hashMap={}
    for i in range(n):
        current=arr[i]
        required=target-arr[i]
        if(hashMap.get(required)!=None):
            return "YES"
        hashMap[current]=i
    return "NO"

def optimized(arr,n,target):
    arr.sort()
    left,right=0,n-1
    while left<right:
        temp=arr[left]+arr[right]
        if(temp==target):
            return "YES"
        if(temp<target):
            left+=1
        else:
            right-=1
    return "NO"

arr=list(map(int,input().split()))
n=len(arr)
target=int(input())
print(bruteForce(arr,n,target))
print(better(arr,n,target))
print(optimized(arr,n,target))
