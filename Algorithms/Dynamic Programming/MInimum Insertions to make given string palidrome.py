#Find Logngest palindrome in given string
#then the remaining is the non-palindromic
#then to make non palindromic into palindromic.
#we need reverse of non-palindromic
#then length of non-palindromic is answer

def lcs(s1,s2,m,n):
    if(m<0 or n<0):
        return 0
    else:
        if(s1[m]==s2[n]):
            return 1+lcs(s1,s2,m-1,n-1)
        else:
            return max(lcs(s1,s2,m-1,n),lcs(s1,s2,m,n-1))
s1=input()
temp=s1[::-1]
k=lcs(s1,temp,len(s1)-1,len(temp)-1)
print(len(s1)-k)
