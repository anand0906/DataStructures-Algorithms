def bruteforce(n,s,k):
    maxi=0
    for i in range(n):
        for j in range(i,n):
            maxFreq=0
            count={}
            for t in range(i,j+1):
                if s[t] in count:
                    count[s[t]]+=1
                else:
                    count[s[t]]=1
                maxFreq=max(maxFreq,count[s[t]])
            length=j-i+1
            if((length-maxFreq)<=k):
                maxi=max(maxi,length)
    return maxi

def better(n,s,k):
    maxi=0
    for i in range(n):
        maxFreq=0
        count={}
        for j in range(i,n):
            if s[j] in count:
                count[s[j]]+=1
            else:
                count[s[j]]=1
            maxFreq=max(maxFreq,count[s[j]])
            length=j-i+1
            if((length-maxFreq)<=k):
                maxi=max(maxi,length)
    return maxi

def optimized(n,s,k):
    left,right=0,0
    maxi=0
    maxFreq=0
    count={}
    while(right<n):
        if s[right] in count:
            count[s[right]]+=1
        else:
            count[s[right]]=1
        maxFreq=max(maxFreq,count[s[right]])
        length=right-left+1
        while((left<right) and (length-maxFreq)>k):
            count[s[left]]-=1
            maxFreq=max(maxFreq,count[s[left]])
            left+=1
            length=right-left+1
        maxi=max(maxi,length)
        right+=1
    return maxi

s=input()
n=len(s)
k=int(input())
print(bruteforce(n,s,k))
print(better(n,s,k))
print(optimized(n,s,k))
