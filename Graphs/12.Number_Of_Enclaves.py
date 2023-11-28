n=int(input("Enter row size : "))
m=int(input("Enter column size : "))
matrix=[list(map(int,input().split())) for i in range(n)]
queue=[]
visited=[[False]*m for i in range(n)]
for i in range(n):
    if(matrix[i][0]==1):
        queue.append((i,0))
    if(matrix[i][m-1]==1):
        queue.append((i,m-1))
for i in range(m):
    if(matrix[0][i]==1):
        queue.append((0,i))
    if(matrix[n-1][i]==1):
        queue.append((n-1,i))
while queue:
    temp=queue.pop(0)
    r,c=temp
    for i,j in zip([0,0,1,-1],[1,-1,0,0]):
        row,col=r+i,c+j
        if(row<n and col<m and row>=0 and col>=0 and (not visited[row][col]) and matrix[row][col]==1):
            queue.append((row,col))
            visited[row][col]=True
count=0
for i in range(n):
    for j in range(m):
        if((not visited[i][j]) and (matrix[i][j]==1)):
            count+=1
print(count)
