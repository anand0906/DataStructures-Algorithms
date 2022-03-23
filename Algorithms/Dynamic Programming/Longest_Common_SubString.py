def tabulation(s1,s2):
    m=len(s1)
    n=len(s2)
    dp=[[0]*(n+1) for i in range(m+1)]
    final=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if(s1[i-1]==s2[j-1]):
                dp[i][j]=1+dp[i-1][j-1]
                final=max(dp[i][j],final)
            else:
                dp[i][j]=0
    return final
def tabulation(s1,s2):#print substring
    m=len(s1)
    n=len(s2)
    dp=[[""]*(n+1) for i in range(m+1)]
    final=""
    for i in range(1,m+1):
        for j in range(1,n+1):
            if(s1[i-1]==s2[j-1]):
                dp[i][j]=s1[i-1]+dp[i-1][j-1]
                final=max(dp[i][j],final,key=len)
            else:
                dp[i][j]=""
    return final
s1=input()
s2=input()
print(tabulation(s1,s2))
