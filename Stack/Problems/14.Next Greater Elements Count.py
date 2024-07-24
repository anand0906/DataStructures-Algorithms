def bruteforce(n,arr):
    ans=[]
    for i in range(n):
        cnt=0
        for j in range(i+1,n):
            if(arr[j]>arr[i]):
                cnt+=1
        ans.append(cnt)
    return ans


arr=list(map(int,input().split()))
n=len(arr)
print(bruteforce(n,arr))
