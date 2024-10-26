def bruteForce(n,arr):
    cnt=0
    for i in range(n):
        for j in range(i,n):
            for k in range(j,n):
                a=0
                b=0
                for t in range(i,j):
                    a^=arr[t]
                for t in range(j,k+1):
                    b^=arr[t]
                if(a==b and i<j<=k):
                    cnt+=1
    return cnt

def better(n,arr):
    cnt=0
    for i in range(n):
        a=0
        prev=0
        for j in range(i,n):
            prev=a
            a^=arr[j]
            b=0
            for k in range(j,n):
                b^=arr[k]
                if(prev==b and i<j<=k):
                    cnt+=1
    return cnt


def optimized(n,arr):
    target=0
    cnt=0
    prefix={0:[-1]}
    currentXor=0
    for i in range(n):
        currentXor^=arr[i]
        if currentXor in prefix:
            for j in prefix[currentXor]:
                cnt+=(i-j-1)
        if currentXor in prefix:
            prefix[currentXor]+=[i]
        else:
            prefix[currentXor]=[i]
    return cnt

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(better(n,arr))
print(optimized(n,arr))
