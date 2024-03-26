import heapq
nodes,edges=int(input()),int(input())
edges=[input().split() for i in range(edges)]
edges_converted=[(int(i),int(j),int(w)) for i,j,w in edges]
graph={i:dict() for i in range(nodes)}
for i,j,w in edges_converted:
    graph[i][j]=w
    graph[j][i]=w
source=int(input())
queue=[]
distance={i:float('inf') for i in range(nodes)}
heapq.heappush(queue,(0,source))
distance[source]=0
while queue:
    dist,current=heapq.heappop(queue)
    for adj,weight in graph[current].items():
        if(dist+weight < distance[adj]):
            distance[adj]=dist+weight
            heapq.heappush(queue,(dist+weight,adj))
print(distance)


