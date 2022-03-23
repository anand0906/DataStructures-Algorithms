def lcs(s1,s2,m,n):
    if(m<0 or n<0):
        return 0
    else:
        if(s1[m]==s2[n]):
            return 1+lcs(s1,s2,m-1,n-1)
        else:
            return max(lcs(s1,s2,m-1,n),lcs(s1,s2,m,n-1))
def lcs(s1,s2,m,n):#print subsequencse
    if(m<0 or n<0):
        return ""
    else:
        if(s1[m]==s2[n]):
            return s1[m]+lcs(s1,s2,m-1,n-1)
        else:
            return max(lcs(s1,s2,m-1,n),lcs(s1,s2,m,n-1),key=len)
s1=input()
temp=s1[::-1]
print(lcs(s1,temp,len(s1)-1,len(temp)-1))
