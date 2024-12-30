def bruteForceNGE(n,arr):
    ans=[-1]*n
    for i in range(n):
        for j in range(i+1,i+n):
            index=j%n
            if(arr[index]>arr[i]):
                ans[i]=arr[index]
                break
    return ans

def optimizedNGE(n,arr):
    ans=[-1]*n
    stack=[]
    for i in range(2*n):
        i=i%n
        while stack and arr[i]>arr[stack[-1]]:
            index=stack.pop()
            ans[index]=arr[i]
        stack.append(i)
    return ans


arr=list(map(int,input().split()))
n=len(arr)
print(bruteForceNGE(n,arr))
print(optimizedNGE(n,arr))
