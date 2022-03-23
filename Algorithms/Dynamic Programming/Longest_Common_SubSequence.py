##replace max with in min to get minimum legth subsequence

s1=input()
s2=input()

def lcs(s1,s2,m,n):
    if(m<0 or n<0):
        return 0
    else:
        if(s1[m]==s2[n]):
            return 1+lcs(s1,s2,m-1,n-1)
        else:
            return max(lcs(s1,s2,m-1,n),lcs(s1,s2,m,n-1))
def lcs(s1,s2,m,n):
    global memo
    key=(m,n)
    if key in memo:
        return memo[key]
    if(m<0 or n<0):
        return 0
    else:
        if(s1[m]==s2[n]):
            memo[key]=1+lcs(s1,s2,m-1,n-1)
            return memo[key]
        else:
            memo[key]=max(lcs(s1,s2,m-1,n),lcs(s1,s2,m,n-1))
            return memo[key]

def lcs(s1,s2,m,n):#print subsequencse
    if(m<0 or n<0):
        return ""
    else:
        if(s1[m]==s2[n]):
            return s1[m]+lcs(s1,s2,m-1,n-1)
        else:
            return max(lcs(s1,s2,m-1,n),lcs(s1,s2,m,n-1),key=len)
def lcs(s1,s2,m,n):#print subsequencse
    global memo
    key=(m,n)
    if key in memo:
        return memo[key]
    if(m<0 or n<0):
        return ""
    else:
        if(s1[m]==s2[n]):
            memo[key]=s1[m]+lcs(s1,s2,m-1,n-1)
            return memo[key]
        else:
            memo[key]=max(lcs(s1,s2,m-1,n),lcs(s1,s2,m,n-1),key=len)
            return memo[key]
def tabulation(s1,s2):
    m=len(s1)
    n=len(s2)
    dp=[[0]*(n+1) for i in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if(s1[i-1]==s2[j-1]):
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[m][j]

def tabulation(s1,s2):# print all sub sequences
    m=len(s1)
    n=len(s2)
    dp=[[""]*(n+1) for i in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if(s1[i-1]==s2[j-1]):
                dp[i][j]=s1[i-1]+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1],key=len)
    return dp[m][j]
m=len(s1)
n=len(s2)
memo={}
print(lcs(s1,s2,m-1,n-1))
print(tabulation(s1,s2))
            
