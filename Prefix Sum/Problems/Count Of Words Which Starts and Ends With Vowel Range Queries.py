def bruteForce(n,words,q,queries):
    ans=[]
    for i in range(q):
        cnt=0
        left,right=queries[i]
        for j in range(left,right+1):
            word=words[j].lower()
            if(word[0] in "aeiou" and word[-1] in "aeiou"):
                cnt+=1
        ans.append(cnt)
    return ans
            
def optimized(n,words,q,queries):
    ans=[]
    prefixVowelCnt=[0]*n
    vowelCnt=0
    for i in range(n):
        word=words[i].lower()
        if(word[0] in "aeiou" and word[-1] in "aeiou"):
            vowelCnt+=1
        prefixVowelCnt[i]=vowelCnt
    for i in range(q):
        left,right=queries[i]
        if(left==0):
            ans.append(prefixVowelCnt[right])
        else:
            ans.append(prefixVowelCnt[right]-prefixVowelCnt[left-1])
    return ans

words=input().split()
n=len(words)
q=int(input())
queries=[list(map(int,input().split())) for i in range(q)]
print(bruteForce(n,words,q,queries))
print(optimized(n,words,q,queries))
