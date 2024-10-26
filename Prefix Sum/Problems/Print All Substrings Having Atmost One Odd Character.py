from collections import defaultdict
def bruteForce(n,word):
    ans=[]
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
                ans.append(word[i:j+1])
    return sorted(ans)

def better(n,word):
    ans=[]
    for i in range(n):
        freq=defaultdict(int)
        for j in range(i,n):
            freq[word[j]]+=1
            oddCnt=0
            for key,val in freq.items():
                if(val & 1):
                    oddCnt+=1
            if(oddCnt<=1):
                ans.append(word[i:j+1])
    return sorted(ans)

def optimized(n,word):
    ans=[]
    prefix={}
    prefix[0]=[-1]
    currentXor=0
    for i in range(n):
        mask=1<<(ord(word[i])-ord('a'))
        currentXor^=mask
        if(currentXor in prefix):
            for j in prefix[currentXor]:
                ans.append(word[j+1:i+1])
        for k in range(10): # since string can contain at most a to j charcters 
            mask=1<<k
            oddXor=currentXor^mask
            if oddXor in prefix:
                for j in prefix[oddXor]:
                    ans.append(word[j+1:i+1])
        if(currentXor in prefix):
            prefix[currentXor].append(i)
        else:
            prefix[currentXor]=[i]
    return sorted(ans)

def optimized2(n,word):
    ans=[]
    prefix=[None]*1024 # at most j(9 position), so max value 1<<10 == 1024
    prefix[0]=[-1]
    currentXor=0
    for i in range(n):
        mask=1<<(ord(word[i])-ord('a'))
        currentXor^=mask
        if(prefix[currentXor] is not None):
            for j in prefix[currentXor]:
                ans.append(word[j+1:i+1])
        for k in range(10): # since string can contain at most a to j charcters 
            mask=1<<k
            oddXor=currentXor^mask
            if(prefix[oddXor] is not None):
                for j in prefix[oddXor]:
                    ans.append(word[j+1:i+1])
        if(prefix[currentXor] is not None):
            prefix[currentXor].append(i)
        else:
            prefix[currentXor]=[i]
    return sorted(ans)
            

word=input()
n=len(word)
print(bruteForce(n,word))
print(better(n,word))
print(optimized(n,word))
print(optimized2(n,word))
