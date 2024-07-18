def bruteforce(n,s):
    cnt=0
    for i in range(n):
        for j in range(i,n):
            temp=[0,0,0]
            for k in range(i,j+1):
                temp[ord(s[k])-ord('a')]=1
                if(temp[0] and temp[1] and temp[2]):
                    cnt+=1
                    break
    return cnt

def better(n,s):
    cnt=0
    for i in range(n):
        temp=[0,0,0]
        for j in range(i,n):
            temp[ord(s[j])-ord('a')]=1
            if(temp[0] and temp[1] and temp[2]):
                cnt+=1
    return cnt

def better2(n,s):
    cnt=0
    for i in range(n):
        temp=[0,0,0]
        for j in range(i,n):
            temp[ord(s[j])-ord('a')]=1
            if(temp[0] and temp[1] and temp[2]):
                cnt+=(n-j)
                break
    return cnt

def optimized(n,s):
    left,right=0,0
    cnt=0
    temp=[0,0,0]
    while right<n:
        temp[ord(s[right])-ord('a')]+=1
        while(temp[0] and temp[1] and temp[2]):
            cnt+=(n-right)
            temp[ord(s[left])-ord('a')]-=1
            left+=1
        right+=1
    return cnt

s=input()
n=len(s)
print(bruteforce(n,s))
print(better(n,s))
print(better2(n,s))
print(optimized(n,s))
                
