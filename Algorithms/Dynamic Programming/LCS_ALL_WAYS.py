'''def lcs(a,b,m,n,temp=[],memo=[]):
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
    lcs(a,b,m,n-1,temp)'''

def lcs_tabulation():
    t=[ [-1]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                t[i][j]=''
            elif a[i-1]==b[j-1]:
                t[i][j]=t[i-1][j-1]+a[i-1]
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    for i in t:
        print(i)
                
a=input()
b=input()
m=len(a)
g=[]
n=len(b)
lcs_tabulation()
'''
final=set()
lcs(a,b,m,n)
for i in final:
    print("".join(i))'''
