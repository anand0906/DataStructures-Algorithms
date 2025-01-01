def bruteForce(n,s,k):
    s=list(s)
    for _ in range(k):

        n=len(s)
        current=1
        while (current<n) and s[current]>=s[current-1]:
            current+=1

        if(current<n):
            del s[current-1]
        else:
            del s[-1]
            
    ans=int("".join(s))
    return str(ans)

def optimized(num,k):
    arr=list(num)
    stack=[]
    for i in range(len(arr)):
        while stack and arr[i]<stack[-1] and k>0:
            stack.pop()
            k-=1
        stack.append(arr[i])
    while stack and k>0:
        stack.pop()
        k-=1
    ans="".join(stack).lstrip('0')
    return "0" if ans=="" else ans

s=input()
n=len(s)
k=int(input())
print(bruteForce(n,s,k))
        

        
