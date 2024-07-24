
def bruteForce(n,arr):
    maxArea=0
    for i in range(n):
        leftMin=-1
        rightMin=n
        for j in range(i-1,-1,-1):
            if(arr[j]<arr[i]):
                leftMin=j
                break
        for j in range(i+1,n):
            if(arr[j]<arr[i]):
                rightMin=j
                break
        area=(rightMin-leftMin-1)*arr[i]
        maxArea=max(maxArea,area)
    return maxArea
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

def previousSmallerElement(n,arr):
    ans=[]
    stack=[]
    for i in range(n):
        if(i==0):
            ans.append(-1)
            stack.append(i)
        else:
            while stack and arr[i]<=arr[stack[-1]]:
                stack.pop()
            if(stack):
                ans.append(stack[-1])
            else:
                ans.append(-1)
            stack.append(i)
    return ans

def better(n,arr):
    nse=nextSmallerElement(n,arr)
    pse=previousSmallerElement(n,arr)
    maxArea=0
    for i in range(n):
        leftMin=pse[i]
        rightMin=nse[i]
        area=(rightMin-leftMin-1)*arr[i]
        maxArea=max(maxArea,area)
    return maxArea

def optimized(n,arr):
    stack=[]
    maxArea=0
    for i in range(n):
        while stack and arr[i]<arr[stack[-1]]:
            current=arr[stack.pop()]
            rightMin=i
            if(stack):
                leftMin=stack[-1]
            else:
                leftMin=-1
            area=(rightMin-leftMin-1)*current
            maxArea=max(maxArea,area)
        stack.append(i)
    while stack:
        rightMin=n
        current=arr[stack.pop()]
        if(stack):
            leftMin=stack[-1]
        else:
            leftMin=-1
        area=(rightMin-leftMin-1)*current
        maxArea=max(maxArea,area)
    return maxArea
    
arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(better(n,arr))
print(optimized(n,arr))
