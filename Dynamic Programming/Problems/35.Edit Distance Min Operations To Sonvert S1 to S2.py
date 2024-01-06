'''
Base Cases :
------------
index1<0 -> index2+1
index2<0 -> index1+1

Recurrance Relation:
---------------------
f(index1,index2)=
if(S1[index2]==S2[index2]):
    return f(index1-1,index2-1)
else:
    replace=1+f(index1-1,index2-1)
    insert=1+f(index1-1,index2)
    delete=1+f(index1,index2-1)
    return min(replace,insert,delete)
'''
#TC : O(2^(n1*n2))
#Sc : O(n1*n2)
def recursive(s1,s2,index1,index2):
    if(index1<0):
        return index2+1
    if(index2<0):
        return index1+1
    if(s1[index1]==s2[index2]):
        return recursive(s1,s2,index1-1,index2-1)
    else:
        replace=1+recursive(s1,s2,index1-1,index2-1)
        insert=1+recursive(s1,s2,index1-1,index2)
        delete=1+recursive(s1,s2,index1,index2-1)
        return min(replace,insert,delete)
    
#TC : O(n1*n2)
#Sc : O(n1*n2)
def memorization(s1,s2,index1,index2,memo):
    key=(index1,index2)
    if key in memo:
        return memo[key]
    if(index1<0):
        return index2+1
    if(index2<0):
        return index1+1
    if(s1[index1]==s2[index2]):
        memo[key]=memorization(s1,s2,index1-1,index2-1,memo)
        return memo[key]
    else:
        replace=1+memorization(s1,s2,index1-1,index2-1,memo)
        insert=1+memorization(s1,s2,index1-1,index2,memo)
        delete=1+memorization(s1,s2,index1,index2-1,memo)
        memo[key]=min(replace,insert,delete)
        return memo[key]

#TC : O(n1*n2)
#Sc : O(n1*n2)
def tabulation(s1,s2,n1,n2):
    dp=[[0]*(n2+1) for i in range(n1+1)]
    for i in range(1,n1+1):
        dp[i][0]=i
    for i in range(1,n2+1):
        dp[0][i]=i
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            index1,index2=i-1,j-1
            if(s1[index1]==s2[index2]):
                dp[i][j]=dp[i-1][j-1]
            else:
                replace=1+dp[i-1][j-1]
                insert=1+dp[i-1][j]
                delete=1+dp[i][j-1]
                dp[i][j]=min(replace,insert,delete)
    return dp[n1][n2]

#TC : O(n1*n2)
#Sc : O(n2)
def optimization(s1,s2,n1,n2):
    dp_prev=[0]*(n2+1)
    dp_curr=[0]*(n2+1)
    dp_curr[0]=0
    for i in range(1,n2+1):
        dp_prev[i]=i
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            dp_curr[0]=i
            index1,index2=i-1,j-1
            if(s1[index1]==s2[index2]):
                dp_curr[j]=dp_prev[j-1]
            else:
                replace=1+dp_prev[j-1]
                insert=1+dp_prev[j]
                delete=1+dp_curr[j-1]
                dp_curr[j]=min(replace,insert,delete)
        dp_prev=dp_curr.copy()
    return dp_curr[n2]

s1,s2=input(),input()
n1,n2=len(s1),len(s2)
print(recursive(s1,s2,n1-1,n2-1))
memo={}
print(memorization(s1,s2,n1-1,n2-1,memo))
print(tabulation(s1,s2,n1,n2))
print(optimization(s1,s2,n1,n2))
