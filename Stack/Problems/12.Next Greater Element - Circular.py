def bruteForce(n,arr):
    ans=[]
    for i in range(n):
        flag=True
        for j in range(i+1,n+i):
            if(arr[j%n]>arr[i]):
                ans.append(arr[j%n])
                flag=False
                break
        if(flag):
            ans.append(-1)
    return ans

def optimized(n,arr):
    ans=[]
    stack=[]
    for j in range(2*n-1,-1,-1):
        i=j%n
        while stack and arr[i]>=stack[-1]:
            stack.pop()
        if(j<n):
            if(stack):
                ans.append(stack[-1])
            else:
                ans.append(-1)
        stack.append(arr[i])
    ans=ans[::-1]
    return ans  

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(optimized(n,arr))
                
            
