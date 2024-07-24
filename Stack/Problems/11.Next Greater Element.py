def bruteForce(n,arr):
    ans=[]
    for i in range(n):
        flag=True
        for j in range(i+1,n):
            if(arr[j]>arr[i]):
                ans.append(arr[j])
                flag=False
                break
        if(flag):
            ans.append(-1)
    return ans

def optimized(n,arr):
    ans=[]
    stack=[]
    for i in range(n-1,-1,-1):
        if(i==n-1):
            ans.append(-1)
            stack.append(arr[i])
        else:
            while stack and arr[i]>=stack[-1]:
                stack.pop()
            if(stack):
                ans.append(stack[-1])
            else:
                ans.append(-1)
            stack.append(arr[i])
    return ans[::-1]
    
arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(optimized(n,arr))
