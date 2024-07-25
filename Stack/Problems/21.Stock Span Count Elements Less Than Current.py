def bruteForce(n,arr):
    ans=[]
    for i in range(n):
        cnt=1
        for j in range(i-1,-1,-1):
            if(arr[j]<=arr[i]):
                cnt+=1
            else:
                break
        ans.append(cnt)
    return ans

def better(n,arr):
    pge=[]
    stack=[]
    for i in range(n):
        while stack and arr[i]>=arr[stack[-1]]:
            stack.pop()
        if(stack):
            pge.append(stack[-1])
        else:
            pge.append(-1)
        stack.append(i)
    ans=[]
    for i in range(n):
        ans.append(i-pge[i])
    return ans

def optimized(n,arr):
    ans=[]
    stack=[]
    for i in range(n):
        while stack and arr[i]>=arr[stack[-1]]:
            stack.pop()
        if(stack):
            ans.append(i-stack[-1])
        else:
            ans.append(i-(-1))
        stack.append(i)
    return ans
    


arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(better(n,arr))
print(optimized(n,arr))
