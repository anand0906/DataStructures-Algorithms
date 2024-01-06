'''
Base Cases :
------------
index1<0 and index2<0 -> True
index1<0 and index2>=0 -> False
index2<0 and index1>=0 -> True if(AllStar(S1,index1)) else False

Recurrance Relation :
--------------------
if(S1[index1]==S2[index2] or s1[index1]=='?'):
    return f(index1-1,index2-1)
else:
    if(S1[index1]=='*'):
        return f(index1-1,index2) or f(index1,index2-1)
    else:
         return False
    
'''
#TC : O(2^(n1*n2))
#SC : O(n1*n2)
def recursive(S1,S2,index1,index2):
    if(index1<0 and index2<0):
        return True
    if(index1<0 and index2>=0):
        return False
    if(index2<0 and index1>=0):
        if(S1[index1]=='*' and len(set(S1[index1:]))==1):
            return True
        else:
            return False

    if(S1[index1]==S2[index2] or S1[index1]=='?'):
        return recursive(S1,S2,index1-1,index2-1)
    else:
        if(S1[index1]=='*'):
            excludeS1=recursive(S1,S2,index1-1,index2)
            excludeS2=recursive(S1,S2,index1,index2-1)
            return excludeS1 or excludeS2
        else:
            return False

#TC : O(n1*n2)
#SC : O(n1*n2)
def memorization(S1,S2,index1,index2,memo):
    key=(index1,index2)
    if key in memo:
        return memo[key]
    if(index1<0 and index2<0):
        return True
    if(index1<0 and index2>=0):
        return False
    if(index2<0 and index1>=0):
        if(S1[index1]=='*' and len(set(S1[index1:]))==1):
            return True
        else:
            return False

    if(S1[index1]==S2[index2] or S1[index1]=='?'):
        memo[key]=memorization(S1,S2,index1-1,index2-1,memo)
        return memo[key]
    else:
        if(S1[index1]=='*'):
            excludeS1=memorization(S1,S2,index1-1,index2,memo)
            excludeS2=memorization(S1,S2,index1,index2-1,memo)
            memo[key]=excludeS1 or excludeS2
            return memo[key]
        else:
            memo[key]=False
            return memo[key]


#TC : O(n1*n2)
#SC : O(n1*n2)
def tabulation(S1,S2,n1,n2):
    dp=[[False]*(n2+1) for i in range(n1+1)]
    dp[0][0]=True
    for i in range(1,n2+1):
        dp[0][i]=False
    for i in range(1,n1+1):
        index1=i-1
        if(S1[index1]=='*' and len(set(S1[index1:]))==1):
            dp[i][0]=True
        else:
            dp[i][0]=False
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            index1,index2=i-1,j-1
            if(S1[index1]==S2[index2] or S1[index1]=='?'):
                dp[i][j]=dp[i-1][j-1]
            else:
                if(S1[index1]=='*'):
                    dp[i][j]=dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j]=False
    return dp[n1][n2]

#TC : O(n1*n2)
#SC : O(n2)
def optimization(S1,S2,n1,n2):
    dp_prev=[False]*(n2+1)
    dp_curr=[False]*(n2+1)
    dp_prev[0]=True
    for i in range(1,n2+1):
        dp_prev[i]=False
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            index1,index2=i-1,j-1
            if(S1[index1]=='*' and len(set(S1[index1:]))==1):
                dp_curr[0]=True
            else:
                dp_curr[0]=False
            if(S1[index1]==S2[index2] or S1[index1]=='?'):
                dp_curr[j]=dp_prev[j-1]
            else:
                if(S1[index1]=='*'):
                    dp_curr[j]=dp_prev[j] or dp_curr[j-1]
                else:
                    dp_curr[j]=False
        dp_prev=dp_curr.copy()
    return dp_curr[n2]

S1=input()
S2=input()
n1=len(S1)
n2=len(S2)
print(recursive(S1,S2,n1-1,n2-1))
memo={}
print(memorization(S1,S2,n1-1,n2-1,memo))
print(tabulation(S1,S2,n1,n2))
print(optimization(S1,S2,n1,n2))
