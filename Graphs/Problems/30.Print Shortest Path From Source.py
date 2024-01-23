import heapq
n,e=list(map(int,input().split()))
edges=[input().split() for i in range(e)]
edges_con=[(int(i),int(j),int(w)) for i,j,w in edges]
graph={i:dict() for i in range(n)}
for i,j,w in edges_con:
    graph[i][j]=w
    graph[j][i]=w
distance={i:float('inf') for i in range(n)}
parent={i:i for i in range(n)}
source=0
queue=[(0,source)]
distance[0]=0
heapq.heapify(queue)
while queue:
    dist,node=heapq.heappop(queue)
    for i in graph[node]:
        if(graph[node][i]+dist < distance[i]):
            distance[i]=graph[node][i]+dist
            heapq.heappush(queue,(distance[i],i))
            parent[i]=node
dest=n-1
final=[]
while parent[dest]!=dest:
    final.append(dest)
    dest=parent[dest]
final.append(source)
print(final[::-1])
