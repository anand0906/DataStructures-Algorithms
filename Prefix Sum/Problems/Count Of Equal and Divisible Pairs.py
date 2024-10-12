
def bruteForce(n,arr,k):
    ans=0
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i]==arr[j] and (i*j)%k==0):
                ans+=1
    return ans

def optimized(n,arr,k):
    ans=0
    cntMap={}
    for i in range(n):
        if(arr[i] in cntMap):
            for j in cntMap[arr[i]]:
                if(arr[i]==arr[j] and (i*j)%k==0):
                    ans+=1
        if arr[i] in cntMap:
            cntMap[arr[i]].append(i)
        else:
            cntMap[arr[i]]=[i]
    return ans

    

arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteForce(n,arr,k))
print(optimized(n,arr,k))
