def bruteForce(n,arr):
    ans=0
    for i in range(n):
        for j in range(i,n):
            mini=float('inf')
            for k in range(i,j+1):
                mini=min(mini,arr[k])
            ans+=mini
    return ans

def better(n,arr):
    ans=0
    for i in range(n):
        mini=float('inf')
        for j in range(i,n):
            mini=min(mini,arr[j])
            ans+=mini
    return ans

def optimized(n,arr):
    PSE=[-1]*n
    stack=[]
    for i in range(n):
        while stack and arr[i]<=arr[stack[-1]]:
            stack.pop()
        if stack:
            PSE[i]=stack[-1]
        stack.append(i)
    NSE=[n]*n
    stack=[]
    for i in range(n):
        while stack and arr[i]<arr[stack[-1]]:
            index=stack.pop()
            NSE[index]=i
        stack.append(i)
    ans=0
    for i in range(n):
        left=i-PSE[i]-1
        right=NSE[i]-i
        ans+=((left*right+right)*arr[i])
    return ans

def optimized2(n,arr):
    result=[0]*n
    stack=[]
    for i in range(n):
        while stack and arr[i]<=arr[stack[-1]]:
            stack.pop()
        if stack:
            prevSmaller=stack[-1]
            result[i]=result[prevSmaller]+(i-prevSmaller)*arr[i]
        else:
            result[i]=(i+1)*arr[i]
        stack.append(i)
    return sum(result)

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(better(n,arr))
print(optimized(n,arr))
print(optimized2(n,arr))
