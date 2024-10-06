def bruteForce(n,arr,k):
    largest=0
    for i in range(n):
        for j in range(i,n):
            sum=0
            for l in range(i,j+1):
                sum+=arr[l]
            if(sum==k):
                length=j-i+1
                largest=max(largest,length)
    return largest

def better(n,arr,k):
    largest=0
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            if(sum==k):
                length=j-i+1
                largest=max(largest,length)
    return largest

def optimized1(n,arr,k):
    prefix={}
    largest=0
    sum=0
    for i in range(n):
        sum+=arr[i]
        if(sum==k):
            largest=max(largest,i+1)
        rem=sum-k
        if(rem in prefix):
            length=i-prefix[rem]
            largest=max(largest,length)
        if sum not in prefix:
            prefix[sum]=i
    return largest

def optimized2(n,arr,k):
    largest=0
    left,right=0,0
    sum=arr[0]
    while right<n:

        while (left<=right and sum>k):
            sum-=arr[left]
            left-=1

        if(sum==k):
            length=right-left+1
            largest=max(largest,length)

        right+=1
        if(right<n):
            sum+=arr[right]
    return largest
            
            
                
    
arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteForce(n,arr,k))
print(better(n,arr,k))
print(optimized1(n,arr,k))
print(optimized2(n,arr,k))                                                                          

