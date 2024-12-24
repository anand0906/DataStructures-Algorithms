def infixToPostfix(s):
    n=len(s)
    stack=[]
    ans=""
    order={"(":0,")":0,"+":1,"-":1,"*":2,"/":2,"%":2,"^":3}
    for i in range(n):
        if(s[i].isalnum()):
            ans+=s[i]
        elif(s[i]=="("):
            stack.append(s[i])
        elif(s[i]==")"):
            while stack and stack[-1]!="(":
                ans+=stack.pop()
            stack.pop()
        else:
            while (stack and
                   ((s[i] == "^" and order[s[i]] < order[stack[-1]]) or
                    (s[i] != "^" and order[s[i]] <= order[stack[-1]]))):
                ans += stack.pop()
            stack.append(s[i])
    while stack:
        ans+=stack.pop()
    return ans

def solve(s):
    n=len(s)
    temp=list(s[::-1])
    for i in range(n):
        if(temp[i]=="("):
            temp[i]=")"
        elif(temp[i]==")"):
            temp[i]="("
    temp="".join(temp)
    ans=infixToPostfix(temp)
    ans=ans[::-1]
    return ans
s=input()
print(solve(s))
