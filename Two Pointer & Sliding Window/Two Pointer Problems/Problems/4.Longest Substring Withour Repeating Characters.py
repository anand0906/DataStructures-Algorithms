def bruteForce(n,s):
    maxi=0
    for i in range(n):
        for j in range(i+1,n+1):
            substr=s[i:j]
            count={}
            for k in substr:
                if k in count:
                    count[k]+=1
                else:
                    count[k]=1
                if(count[k]>1):
                    break
            else:
                length=j-i
                maxi=max(maxi,length)
    return maxi

def better(n,s):
    maxi=0
    for i in range(n):
        check={}
        substr=""
        for j in range(i,n):
            if s[j] in check:
                break
            substr+=s[j]
            check[s[j]]=1
            length=j-i+1
            maxi=max(maxi,length)
    return maxi

def better2(n,s):
    maxi=0
    for i in range(n):
        check=[0]*256
        for j in range(i,n):
            if check[ord(s[j])]:
                break
            check[ord(s[j])]=1
            length=j-i+1
            maxi=max(maxi,length)
    return maxi

def optimized(n,s):
    maxi=0
    check={}
    left,right=0,0
    while right<n:
        if s[right] in check:
            left=max(check[s[right]]+1,left)
        check[s[right]]=right
        length=right-left+1
        maxi=max(maxi,length)
        right+=1
    return maxi

def optimized2(n,s):
    maxi=0
    check=[-1]*256
    left,right=0,0
    while right<n:
        if check[ord(s[right])]!=-1:
            left=max(check[ord(s[right])]+1,left)
        check[ord(s[right])]=right
        length=right-left+1
        maxi=max(maxi,length)
        right+=1
    return maxi

s=input()
n=len(s)
print(bruteForce(n,s))
print(better(n,s))
print(better2(n,s))
print(optimized(n,s))
print(optimized2(n,s))
