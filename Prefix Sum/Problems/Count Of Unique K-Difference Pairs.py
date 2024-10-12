
def bruteForce(n,arr,k):
    ans=set()
    for i in range(n):
        for j in range(i+1,n):
            if(abs(arr[i]-arr[j])==k):
                ans.add(tuple(sorted([arr[i],arr[j]])))
    return len(ans)

def better(n,arr,k):
    ans=set()
    cntMap={}
    for i in range(n):
        diff1=arr[i]+k
        diff2=arr[i]-k
        if diff1 in cntMap:
            ans.add(tuple(sorted([diff1,arr[i]])))
        if diff2 in cntMap:
            ans.add(tuple(sorted([diff2,arr[i]])))
        if arr[i] not in cntMap:
            cntMap[arr[i]]=1
    return len(ans)

def optimized(n,arr,k):
    cnt=0
    cntMap={i:0 for i in arr}
    for i in arr:
        cntMap[i]+=1
    for element in cntMap:
        if k==0:
            if(cntMap[element]>=2):
                cnt+=1
        else:
            if(element+k in cntMap):
                cnt+=1
    return cnt
    

arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteForce(n,arr,k))
print(better(n,arr,k))
print(optimized(n,arr,k))
