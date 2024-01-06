'''
Base Cases :
------------
index1<0 or index2<0 -> 0

Recurrance Relation :
------------------
if(S1[index1]==S2[index2]):
    return 1+f(index1-1,index2-1)
else:
    return max(f(index1-1,index2),f(index1,index2-1))
'''

def tabulation(S1,S2,n1,n2):
    dp=[[0]*(n2+1) for i in range(n1+1)]
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            index1,index2=i-1,j-1
            if(S1[index1]==S2[index2]):
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    lcs=dp[n1][n2]
    i,j=n1,n2
    final=[]
    while(i>0 and j>0):
        index1,index2=i-1,j-1
        if(S1[index1]==S2[index2]):
            i-=1
            j-=1
            final.append(S1[index1])
        else:
            if(dp[i-1][j] > dp[i][j-1]):
                i-=1
            else:
                j-=1
    return "".join(final[::-1])
S1=input()
S2=input()
n1,n2=len(S1),len(S2)
print(tabulation(S1,S2,n1,n2))
            
