def bruteforce(n,arr):
    ans=[]
    arr.sort()
    for i in range(n):
        start,end=arr[i]
        if(ans and start <= ans[-1][1]):
            continue
        for j in range(i+1,n):
            if(arr[j][0]<=end):
                end=max(end,arr[j][1])
            else:
                break
        ans.append([start,end])
    return ans

def optimized(n,arr):
    ans=[]
    arr.sort()
    for i in range(n):
        start,end=arr[i]
        if(not ans or start>ans[-1][1]):
            ans.append([start,end])
        else:
            ans[-1][1]=max(ans[-1][1],end)
    return ans

n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
print(bruteforce(n,arr))
print(optimized(n,arr))
