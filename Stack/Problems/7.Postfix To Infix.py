def solve(n,s):
    stack=[]
    for i in range(n):
        if(s[i].isalnum()):
            stack.append(s[i])
        else:
            op1=stack.pop()
            op2=stack.pop()
            new=f"({op2+s[i]+op1})"
            stack.append(new)
    return stack[-1]

s=input()
n=len(s)
print(solve(n,s))
