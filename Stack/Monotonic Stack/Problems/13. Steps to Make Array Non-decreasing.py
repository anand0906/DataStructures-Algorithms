def solve(n,arr):
    stack=[]
    maxiCnt=[0]*n
    maxi=0
    for i in range(n-1,-1,-1):
        while stack and arr[i]>arr[stack[-1]]:
            index=stack.pop()
            maxiCnt[i]=max(maxiCnt[i]+1,maxiCnt[index])
        stack.append(i)
        maxi=max(maxi,maxiCnt[i])
    return maxi
