def bruteForce(n,arr,k):
    ans=0
    for i in range(n):
        for j in range(i+1,n):
            if(abs(arr[i]-arr[j])==k):
                ans+=1
    return ans

def optimized(n,arr,k):
    ans=0
    cntMap={}
    for i in range(n):
        diff1=arr[i]+k
        diff2=arr[i]-k
        if diff1 in cntMap:
            ans+=cntMap[diff1]
        if diff2 in cntMap:
            ans+=cntMap[diff2]
        if arr[i] in cntMap:
            cntMap[arr[i]]+=1
        else:
            cntMap[arr[i]]=1
    return ans

    

arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteForce(n,arr,k))
print(optimized(n,arr,k))
