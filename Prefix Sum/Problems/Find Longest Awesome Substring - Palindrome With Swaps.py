from collections import defaultdict
def bruteForce(n,word):
    maxi=0
    for i in range(n):
        for j in range(i,n):
            freq=defaultdict(int)
            for k in range(i,j+1):
                freq[word[k]]+=1
            odd=0
            for ch,cnt in freq.items():
                if(cnt%2!=0):
                    odd+=1
            if(odd<=1):
                length=j-i+1
                maxi=max(maxi,length)
    return maxi

def better(n,word):
    maxi=0
    for i in range(n):
        freq=defaultdict(int)
        for j in range(i,n):
            freq[word[j]]+=1
            odd=0
            for ch,cnt in freq.items():
                if(cnt%2!=0):
                    odd+=1
            if(odd<=1):
                length=j-i+1
                maxi=max(maxi,length)
    return maxi

def optimized(n,word):
    prefix={}
    prefix[0]=-1
    currentXor=0
    maxi=0
    for i in range(n):
        mask=1<<int(word[i])
        currentXor^=mask
        if(currentXor in prefix):
            length=i-prefix[currentXor]
            maxi=max(maxi,length)
        for j in range(10):
            mask=1<<int(j)
            oddCnt=currentXor^mask
            if(oddCnt in prefix):
                length=i-prefix[oddCnt]
                maxi=max(maxi,length)
        if(currentXor not in prefix):
            prefix[currentXor]=i
    return maxi

def optimized2(n,word):
    prefix=[None]*1024
    prefix[0]=-1
    currentXor=0
    maxi=0
    for i in range(n):
        mask=1<<int(word[i])
        currentXor^=mask
        if(prefix[currentXor] is not None):
            length=i-prefix[currentXor]
            maxi=max(maxi,length)
        for j in range(10):
            mask=1<<int(j)
            oddCnt=currentXor^mask
            if(prefix[oddCnt] is not None):
                length=i-prefix[oddCnt]
                maxi=max(maxi,length)
        if(prefix[currentXor] is None):
            prefix[currentXor]=i
    return maxi
word=input()
n=len(word)
print(bruteForce(n,word))
print(better(n,word))
print(optimized(n,word))
print(optimized2(n,word))
