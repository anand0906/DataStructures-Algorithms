def bruteForce(n,word):
    maxi=0
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
                length=j-i+1
                maxi=max(maxi,length)
    return maxi

def better(n,word):
    maxi=0
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
                length=j-i+1
                maxi=max(maxi,length)
    return maxi

def optimized(n,word):
    prefix={0:-1}
    currentXor=0
    maxi=0
    for i in range(n):
        if(word[i] in 'aeiou'):
            mask=1<<(ord(word[i])-ord('a'))
            currentXor^=mask
        if(currentXor in prefix):
            length=i-prefix[currentXor]
            maxi=max(maxi,length)
        if(currentXor not in prefix):
            prefix[currentXor]=i
    return maxi
word=input()
n=len(word)
print(bruteForce(n,word))
print(better(n,word))
print(optimized(n,word))
