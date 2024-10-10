
def bruteForce(n,arr,q,queries):
    ans=[]
    for i in range(q):
        left,right=queries[i]
        xor=0
        for j in range(left,right+1):
            xor^=arr[j]
        ans.append(xor)
    return ans

def optimized(n,arr,q,queries):
    prefixXor=[0]*n
    for i in range(n):
        if(i==0):
            prefixXor[i]=arr[i]
            continue
        prefixXor[i]=prefixXor[i-1]^arr[i]
    ans=[]
    for i in range(q):
        left,right=queries[i]
        if(left==0):
            ans.append(prefixXor[right])
        else:
            ans.append(prefixXor[right]^prefixXor[left-1])
    return ans


arr=list(map(int,input().split()))
n=len(arr)
q=int(input())
queries=[list(map(int,input().split())) for i in range(q)]
print(bruteForce(n,arr,q,queries))
print(optimized(n,arr,q,queries))
