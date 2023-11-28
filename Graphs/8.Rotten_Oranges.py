n=int(input("Enter row size : "))
m=int(input("Enter column size : "))
matrix=[list(map(int,input().split())) for i in range(n)]
queue=[]
count=0
ct=0
final=-float('inf')
for i in range(n):
    for j in range(m):
        if(matrix[i][j]==2):
            queue.append((i,j,0))
        if(matrix[i][j]==1):
            count+=1
a,b=[0,0,1,-1],[1,-1,0,0]
while queue:
    temp=queue.pop(0)
    r,c,v=temp
    for i in range(4):
        r1=r+a[i]
        c1=c+b[i]
        if(r1>=0 and r1<n and c1<m and c1>=0 and matrix[r1][c1]==1):
            matrix[r1][c1]+=1
            ct+=1
            queue.append((r1,c1,v+1))
            final=max(final,v+1)
print(*matrix,sep="\n")
if(ct==count):
    print(final)
else:
    print(-1)
            
    
