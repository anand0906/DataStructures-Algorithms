def bfs(matrix,i,j):
    global visited
    queue=[(i,j)]
    visited[i][j]=1
    while queue:
        temp=queue.pop(0)
        r,c=temp
        for row in range(-1,2):
            for col in range(-1,2):
                ro=r+row
                co=c+col
                if(ro>=0 and ro<n and co>=0 and co<m and matrix[ro][co] and (not visited[ro][co])):
                    visited[ro][co]=1
                    queue.append((ro,co))
    
n,m=int(input("Enter row size : ")),int(input("Enter column size : "))
matrix=[list(map(int,input().split())) for i in range(n)]
visited=[[0 for j in range(m)] for i in range(n)]
count=0
for i in range(n):
    for j in range(m):
        if(matrix[i][j] and (not visited[i][j])):
            count+=1
            bfs(matrix,i,j)
print(count)
