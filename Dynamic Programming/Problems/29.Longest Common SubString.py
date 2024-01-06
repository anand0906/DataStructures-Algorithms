
def tabulation(S1,S2,n1,n2):
    dp=[[0]*(n2+1) for i in range(n1+1)]
    final=float('-inf')
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            index1,index2=i-1,j-1
            if(S1[index1]==S2[index2]):
                temp=1+dp[i-1][j-1]
                dp[i][j]=temp
                final=max(final,temp)
            else:
                dp[i][j]=0
    return final

def optimization(S1,S2,n1,n2):
    dp_prev=[0]*(n2+1)
    dp_curr=[0]*(n2+1)
    final=float('-inf')
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            index1,index2=i-1,j-1
            if(S1[index1]==S2[index2]):
                temp=1+dp_prev[j-1]
                dp_curr[j]=temp
                final=max(final,temp)
            else:
                dp_curr[j]=0
        dp_prev=dp_curr.copy()
    return final
S1=input()
S2=input()
n1,n2=len(S1),len(S2)
print(tabulation(S1,S2,n1,n2))
print(optimization(S1,S2,n1,n2))
