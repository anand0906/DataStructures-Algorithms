import heapq
n,e=list(map(int,input().split()))
edges=[input().split() for i in range(e)]
edges_con=[(int(i),int(j),int(w)) for i,j,w in edges]
graph={i:dict() for i in range(n)}
for i,j,w in edges_con:
    graph[i][j]=w
    graph[j][i]=w
distance={i:float('inf') for i in range(n)}
ways={i:0 for i in range(n)}
queue=[(0,0)]
distance[0]=0
ways[0]=1
heapq.heapify(queue)
while queue:
    dist,node=heapq.heappop(queue)
    for i in graph[node]:
        new_dist=graph[node][i]+dist
        if(new_dist < distance[i]):
            distance[i]=new_dist
            heapq.heappush(queue,(new_dist,i))
            ways[i]=ways[node]
        elif(new_dist == distance[i]):
            ways[i]=ways[i]+ways[node]
print(ways[n-1])
            
