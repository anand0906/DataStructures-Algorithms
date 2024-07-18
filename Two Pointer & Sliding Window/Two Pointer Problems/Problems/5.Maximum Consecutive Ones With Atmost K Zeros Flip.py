def bruteforce(n,arr,k):
    maxi=0
    for i in range(n):
        for j in range(i,n):
            zeros=0
            for t in range(i,j+1):
                if(arr[t]==0):
                    zeros+=1
            if(zeros<=k):
                length=j-i+1
                maxi=max(maxi,length)
    return maxi

def better(n,arr,k):
    maxi=0
    for i in range(n):
        zeros=0
        for j in range(i,n):
            if(arr[j]==0):
                zeros+=1
            if(zeros<=k):
                length=j-i+1
                maxi=max(maxi,length)
    return maxi

def optimized(n,arr,k):
    maxi=0
    left,right=0,0
    zeros=0
    while right<n:
        if(arr[right]==0):
            zeros+=1
        if(zeros>k):
            while (zeros>k):
                if(arr[left]==0):
                    zeros-=1
                left+=1
        length=right-left+1
        maxi=max(maxi,length)
        right+=1
    return maxi
        
                
arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteforce(n,arr,k))
print(better(n,arr,k))
print(optimized(n,arr,k))

