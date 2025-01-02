def solve(n,arr,k):
    stack=[]
    k=n-k
    for i in range(n):
        while stack and arr[i]<stack[-1] and k>0:
            stack.pop()
            k-=1
        stack.append(arr[i])
    while stack and k>0:
        stack.pop()
        k-=1
    return stack


arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(solve(n,arr,k))
