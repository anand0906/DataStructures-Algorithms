n=int(input("Enter row size : "))
m=int(input("Enter column size : "))
matrix=[input().split() for i in range(n)]
visited=[[False]*m for i in range(n)]
queue=[]
for i in range(n):
    if(matrix[i][0]=='0'):
        queue.append((i,0))
        visited[i][0]=True
    if(matrix[i][m-1]=='0'):
        queue.append((i,m-1))
        visited[i][m-1]=True
        
for j in range(m):
    if(matrix[0][j]=='0'):
        queue.append((0,j))
        visited[0][j]=True
    if(matrix[n-1][j]=='0'):
        queue.append((n-1,j))
        visited[n-1][j]=True
while queue:
    temp=queue.pop(0)
    for i,j in zip([0,0,1,-1],[1,-1,0,0]):
        r=temp[0]+i
        c=temp[1]+j
        if(r<n and r>=0 and c<m and c>=0 and (not visited[r][c]) and matrix[r][c]=='0'):
            queue.append((r,c))
            visited[r][c]=True
for i in range(n):
    for j in range(m):
        if(visited[i][j]==False and matrix[i][j]=='0'):
            matrix[i][j]="x"
print(*matrix,sep="\n")
    
            


