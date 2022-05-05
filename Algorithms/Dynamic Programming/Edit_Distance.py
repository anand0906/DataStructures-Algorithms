def myfunc(s1,s2,m,n):
    #if first string becomes empty, that means we need to insert s2 charcters
    # to the s1, so we are returning n , that is length of length of s2
    #number of insertions
    if m==0:
        return n
    #if second string becomes empty, that means we need to remove s1 charcters to
    #make s1 equal to s2, so we are returning length of s1
    #number of removals
    if n==0:
        return m
    if s1[m-1]==s2[n-1]:
        return myfunc(s1,s2,m-1,n-1)
    else:
        insert=1+myfunc(s1,s2,m,n-1)
        remove=1+myfunc(s1,s2,m-1,n)
        replace=1+myfunc(s1,s2,m-1,n-1)
        return min(insert,remove,replace)

def myfunc(s1,s2,m,n,memo={}):
    key=(m,n)
    if key in memo:
        return memo[key]
    if m==0:
        return n
    if n==0:
        return m
    if s1[m-1]==s2[n-1]:
        memo[key]=myfunc(s1,s2,m-1,n-1,memo)
        return memo[key]
    else:
        insert=1+myfunc(s1,s2,m,n-1,memo)
        remove=1+myfunc(s1,s2,m-1,n,memo)
        replace=1+myfunc(s1,s2,m-1,n-1,memo)
        memo[key]=min(insert,remove,replace)
        return memo[key]

def myfunc_tabulation(s1,s2,m,n):
    dp=[[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                dp[i][j]=j
            elif j==0:
                dp[i][j]=i
            elif(s1[i-1]==s2[j-1]):
                dp[i][j]=dp[i-1][j-1]
            else:
                insert=dp[i][j-1]
                remove=dp[i-1][j]
                replace=dp[i-1][j-1]
                dp[i][j]=1+min(insert,remove,replace)
    return dp[-1][-1]

def myfunc_table_space(s1,s2,m,n):
    prev=[i for i in range(n+1)]
    curr=[0 for i in range(n+1)]
    for i in range(1,m+1):
        curr[0]=i
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]:
                curr[j]=prev[j-1]
            else:
                insert=curr[j-1]
                remove=prev[j]
                replace=prev[j-1]
                curr[j]=1+min(insert,remove,replace)
        prev=curr.copy()
    return curr[-1]

    
s1=input()
s2=input()
m=len(s1)
n=len(s2)
ans=myfunc(s1,s2,m,n)
print(ans,myfunc_tabulation(s1,s2,m,n),myfunc_table_space(s1,s2,m,n))
    
