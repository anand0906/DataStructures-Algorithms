# Search for the Insert Position where given target can be inserted
# Answer is finding lower bound
def myfunc(arr,n,target):
    left,right=0,n-1
    final=n
    while(left<=right):
        mid=(left+right)//2
        if(arr[mid]==target):
            final=mid
            right=mid-1
        elif(arr[mid] > target):
            final=mid
            right=mid-1
        elif(arr[mid] < target):
            left=mid+1
    return final;

arr=list(map(int,input().split()))
target=int(input())
n=len(arr)
print(myfunc(arr,n,target))
            
    
