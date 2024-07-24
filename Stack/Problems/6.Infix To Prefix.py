def solve(n,s):
    s=s[::-1]
    temp=list(s)
    for i in range(n):
        if(temp[i]=="("):
            temp[i]=")"
        elif(temp[i]==")"):
            temp[i]="("
    s="".join(temp)
    stack=[]
    ans=""
    order={"(":0,")":0,"+":1,"-":1,"*":2,"/":2,"^":3}
    for i in range(n):
        if(s[i].isalnum()):
            ans+=s[i]
        elif(s[i] == "("):
            stack.append(s[i])
        elif(s[i] == ")"):
            while stack and stack[-1]!="(":
                ans+=stack.pop()
            stack.pop()
        else:
            if(s[i]=="^"):
                while stack and (order[s[i]]<=order[stack[-1]]):
                    ans+=stack.pop()
            else:
                while stack and (order[s[i]]<order[stack[-1]]):
                    ans+=stack.pop()
            stack.append(s[i])
    while stack:
        ans+=stack.pop()
    return ans[::-1]

s=input()
n=len(s)
print(solve(n,s))
