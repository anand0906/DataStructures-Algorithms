n=int(input("Enter row size : "))
m=int(input("Enter column size : "))
matrix=[list(map(int,input().split())) for i in range(n)]
distance=[[0]*m for i in range(n)]
visited=[[False]*m for i in range(n)]
queue=[]
for i in range(n):
    for j in range(m):
        if(matrix[i][j]==1):
            queue.append((i,j,0))
            visited[i][j]=True
while queue:
    temp=queue.pop(0)
    i,j,v=temp
    distance[i][j]=v
    for r,c in zip([0,0,1,-1],[1,-1,0,0]):
        row=i+r
        col=j+c
        if(row>=0 and row<n and col>=0 and col<m and (not visited[row][col])):
            queue.append((row,col,v+1))
            visited[row][col]=True
print(*distance,sep="\n")
            
