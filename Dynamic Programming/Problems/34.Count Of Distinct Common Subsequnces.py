'''
Base Cases :
------------
index2<0 -> 1
index1<0 -> 0

Recurrance Relation
------------------
f(index1,index2)=f(index1-1,index2-1)+f(index1-1,index2) if(S1[index1]==S2[index2]) else f(index1-1,index2)

'''

#TC : O(2^(n1*n2))
#SC : O(n1*n2)
def recursive(s1,s2,index1,index2):
    if(index2<0):
        return 1
    if(index1<0):
        return 0
    if(s1[index1]==s2[index2]):
        return recursive(s1,s2,index1-1,index2-1)+recursive(s1,s2,index1-1,index2)
    else:
        return recursive(s1,s2,index1-1,index2)
    
#TC : O(n1*n2)
#SC : O(n1*n2)
def memorization(s1,s2,index1,index2,memo):
    key=(index1,index2)
    if key in memo:
        return memo[key]
    if(index2<0):
        return 1
    if(index1<0):
        return 0
    if(s1[index1]==s2[index2]):
        memo[key]=memorization(s1,s2,index1-1,index2-1,memo)+memorization(s1,s2,index1-1,index2,memo)
        return memo[key]
    else:
        memo[key]=memorization(s1,s2,index1-1,index2,memo)
        return memo[key]
    
#TC : O(n1*n2)
#SC : O(n1*n2)
def tabulation(s1,s2,n1,n2):
    dp=[[0]*(n2+1) for i in range(n1+1)]
    for i in range(n2+1):
        dp[i][0]=1
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            index1,index2=i-1,j-1
            if(s1[index1]==s2[index2]):
                dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n1][n2]

#TC : O(n1*n2)
#SC : O(n2)
def optimization(s1,s2,n1,n2):
    dp_prev=[0]*(n2+1)
    dp_curr=[0]*(n2+1)
    dp_prev[0]=1
    dp_curr[0]=1
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            index1,index2=i-1,j-1
            if(s1[index1]==s2[index2]):
                dp_curr[j]=dp_prev[j-1]+dp_prev[j]
            else:
                dp_curr[j]=dp_prev[j]
        dp_prev=dp_curr.copy()
    return dp_curr[n2]
s1,s2=input(),input()
n1,n2=len(s1),len(s2)
print(recursive(s1,s2,n1-1,n2-1))
memo={}
print(memorization(s1,s2,n1-1,n2-1,memo))
print(tabulation(s1,s2,n1,n2))
print(optimization(s1,s2,n1,n2))
