'''
Base Cases :
------------
f(index1<0,index2<0)=0

Recurrance Relation :
---------------------
f(index1,index2)=1+f(index1-1,index2-1) if(S1[index1]==S2[index2]) else max(f(index1-1,index2),f(index1,index2-1))
'''

#TC : O(2^(n1*n2))
#SC : O(n1*n2)
def recursive(S1,S2,index1,index2):
    if(index1<0 or index2<0):
        return 0
    if(S1[index1]==S2[index2]):
        return 1+recursive(S1,S2,index1-1,index2-1)
    else:
        excludeS1=recursive(S1,S2,index1-1,index2)
        excludeS2=recursive(S1,S2,index1,index2-1)
        return max(excludeS1,excludeS2)

#TC : O(n1*n2)
#SC : O(n1*n2)
def memorization(S1,S2,index1,index2,memo):
    key=(index1,index2)
    if key in memo:
        return memo[key]
    if(index1<0 or index2<0):
        return 0
    if(S1[index1]==S2[index2]):
        memo[key]=1+ memorization(S1,S2,index1-1,index2-1,memo)
        return memo[key]
    else:
        excludeS1= memorization(S1,S2,index1-1,index2,memo)
        excludeS2= memorization(S1,S2,index1,index2-1,memo)
        memo[key]=max(excludeS1,excludeS2)
        return memo[key]

#TC : O(n1*n2)
#SC : O(n1*n2)
def tabulation(S1,S2):
    n1,n2=len(S1),len(S2)
    dp=[[0]*(n2+1) for i in range(n1+1)]
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            index1,index2=i-1,j-1
            if(S1[index1]==S2[index2]):
                dp[i][j]=1+dp[i-1][j-1]
            else:
                excludeS1=dp[i-1][j]
                excludeS2=dp[i][j-1]
                dp[i][j]=max(excludeS1,excludeS2)
    return dp[n1][n2]

#TC : O(n1*n2)
#SC : O(n2)
def optimization(S1,S2):
    n1,n2=len(S1),len(S2)
    dp_prev=[0]*(n2+1)
    dp_curr=[0]*(n2+1)
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            index1,index2=i-1,j-1
            if(S1[index1]==S2[index2]):
                dp_curr[j]=1+dp_prev[j-1]
            else:
                excludeS1=dp_prev[j]
                excludeS2=dp_curr[j-1]
                dp_curr[j]=max(excludeS1,excludeS2)
        dp_prev=dp_curr.copy()
    return dp_curr[n2]

S1=input()
S2=input()
n1=len(S1)
n2=len(S2)
print(recursive(S1,S2,n1-1,n2-1))
memo={}
print(memorization(S1,S2,n1-1,n2-1,memo))
print(tabulation(S1,S2))
print(optimization(S1,S2))

