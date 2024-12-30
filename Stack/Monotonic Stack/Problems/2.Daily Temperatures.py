def bruteForce(n,arr):
    ans=[]
    for i in range(n):
        for j in range(i+1,n):
            if(arr[j]>arr[i]):
                days=j-i
                ans.append(days)
                break
        else:
            ans.append(0)
    return ans

def optimized(n,arr):
    ans=[0]*n
    stack=[]
    for i in range(n):
        while stack and arr[i]>arr[stack[-1]]:
            ind=stack.pop()
            ans[ind]=i-ind
        stack.append(i)
    return ans
arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(optimized(n,arr))
