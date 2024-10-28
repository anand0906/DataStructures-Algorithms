def bruteForce(n,m,matrix):
    maxi=0
    def check(row,col,length):
        for r in range(row,row+length):
            for c in range(col,col+length):
                if(matrix[r][c]==0):
                    return False
        return True
    for i in range(n):
        for j in range(m):
            if(matrix[i][j]==1):
                for sideLen in range(1,min(n-i,m-j)+1):
                    temp=check(i,j,sideLen)
                    if(temp):
                        maxi=max(maxi,sideLen)
    area=maxi*maxi
    return area

def optimized(n,m,matrix):
    dp=[[0]*m for i in range(n)]
    for i in range(n):
        dp[i][0]=int(matrix[i][0])
    for j in range(m):
        dp[0][j]=matrix[0][j]
    maxi=0
    for i in range(n):
        for j in range(m):
            if(matrix[i][j]!=1):
                continue
            left,top,diagonal=0,0,0
            if(j>0):
                left=int(dp[i][j-1])
            if(i>0):
                top=int(dp[i-1][j])
            if(i>0 and j>0):
                diagonal=int(dp[i-1][j-1])
            dp[i][j]=min(left,top,diagonal)+1
            maxi=max(dp[i][j],maxi)
    area=maxi*maxi
    return area

n,m=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(n)]
print(bruteForce(n,m,matrix))
print(optimized(n,m,matrix))
