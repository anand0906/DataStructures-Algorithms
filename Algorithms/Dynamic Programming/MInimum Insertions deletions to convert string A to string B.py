def lcs(s1,s2,m,n):
    if(m<0 or n<0):
        return 0
    else:
        if(s1[m]==s2[n]):
            return 1+lcs(s1,s2,m-1,n-1)
        else:
            return max(lcs(s1,s2,m-1,n),lcs(s1,s2,m,n-1))
s1=input()
s2=input()
k=lcs(s1,s2,len(s1)-1,len(s2)-1)
delitions=len(s1)-k
insertions=len(s2)-k
print(insertions+delitions)
