'''
Base Cases :
------------
f(index1<0,index2<0)=0

Recurrance Relation :
---------------------
f(index1,index2)=1+f(index1-1,index2-1) if(S1[index1]==S2[index2]) else max(f(index1-1,index2),f(index1,index2-1))
'''

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
S2=S1[::-1]
n1=len(S1)
n2=len(S2)
print(optimization(S1,S2))
