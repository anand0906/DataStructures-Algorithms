def bruteForce(n,word,m):
    ans=[]
    temp=""
    for i in range(n):
        temp+=word[i]
        if(int(temp)%m==0):
            ans.append(1)
        else:
            ans.append(0)
    return ans

def optimized(n,word,m):
    ans=[]
    prevRem=0
    for i in range(n):
        digit=int(word[i])
        prevRem=(prevRem*10+(digit))%m
        if(prevRem%m==0):
            ans.append(1)
        else:
            ans.append(0)
    return ans

word=input()
n=len(word)
m=int(input())
print(bruteForce(n,word,m))
print(optimized(n,word,m))
