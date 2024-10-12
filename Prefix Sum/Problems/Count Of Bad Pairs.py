
def bruteForce(n,arr):
    cnt=0
    for i in range(n):
        for j in range(i+1,n):
            if(j-i!=arr[j]-arr[i]):
                cnt+=1
    return cnt

def optimized(n,arr):
    m=n-1
    totalCnt=m*(m+1)//2
    goodCnt=0
    cntMap={}
    for i in range(n):
        temp=i-arr[i]
        if temp in cntMap:
            goodCnt+=cntMap[temp]
            cntMap[temp]+=1
        else:
            cntMap[temp]=1
    badCnt=totalCnt-goodCnt
    return badCnt
    

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(optimized(n,arr))
