def bruteforce(n,arr):
    sum=0
    for i in range(n):
        for j in range(i,n):
            mini=float('inf')
            for k in range(i,j+1):
                mini=min(mini,arr[k])
            sum+=mini
    return sum

def better(n,arr):
    sum=0
    for i in range(n):
        mini=float('inf')
        for j in range(i,n):
            mini=min(mini,arr[j])
            sum+=mini
    return sum

def nextSmallerElement(n,arr):
    ans=[]
    stack=[]
    for i in range(n-1,-1,-1):
        if(i==n-1):
            ans.append(n)
            stack.append(i)
        else:
            while stack and arr[i]<=arr[stack[-1]]:
                stack.pop()
            if(stack):
                ans.append(stack[-1])
            else:
                ans.append(n)
            stack.append(i)
    return ans[::-1]

def previousSmallerOrEqualElement(n,arr):
    ans=[]
    stack=[]
    for i in range(n):
        if(i==0):
            ans.append(-1)
            stack.append(i)
        else:
            while stack and arr[i]<arr[stack[-1]]:
                stack.pop()
            if(stack):
                ans.append(stack[-1])
            else:
                ans.append(-1)
            stack.append(i)
    return ans

def optimized(n,arr):
    nse=nextSmallerElement(n,arr)
    pse=previousSmallerOrEqualElement(n,arr)
    sum=0
    for i in range(n):
        right=nse[i]-i
        left=i-pse[i]
        sum+=(left*right*arr[i])
    return sum

arr=list(map(int,input().split()))
n=len(arr)
print(bruteforce(n,arr))
print(better(n,arr))
print(optimized(n,arr))
