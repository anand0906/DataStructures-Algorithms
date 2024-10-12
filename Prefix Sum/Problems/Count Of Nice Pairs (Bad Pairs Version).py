
def bruteForce(n,arr):
    cnt=0
    revArr=[int(str(i)[::-1]) for i in arr]
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i]+revArr[j]==arr[j]+revArr[i]):
                cnt+=1
    return cnt

def optimized(n,arr):
    revArr=[int(str(i)[::-1]) for i in arr]
    cnt=0
    cntMap={}
    for i in range(n):
        temp=arr[i]-revArr[i]
        if temp in cntMap:
            cnt+=cntMap[temp]
            cntMap[temp]+=1
        else:
            cntMap[temp]=1
    return cnt
    

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(optimized(n,arr))
