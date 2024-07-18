def bruteForce(n,s,k):
    maxi=0
    for i in range(n):
        for j in range(i,n):
            temp=set()
            for t in range(i,j+1):
                temp.add(s[t])
                if(len(temp)>k):
                    break
            else:
                length=j-i+1
                maxi=max(maxi,length)
    return maxi

def better(n,s,k):
    maxi=0
    for i in range(n):
        temp=set()
        for j in range(i,n):
            temp.add(s[j])
            if(len(temp)>k):
                break
            length=j-i+1
            maxi=max(maxi,length)
    return maxi

def optimized(n,s,k):
    maxi=0
    left,right=0,0
    count={}
    while right<n:
        if s[right] in count:
            count[s[right]]+=1
        else:
            count[s[right]]=1
        if(len(count)>2):
            while (len(count)>k):
                count[s[left]]-=1
                if(count[s[left]]==0):
                    del count[s[left]]
                left+=1
        length=right-left+1
        maxi=max(maxi,length)
        right+=1
    return maxi

s=input()
n=len(s)
k=int(input())
print(bruteForce(n,s,k))
print(better(n,s,k))
print(optimized(n,s,k))
