def bruteForce(n,arr,target):
    cnt=0
    for i in range(n):
        for j in range(i,n):
            visited={}
            for k in range(i,j+1):
                if(arr[k] in visited):
                    visited[arr[k]]+=1
                else:
                    visited[arr[k]]=1
                if(visited[arr[k]]==0):
                    del visited[arr[k]]
            if(len(visited)==target):
                cnt+=1
    return cnt

def better(n,arr,target):
    cnt=0
    for i in range(n):
        visited={}
        for j in range(i,n):
            if(arr[j] in visited):
                visited[arr[j]]+=1
            else:
                visited[arr[j]]=1
            if(visited[arr[j]]==0):
                del visited[arr[j]]
            if(len(visited)==target):
                cnt+=1
    return cnt

def optimizedAtMostTarget(n,arr,target):
    cnt=0
    left,right=0,0
    visited={}
    while (right<n):
        if arr[right] in visited:
            visited[arr[right]]+=1
        else:
            visited[arr[right]]=1
        while len(visited)>target and left<=right:
            visited[arr[left]]-=1
            if(visited[arr[left]]==0):
                del visited[arr[left]]
            left+=1
        cnt+=(right-left+1)
        right+=1
    return cnt

def optimized(n,arr,target):
    tgtCnt=optimizedAtMostTarget(n,arr,target)
    tgtCnt2=optimizedAtMostTarget(n,arr,target-1)
    return tgtCnt-tgtCnt2

arr=list(map(int,input().split()))
n=len(arr)
target=int(input())
print(bruteForce(n,arr,target))
print(better(n,arr,target))
print(optimized(n,arr,target))
