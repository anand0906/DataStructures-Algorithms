def bruteForce(n,arr):
    maxi=float('-inf')
    for i in range(n):
        for j in range(i,n):
            temp=1
            for k in range(i,j+1):
                temp*=arr[k]
            maxi=max(maxi,temp)
    return maxi

def better(n,arr):
    maxi=float('-inf')
    for i in range(n):
        temp=1
        for j in range(i,n):
            temp*=arr[j]
            maxi=max(maxi,temp)
    return maxi

def optimized(n,arr):
    prefix,suffix,maxi=1,1,float('-inf')
    for i in range(n):
        if(prefix==0):
            prefix=1
        if(suffix==0):
            suffix=1
        prefix=prefix*(arr[i])
        suffix=suffix*(arr[n-i-1])
        maxi=max(maxi,max(prefix,suffix))
    return maxi

def optimized2(n,arr):
    currMin,currMax=1,1
    ans=max(arr)
    for i in range(n):
        if(arr[i]==0):
            currMin,currMax=1,1
            continue
        temp=currMin
        currMin=min(currMax*arr[i],currMin*arr[i],arr[i])
        currMax=max(currMax*arr[i],temp*arr[i],arr[i])
        ans=max(ans,currMax)
    return ans

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(better(n,arr))
print(optimized(n,arr))
print(optimized2(n,arr))
