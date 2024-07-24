def solve(n,s,k):
    stack=[]
    for i in range(n):
        while stack and int(s[i]) <int(stack[-1]) and k>0:
            stack.pop()
            k-=1
        stack.append(s[i])

    while k>0:
        k-=1
        stack.pop()
    final="".join(stack).lstrip('0')
    return final if final else '0'

s=input()
n=len(s)
k=int(input())
print(solve(n,s,k))
