from collections import defaultdict
def bruteForce(n,arr,k):
    ans=[]
    for i in range(n-k+1):
        distinct=defaultdict(lambda : 0)
        for j in range(i,i+k):
            distinct[arr[j]]+=1
        ans.append(len(distinct))
    return ans

def optimized(n,arr,k):
    ans=[]
    left,right=0,0
    count=defaultdict(lambda : 0)
    cnt=0
    while right<k:
        if arr[right] not in count:
            cnt+=1
        count[arr[right]]+=1
        right+=1
    ans.append(cnt)
    while right<n:
        if(count[arr[left]]==1):
            cnt-=1
        count[arr[left]]-=1

        if(count[arr[right]]==0):
            cnt+=1
        count[arr[right]]+=1
        ans.append(cnt)

        left+=1
        right+=1
    return ans
    
        

arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bruteForce(n,arr,k))
print(optimized(n,arr,k))
