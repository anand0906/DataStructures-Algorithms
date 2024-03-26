nodes,edges=int(input()),int(input())
edges=[input().split() for i in range(edges)]
edges_converted=[(int(i),int(j)) for i,j in edges]
graph={i:set() for i in range(nodes)}
for i,j in edges_converted:
    graph[i].add(j)
    graph[j].add(i)
queue=[]
distance={i:float('inf') for i in range(nodes)}
source=0
distance[source]=0
queue.append(source)
while queue:
    current=queue.pop(0)
    for adj in graph[current]:
        if(distance[current]+1 < distance[adj]):
            distance[adj]=1+distance[current]
            queue.append(adj)
final_output={i:-1 for i in range(nodes)}
for i,j in distance.items():
    if(distance[i]!=float('inf')):
    	final_output[i]=j
print(final_output)
