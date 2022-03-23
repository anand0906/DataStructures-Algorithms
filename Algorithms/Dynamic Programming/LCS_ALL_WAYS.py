def lcs(a,b,m,n,temp=[],memo=[]):
    global final
    key=(m,n)
    if key in memo:
        return memo[key]
    if(m==0 or n==0):
        if temp:
            final.add(tuple(temp[::-1]))
        return 0
    if(a[m-1]==b[n-1]):
        lcs(a,b,m-1,n-1,temp+[a[m-1]])
    lcs(a,b,m-1,n,temp)
    lcs(a,b,m,n-1,temp)
a=input()
b=input()
m=len(a)
g=[]
n=len(b)
final=set()
print(lcs(a,b,m,n))
print(final)
print(g)
