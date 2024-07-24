def bruteForce(n,arr):
    ans=[]
    for i in range(n):
        flag=True
        for j in range(i-1,0,-1):
            if(arr[j]<arr[i]):
                ans.append(arr[j])
                flag=False
                break
        if(flag):
            ans.append(-1)
    return ans

def optimized(n,arr):
    ans=[]
    stack=[]
    for i in range(n):
        if(i==0):
            ans.append(-1)
            stack.append(arr[i])
        else:
            while stack and arr[i]<=stack[-1]:
                stack.pop()
            if(stack):
                ans.append(stack[-1])
            else:
                ans.append(-1)
            stack.append(arr[i])
    return ans
    
arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(optimized(n,arr))
