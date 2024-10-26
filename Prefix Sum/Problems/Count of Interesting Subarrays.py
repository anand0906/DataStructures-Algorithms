def bruteForce(n,arr,modulo,k):
    ans=0
    for i in range(n):
        for j in range(i,n):
            cnt=0
            for t in range(i,j+1):
                if(arr[t]%modulo==k):
                    cnt+=1
            if(cnt%modulo==k):
                ans+=1
    return ans

def better(n,arr,modulo,k):
    ans=0
    for i in range(n):
        cnt=0
        for j in range(i,n):
            if(arr[j]%modulo==k):
                cnt+=1
            if(cnt%modulo==k):
                ans+=1
    return ans

def optimized(n,arr,modulo,k):
    modArr=[1 if(arr[i]%modulo==k) else 0 for i in range(n)]
    prefixMod={0:1}
    currentSum=0
    ans=0
    for i in range(n):
        currentSum+=modArr[i]
        mod=currentSum%modulo
        temp=(mod-k)%modulo
        temp=(temp+modulo)%modulo
        if(temp in prefixMod):
            ans+=prefixMod[temp]
        if(mod in prefixMod):
            prefixMod[mod]+=1
        else:
            prefixMod[mod]=1
    return ans

arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
modulo=int(input())
print(bruteForce(n,arr,modulo,k))
print(better(n,arr,modulo,k))
print(optimized(n,arr,modulo,k))
