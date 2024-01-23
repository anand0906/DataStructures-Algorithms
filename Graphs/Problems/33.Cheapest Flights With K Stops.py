import heapq
n,e=list(map(int,input().split()))
edges=[input().split() for i in range(e)]
source,dest,k=list(map(int,input().split()))
edges_con=[(int(i),int(j),int(w)) for i,j,w in edges]
graph={i:dict() for i in range(n)}
for i,j,w in edges_con:
    graph[i][j]=w
distance={i:float('inf') for i in range(n)}
queue=[(0,source,0)]
distance[0]=0
heapq.heapify(queue)
while queue:
    stops,node,dist=heapq.heappop(queue)
    for i in graph[node]:
        if(graph[node][i]+dist < distance[i] and stops<=k):
            distance[i]=graph[node][i]+dist
            heapq.heappush(queue,(stops+1,i,distance[i]))
print(distance[dest])
