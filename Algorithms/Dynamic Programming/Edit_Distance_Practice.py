def find(str1,str2,m,n):
    if m==0:
        return n
    if n==0:
        return m
    if (str1[m-1]==str2[n-1]):
        return find(str1,str2,m-1,n-1)
    else:
        insert=1+find(str1,str2,m,n-1)
        remove=1+find(str1,str2,m-1,n)
        replace=1+find(str1,str2,m-1,n-1)
        return min(insert,remove,replace)
    
def find_memo(str1,str2,m,n,memo={}):
    key=(m,n)
    if key in memo:
        return memo[key]
    if m==0:
        return n
    if n==0:
        return m
    if str1[m-1]==str2[n-1]:
        memo[key]=find_memo(str1,str2,m-1,n-1,memo)
        return memo[key]
    else:
        insert=1+find_memo(str1,str2,m,n-1,memo)
        remove=1+find_memo(str1,str2,m-1,n,memo)
        replace=1+find_memo(str1,str2,m-1,n-1,memo)
        memo[key]=min(insert,remove,replace)
        return memo[key]

def find_tabulation(str1,str2,m,n):
    dp=[[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                dp[i][j]=j
            elif j==0:
                dp[i][j]=i
            elif str1[i-1]==str2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                insert=1+dp[i][j-1]
                remove=1+dp[i-1][j]
                replace=1+dp[i-1][j-1]
                dp[i][j]=min(insert,remove,replace)
    return dp[-1][-1]

def find_tabulation_optimization(str1,str2,m,n):
    prev=[i for i in range(n+1)]
    curr=[0 for j in range(n+1)]
    for i in range(1,m+1):
        curr[0]=i
        for j in range(1,n+1):
            if str1[i-1]==str2[j-1]:
                curr[j]=prev[j-1]
            else:
                insert=1+curr[j-1]
                remove=1+prev[j]
                replace=1+prev[j-1]
                curr[j]=min(insert,remove,replace)
        prev=curr.copy()
    return curr[-1]
            
def main():
    str1=input()
    str2=input()
    m=len(str1)
    n=len(str2)
    print(find(str1,str2,m,n))
    print(find_memo(str1,str2,m,n))
    print(find_tabulation(str1,str2,m,n))
    print(find_tabulation_optimization(str1,str2,m,n))
main()
