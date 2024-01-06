

def tabulation(S1,S2,n1,n2):
    dp=[[0]*(n2+1) for i in range(n1+1)]
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            index1,index2=i-1,j-1
            if(S1[index1]==S2[index2]):
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    temp=[]
    i,j=n1,n2
    while(i>0 and j>0):
        index1,index2=i-1,j-1
        if(S1[index1]==S2[index2]):
            temp.append(S1[index1])
            i-=1
            j-=1
        else:
            if(dp[i-1][j]>dp[i][j-1]):
                temp.append(S1[index1])
                i-=1
            else:
                temp.append(S2[index2])
                j-=1
    while i>0:
        temp.append(S1[i-1])
        i-=1
    while j>0:
        temp.append(S2[j-1])
        j-=1
    return "".join(temp[::-1])
S1=input()
S2=input()
n1=len(S1)
n2=len(S2)
print(tabulation(S1,S2,n1,n2))
