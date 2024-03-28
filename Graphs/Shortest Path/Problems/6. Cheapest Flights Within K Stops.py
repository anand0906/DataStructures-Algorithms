import heapq
nodes,edge=list(map(int,input().split()))
edges=[input().split() for i in range(edge)]
edges_converted=[(int(i),int(j),int(w)) for i,j,w in edges]
source=int(input())
destination=int(input())
k=int(input())
graph={i:dict() for i in range(nodes)}
for i,j,w in edges_converted:
    graph[i][j]=w
distance={i:float('inf') for i in range(nodes)}
distance[source]=0
queue=[]
heapq.heappush(queue,(0,source,0))
while queue:
    steps,node,currentDistance=heapq.heappop(queue)
    for adj,weight in graph[node].items():
        if(steps+1<=k+1 and currentDistance+weight<distance[adj]):
            distance[adj]=currentDistance+weight
            heapq.heappush(queue,(steps+1,adj,distance[adj]))
print(-1 if(distance[destination]==float('inf')) else distance[destination])
