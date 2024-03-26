import heapq
nodes,edge=int(input()),int(input())
edges=[input().split() for i in range(edge)]
edges_converted=[(int(i),int(j),int(w)) for i,j,w in edges]
source,destination=int(input("Source : ")),int(input("Destination : "))
graph={i:{} for i in range(1,nodes+1)}
for i,j,w in edges_converted:
    graph[i][j]=w
    graph[j][i]=w
queue=[]
heapq.heappush(queue,(0,source))
distance={i:float('inf') for i in range(1,nodes+1)}
parent={i:i for i in range(1,nodes+1)}
parent[source]=-1
distance[source]=0
while queue:
    dist,current=heapq.heappop(queue)
    for adj,weight in graph[current].items():
        if(distance[current]+weight < distance[adj]):
            distance[adj]=distance[current]+weight
            heapq.heappush(queue,(distance[current]+weight,adj))
            parent[adj]=current
temp=destination
final=[]
while temp!=source:
    final.append(temp)
    temp=parent[temp]
else:
    final.append(source)
print(final[::-1])

            
