def findFirst(arr,n,target):
    l,r=0,n-1
    final=-1
    while(l<=r):
        m=(l+r)//2
        if(arr[m]==target):
            final=m
            r=m-1
        elif(target > arr[m]):
            l=m+1
        elif(target < arr[m]):
            r=m-1
    return final

def findLast(arr,n,target):
    l,r=0,n-1
    final=-1
    while(l<=r):
        m=(l+r)//2
        if(arr[m]==target):
            l=m+1
            final=m
        elif(target > arr[m]):
            l=m+1
        else:
            r=m-1
    return final

arr=list(map(int,input().split()))
n=len(arr)
target=int(input())
s=findLast(arr,n,target)
e=findFirst(arr,n,target)
if(s==-1):
    print("Not Found")
else:
    print(e-s+1)
