import heapq
n,m=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(n)]
source_row,source_col=list(map(int,input().split()))
dest_row,dest_col=list(map(int,input().split()))
distance=[[float('inf')]*m for i in range(n)]
distance[source_row][source_col]=0
queue=[]
heapq.heappush(queue,(0,(source_row,source_col)))
while queue:
    current_row,current_col=heapq.heappop(queue)[1]
    for i,j in zip([0,0,-1,1],[1,-1,0,0]):
        row=current_row+i
        col=current_col+j
        if(row>=0 and col>=0 and row<n and col<m and matrix[row][col]==1 and 1+distance[current_row][current_col]<distance[row][col]):
            distance[row][col]=1+distance[current_row][current_col]
            heapq.heappush(queue,(1+distance[current_row][current_col],(row,col)))
print(distance[dest_row][dest_col])
