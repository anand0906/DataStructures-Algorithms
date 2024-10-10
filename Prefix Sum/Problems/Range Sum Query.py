
def bruteForce(n,arr,q,queries):
    ans=[]
    for i in range(q):
        left,right=queries[i]
        sum=0
        for j in range(left,right+1):
            sum+=arr[j]
        ans.append(sum)
    return ans

def optimized(n,arr,q,queries):
    prefixSum=[0]*n
    for i in range(n):
        if(i==0):
            prefixSum[i]=arr[i]
            continue
        prefixSum[i]=prefixSum[i-1]+arr[i]
    ans=[]
    for i in range(q):
        left,right=queries[i]
        if(left==0):
            ans.append(prefixSum[right])
        else:
            ans.append(prefixSum[right]-prefixSum[left-1])
    return ans


arr=list(map(int,input().split()))
n=len(arr)
q=int(input())
queries=[list(map(int,input().split())) for i in range(q)]
print(bruteForce(n,arr,q,queries))
print(optimized(n,arr,q,queries))
