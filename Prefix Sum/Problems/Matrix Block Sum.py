def prefixSum(n,m,matrix):
    prefix=[[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if(i==0 and j==0):
                prefix[i][j]=matrix[i][j]
            elif(i==0 and j!=0):
                prefix[i][j]=prefix[i][j-1]+matrix[i][j]
            elif(i!=0 and j==0):
                prefix[i][j]=prefix[i-1][j]+matrix[i][j]
            else:
                prefix[i][j]=prefix[i][j-1]+prefix[i-1][j]+matrix[i][j]-prefix[i-1][j-1]
    return prefix

def optimized(prefix,row1,col1,row2,col2):
    sum=prefix[row2][col2]
    if(col1>0):
        sum-=prefix[row2][col1-1]
    if(row1>0):
        sum-=prefix[row1-1][col2]
    if(row1>0 and col1>0):
        sum+=prefix[row1-1][col1-1]
    return sum


class Solution:
    def matrixBlockSum(self, mat, k):
        n,m=len(mat),len(mat[0])
        ans=[[0]*m for i in range(n)]
        prefix=prefixSum(n,m,mat)
        for i in range(n):
            for j in range(m):
                row1,col1=i-k,j-k
                row2,col2=i+k,j+k
                if(row2>n-1):
                    row2=n-1
                if(col2>m-1):
                    col2=m-1
                ans[i][j]=optimized(prefix,row1,col1,row2,col2)
        return ans
n,m=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(n)]
k=int(input())
ans=Solution().matrixBlockSum(matrix,k)
print(ans)
