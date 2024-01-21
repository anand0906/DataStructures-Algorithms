n=int(input("Enter row size : "))
m=int(input("Enter column size : "))
matrix=[list(map(int,input().split())) for i in range(n)]
sr=int(input("Enter starting row : "))
sc=int(input("Enter starting column : "))
newColor=int(input("Enter new color : "))
queue=[(sr,sc)]
target=matrix[sr][sc]
a,b=[0,0,1,-1],[-1,1,0,0]
matrix[sr][sc]=newColor
while queue:
    temp=queue.pop(0)
    r,c=temp
    for i in range(4):
        r1,c1=r+a[i],c+b[i]
        if(r1>=0 and r1<n and c1>=0 and c1<m and matrix[r1][c1]==target):
            matrix[r1][c1]=newColor
            queue.append((r1,c1))
print(*matrix,sep="\n")
    

