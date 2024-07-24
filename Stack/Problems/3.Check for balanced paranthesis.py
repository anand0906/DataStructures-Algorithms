def solve(n,s):
    stack=[]
    temp={"(":")","[":"]","{":"}"}
    for i in range(n):
        if(s[i] in "({["):
            stack.append(s[i])
        else:
            if len(stack)==0:
                return False
            if(temp[stack[-1]]==s[i]):
                stack.pop()
            else:
                return False
    if(len(stack)>0):
        return False
    return True

s=input()
n=len(s)
print(solve(n,s))
