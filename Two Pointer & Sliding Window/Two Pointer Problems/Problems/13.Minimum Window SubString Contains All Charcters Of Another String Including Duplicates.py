def bruteForce(n,s,t):
    minLen=float('inf')
    minSubStr=""
    cnt=len(t)
    for i in range(n):
        for j in range(i,n):
            visited={}
            for temp in t:
                if temp in visited:
                    visited[temp]+=1
                else:
                    visited[temp]=1
            currentCnt=0
            for k in range(i,j+1):
                if s[k] in visited:
                    visited[s[k]]-=1
                else:
                    visited[s[k]]=-1
                if(visited[s[k]]>=0):
                    currentCnt+=1
            if(currentCnt>=cnt and (j-i+1)<minLen):
                minLen=j-i+1
                minSubStr=s[i:j+1]
    return minSubStr

def better(n,s,t):
    minLen=float('inf')
    minSubStr=""
    cnt=len(t)
    for i in range(n):
        visited={}
        for temp in t:
            if temp in visited:
                visited[temp]+=1
            else:
                visited[temp]=1
        currentCnt=0
        for j in range(i,n):
            if s[j] in visited:
                visited[s[j]]-=1
            else:
                visited[s[j]]=-1
            if(visited[s[j]]>=0):
                currentCnt+=1
            if(currentCnt>=cnt and (j-i+1)<minLen):
                minLen=j-i+1
                minSubStr=s[i:j+1]
    return minSubStr


def optimized(n,s,t):
    left,right=0,0
    minLength=float('inf')
    minSubStr=""
    visited={}
    for temp in t:
        if temp in visited:
            visited[temp]+=1
        else:
            visited[temp]=1
    cnt=len(t)
    currentCnt=0
    while(right<n):
        if(s[right] in visited):
            visited[s[right]]-=1
        else:
            visited[s[right]]=-1
        if(visited[s[right]]>=0):
            currentCnt+=1
        while(currentCnt==cnt):
            length=right-left+1
            if(length<minLength):
                minLength=length
                minSubStr=s[left:right+1]
            visited[s[left]]+=1
            if(visited[s[left]]>0):
                currentCnt-=1
            left+=1
        right+=1
    return minSubStr
s=input()
t=input()
n=len(s)
print(bruteForce(n,s,t))
print(better(n,s,t))
print(optimized(n,s,t))
