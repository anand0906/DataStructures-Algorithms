def bruteForce(n,word):
    ans=0
    for i in range(n):
        for j in range(i,n):
            cntVowels={k:0 for k in 'aeiou'}
            for k in range(i,j+1):
                if(word[k] in 'aeiou'):
                    cntVowels[word[k]]+=1
            flag=True
            for ch,cnt in cntVowels.items():
                if(cnt%2!=0):
                    flag=False
                    break
            if(flag):
                ans+=1
    return ans

def better(n,word):
    ans=0
    for i in range(n):
        cntVowels={k:0 for k in 'aeiou'}
        for j in range(i,n):
            if(word[j] in 'aeiou'):
                cntVowels[word[j]]+=1
            flag=True
            for ch,cnt in cntVowels.items():
                if(cnt%2!=0):
                    flag=False
                    break
            if(flag):
                ans+=1
    return ans

def optimized(n,word):
    prefix={0:1}
    currentXor=0
    cnt=0
    for i in range(n):
        if(word[i] in 'aeiou'):
            mask=1<<(ord(word[i])-ord('a'))
            currentXor^=mask
        if(currentXor in prefix):
            cnt+=prefix[currentXor]
        if(currentXor in prefix):
            prefix[currentXor]+=1
        else:
            prefix[currentXor]=1
    return cnt
word=input()
n=len(word)
print(bruteForce(n,word))
print(better(n,word))
print(optimized(n,word))
