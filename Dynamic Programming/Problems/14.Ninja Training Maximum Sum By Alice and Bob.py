'''
Base cases :
f(n-1,j)=matrix[n-1][j]
f(i,j>n-1)=float('-inf')
f(i,j<0)=float('-inf')

Recurrance relation :
final=float('-inf')
for i in range(-1,2):
    for j in range(-1,2):
        final=max(final,f(row+1,j1+i,j2+j))
f(i,j1,j2)=final
'''

#TC : O(9^(n))
#SC : O(n)
def recursive(n,m,matrix,row,col1,col2):
    if(col1<0 or col1>m-1 or col2<0 or col2>m-1):
        return float('-inf')
    if(row==n-1):
        if(col1==col2):
            return matrix[n-1][col1]
        else:
            return matrix[n-1][col1]+matrix[n-1][col2]
    final=float('-inf')
    for i in range(-1,2):
        for j in range(-1,2):
            if(col1==col2):
                temp=matrix[row][col1]+recursive(n,m,matrix,row+1,col1+i,col2+j)
            else:
                temp=matrix[row][col1]+matrix[row][col2]+recursive(n,m,matrix,row+1,col1+i,col2+j)
            final=max(final,temp)
    return final

#TC : O(n*m*m)
#SC : O(n*m*m)+O(n)
def memorization(n,m,matrix,row,col1,col2,memo):
    key=(row,col1,col2)
    if key in memo:
        return memo[key]
    if(col1<0 or col1>m-1 or col2<0 or col2>m-1):
        return float('-inf')
    if(row==n-1):
        if(col1==col2):
            return matrix[n-1][col1]
        else:
            return matrix[n-1][col1]+matrix[n-1][col2]
    final=float('-inf')
    for i in range(-1,2):
        for j in range(-1,2):
            if(col1==col2):
                temp=matrix[row][col1]+memorization(n,m,matrix,row+1,col1+i,col2+j,memo)
            else:
                temp=matrix[row][col1]+matrix[row][col2]+memorization(n,m,matrix,row+1,col1+i,col2+j,memo)
            final=max(final,temp)
    memo[key]=final
    return final

def tabulation(n,m,matrix):
    dp=[[[0]*m for i in range(m)] for i in range(n)]
    for i in range(m):
        for j in range(m):
            if(i==j):
                dp[n-1][i][j]=matrix[n-1][j]
            else:
                dp[n-1][i][j]=matrix[n-1][i]+matrix[n-1][j]
    for row in range(n-2,-1,-1):
        for col1 in range(m):
            for col2 in range(m):
                final=float('-inf')
                for i in range(-1,2):
                    for j in range(-1,2):
                        c1,c2=col1+i,col2+j
                        if(c1<0 or c2<0 or c1>m-1 or c2>m-1):
                            ans=float('-inf')
                        if(col1==col2):
                            ans=matrix[row][col1]+dp[row+1][c1][c2]
                        else:
                            ans=matrix[row][col1]+matrix[row][col2]+dp[row+1][c1][c2]
                    final=max(final,ans)
            dp[row][col1][col2]=final
    return dp[0][0][m-1]
        
                
n,m=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(n)]
print(recursive(n,m,matrix,0,0,m-1))
memo={}
print(memorization(n,m,matrix,0,0,m-1,memo))
print(tabulation(n,m,matrix))
