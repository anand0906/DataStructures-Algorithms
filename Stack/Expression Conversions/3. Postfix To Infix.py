def solve(s):
    n=len(s)
    stack=[]
    for i in range(n):
        if(s[i].isalnum()):
            stack.append(s[i])
        else:
            op1=stack.pop()
            op2=stack.pop()
            exp=f"{op2}{s[i]}{op1}"
            stack.append(exp)
    return stack[-1]
s=input()
print(solve(s))
