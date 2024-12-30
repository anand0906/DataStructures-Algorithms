def bruteForce(n, arr):
    ans = [1]*n
    for i in range(n):
        for j in range(i-1, -1, -1):
            if arr[j] > arr[i]:
                ans[i]=i-j
                break
        else:
            ans[i]=i+1
    return ans

def optimized(n,arr):
    ans=[1]*n
    stack=[]
    for i in range(n):
        while stack and arr[i]>=arr[stack[-1]]:
            stack.pop()
        if stack:
            ans[i]=i-stack[-1]
        else:
            ans[i]=i+1
        stack.append(i)
    return ans

arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(optimized(n,arr))
