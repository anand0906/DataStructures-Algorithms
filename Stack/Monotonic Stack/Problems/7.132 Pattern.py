def bruteForce(n,arr):
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if(arr[i]<arr[k]<arr[j]):
                    return True
    return False

def better(n,arr):
    PGE=[None]*n
    stack=[]
    for i in range(n):
        while stack and arr[i]>=arr[stack[-1]]:
            stack.pop()
        if stack:
            PGE[i]=stack[-1]
        stack.append(i)
    MINI=[None]*n
    currentMini=float('inf')
    for i in range(n):
        MINI[i]=currentMini
        currentMini=min(currentMini,arr[i])
    for i in range(n):
        if(PGE[i] and arr[i]>MINI[PGE[i]]):
            return True
    return False

def optimized(n,arr):
    stack=[]
    currentMin=float('inf')
    for i in range(n):
        while stack and arr[i]>=arr[stack[-1][0]]:
            stack.pop()
        if stack and arr[i]>stack[-1][1]:
            return True
        stack.append((i,currentMin))
        currentMin=min(currentMin,arr[i])
    return False
    


arr=list(map(int,input().split()))
n=len(arr)
print(bruteForce(n,arr))
print(better(n,arr))
print(optimized(n,arr))
