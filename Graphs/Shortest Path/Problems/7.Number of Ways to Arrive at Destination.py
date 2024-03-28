import heapq
nodes,edge=list(map(int,input().split()))
edges=[input().split() for i in range(edge)]
edges_converted=[(int(i),int(j),int(w)) for i,j,w in edges]
source=int(input())
destination=int(input())
graph={i:dict() for i in range(nodes)}
ways={i:0 for i in range(nodes)}
for i,j,w in edges_converted:
    graph[i][j]=w
    graph[j][i]=w
distance={i:float('inf') for i in range(nodes)}
distance[source]=0
ways[source]=1
queue=[]
heapq.heappush(queue,(source,0))
while queue:
    node,currentDistance=heapq.heappop(queue)
    for adj,weight in graph[node].items():
        if(currentDistance+weight<distance[adj]):
            distance[adj]=currentDistance+weight
            heapq.heappush(queue,(adj,distance[adj]))
            ways[adj]=ways[node]
        elif(currentDistance+weight==distance[adj]):
            ways[adj]=(ways[node]+ways[adj])%(int(1e9+9))
print(-1 if(distance[destination]==float('inf')) else ways[destination])
