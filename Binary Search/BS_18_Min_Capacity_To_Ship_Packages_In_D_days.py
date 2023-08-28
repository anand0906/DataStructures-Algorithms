def findDays(arr,weight):
    totalDays=1
    current=0
    for i in arr:
        if(current+i > weight):
            totalDays+=1
            current=i
        else:
            current+=i
    return totalDays

def bruteForce(arr,days):
    for i in range(max(arr),sum(arr)+1):
        temp=findDays(arr,i)
        if(temp<=days):
            return i
    return -1

def binarySearch(arr,days):
    left,right=max(arr),sum(arr)
    final=float('inf')
    while(left<=right):
        mid=(left+right)//2
        temp=findDays(arr,mid)
        if(temp==days):
            final=min(final,mid)
            right=mid-1
        elif(temp<days):
            final=min(final,mid)
            right=mid-1
        else:
            left=mid+1
    return final
arr=list(map(int,input().split()))
days=int(input())
print(bruteForce(arr,days),binarySearch(arr,days))
            
            
    
    
            
