def bruteForce(n,arr):
    maxi=0
    for i in range(n):
        leftMin=-1
        for j in range(i-1,-1,-1):
            if(arr[j]<arr[i]):
                leftMin=j
                break
        rightMin=n
        for j in range(i+1,n):
            if(arr[j]<arr[i]):
                rightMin=j
                break
        width=rightMin-leftMin-1
        area=arr[i]*width
        maxi=max(maxi,area)
    return maxi

def better(n,arr):
    PSE=[-1]*n
    NSE=[n]*n
    stack=[]
    for i in range(n):
        while stack and arr[i]<arr[stack[-1]]:
            index=stack.pop()
            NSE[index]=i
        stack.append(i)
    stack=[]
    for i in range(n):
        while stack and arr[i]<arr[stack[-1]]:
            index=stack.pop()
        if(stack):
            PSE[i]=stack[-1]
        stack.append(i)
    maxi=0
    for i in range(n):
        leftMin=PSE[i]
        rightMin=NSE[i]
        width=rightMin-leftMin-1
        maxi=max(maxi,width*arr[i])
    return maxi

def optimized(n,arr):
    stack=[]
    maxi=0
    for i in range(n):
        while stack and arr[i]<arr[stack[-1]]:
            index=stack.pop()
            height=arr[index]
            leftMin=stack[-1] if stack else -1
            rightMin=i
            width=rightMin-leftMin-1
            maxi=max(maxi,width*height)
        stack.append(i)
    while stack:
        index=stack.pop()
        height=arr[index]
        leftMin=stack[-1] if stack else -1
        rightMin=n
        width=rightMin-leftMin-1
        maxi=max(maxi,width*height)
    return maxi

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(better(n,arr))
print(optimized(n,arr))
