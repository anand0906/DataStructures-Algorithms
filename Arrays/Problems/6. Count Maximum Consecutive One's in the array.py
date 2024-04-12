def solve(arr,n):
    currentCount=0
    maxCount=0
    for i in range(n):
        if(arr[i]==1):
            currentCount+=1
        else:
            currentCount=0
        maxCount=max(maxCount,currentCount)
    return maxCount


            
arr=list(map(int,input().split()))
n=len(arr)
print(solve(arr,n))
