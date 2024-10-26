from collections import defaultdict
def bruteForce(n,word):
    cnt=0
    for i in range(n):
        for j in range(i,n):
            freq=defaultdict(int)
            for k in range(i,j+1):
                freq[word[k]]+=1
            oddCnt=0
            for key,val in freq.items():
                if(val & 1):
                    oddCnt+=1
            if(oddCnt<=1):
                cnt+=1
    return cnt

def better(n,word):
    cnt=0
    for i in range(n):
        freq=defaultdict(int)
        for j in range(i,n):
            freq[word[j]]+=1
            oddCnt=0
            for key,val in freq.items():
                if(val & 1):
                    oddCnt+=1
            if(oddCnt<=1):
                cnt+=1
    return cnt

def optimized(n,word):
    ans=0
    prefix={}
    prefix[0]=1
    currentXor=0
    for i in range(n):
        mask=1<<(ord(word[i])-ord('a'))
        currentXor^=mask
        if(currentXor in prefix):
            ans+=prefix[currentXor] # for adding even subtring count
        for k in range(10): # since string can contain at most a to j charcters 
            mask=1<<k
            oddXor=currentXor^mask
            if oddXor in prefix:
                ans+=prefix[oddXor] # for adding one odd subtring count
        if(currentXor in prefix):
            prefix[currentXor]+=1
        else:
            prefix[currentXor]=1
    return ans

def optimized2(n,word):
    ans=0
    prefix=[None]*1024 # at most j(9 position), so max value 1<<10 == 1024
    prefix[0]=1
    currentXor=0
    for i in range(n):
        mask=1<<(ord(word[i])-ord('a'))
        currentXor^=mask
        if(prefix[currentXor] is not None):
            ans+=prefix[currentXor] # for adding even subtring count
        for k in range(10): # since string can contain at most a to j charcters 
            mask=1<<k
            oddXor=currentXor^mask
            if prefix[oddXor] is not None:
                ans+=prefix[oddXor] # for adding one odd subtring count
        if(prefix[currentXor] is not None):
            prefix[currentXor]+=1
        else:
            prefix[currentXor]=1
    return ans
            

word=input()
n=len(word)
print(bruteForce(n,word))
print(better(n,word))
print(optimized(n,word))
print(optimized2(n,word))
