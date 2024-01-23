import heapq
n,m=list(map(int,input().split()))
matrix=[list(map(int,input().split())) for i in range(1,n+1)]
source=list(map(int,input().split()))
dest=list(map(int,input().split()))
distance=[[float('inf')]*m for i in range(n)]
queue=[(0,source)]
distance[source[0]][source[1]]=0
heapq.heapify(queue)
while queue:
    temp=heapq.heappop(queue)
    dist,loc=temp
    r,c=loc
    for i,j in zip([1,-1,0,0],[0,0,1,-1]):
        row,col=r+i,c+j
        if(row>=0 and row<n and col>=0 and col<m and matrix[row][col]==1):
            new_dist=dist+1
            if(new_dist<distance[row][col]):
                distance[row][col]=new_dist
                heapq.heappush(queue,(new_dist,(row,col)))
print(distance[dest[0]][dest[1]])
