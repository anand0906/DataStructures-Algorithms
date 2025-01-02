def bruteForce(n,s):
    ans=None
    unqCnt=len(set(s))
    def recursive(sub,pos,visited):
        nonlocal ans
        if(pos==n):
            if (ans==None or sub<ans) and sub!="" and len(visited)==unqCnt:
                ans=sub
            return
        recursive(sub,pos+1,visited.copy())
        if s[pos] not in visited:
            visited[s[pos]]=1
            recursive(sub+s[pos],pos+1,visited.copy())
    recursive("",0,{})
    return ans

def optimized(n,s):
    visited={i:False for i in set(s)}
    lastPos={i:s.rfind(i) for i in set(s)}
    stack=[]
    for i in range(n):
        if(visited[s[i]]):
            continue
        while stack and s[i]<stack[-1] and lastPos[stack[-1]]>i:
            temp=stack.pop()
            visited[temp]=False
        stack.append(s[i])
        visited[s[i]]=True
    ans="".join(stack)
    return ans


s=input()
n=len(s)
print(bruteForce(n,s))
print(optimized(n,s))
