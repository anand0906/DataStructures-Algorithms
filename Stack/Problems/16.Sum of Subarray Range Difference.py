def bruteforce(n,arr):
    sum=0
    for i in range(n):
        for j in range(i,n):
            mini=float('inf')
            maxi=float('-inf')
            for k in range(i,j+1):
                mini=min(mini,arr[k])
                maxi=max(maxi,arr[k])
            sum+=(maxi-mini)
    return sum

def better(n,arr):
    sum=0
    for i in range(n):
        mini=float('inf')
        maxi=float('-inf')
        for j in range(i,n):
            mini=min(mini,arr[j])
            maxi=max(maxi,arr[j])
            sum+=(maxi-mini)
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

def optimizedMin(n,arr):
    nse=nextSmallerElement(n,arr)
    pse=previousSmallerOrEqualElement(n,arr)
    sum=0
    for i in range(n):
        right=nse[i]-i
        left=i-pse[i]
        sum+=(left*right*arr[i])
    return sum

def nextGreaterElement(n,arr):
    ans=[]
    stack=[]
    for i in range(n-1,-1,-1):
        if(i==n-1):
            ans.append(n)
            stack.append(i)
        else:
            while stack and arr[i]>arr[stack[-1]]:
                stack.pop()
            if(stack):
                ans.append(stack[-1])
            else:
                ans.append(n)
            stack.append(i)
    return ans[::-1]

def previousGreaterOrEqualElement(n,arr):
    ans=[]
    stack=[]
    for i in range(n):
        if(i==0):
            ans.append(-1)
            stack.append(i)
        else:
            while stack and arr[i]>=arr[stack[-1]]:
                stack.pop()
            if(stack):
                ans.append(stack[-1])
            else:
                ans.append(-1)
            stack.append(i)
    return ans

def optimizedMax(n,arr):
    nse=nextGreaterElement(n,arr)
    pse=previousGreaterOrEqualElement(n,arr)
    sum=0
    for i in range(n):
        right=nse[i]-i
        left=i-pse[i]
        sum+=(left*right*arr[i])
    return sum

def optimized(n,arr):
    return optimizedMax(n,arr)-optimizedMin(n,arr)

arr=list(map(int,input().split()))
n=len(arr)
print(bruteforce(n,arr))
print(better(n,arr))
print(optimized(n,arr))
