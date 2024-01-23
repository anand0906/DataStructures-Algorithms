n,e=list(map(int,input().split()))
edges=[input().split() for i in range(e)]
edges_con=[(int(i),int(j)) for i,j in edges]
graph={i:set() for i in range(n)}
for i,j in edges_con:
    graph[i].add(j)
    graph[j].add(i)
queue=[]
distance={i:float('inf') for i in range(n)}
queue.append(0)
distance[0]=0
while queue:
    temp=queue.pop()
    for i in graph[temp]:
        if(1+distance[temp] < distance[i]):
            queue.append(i)
            distance[i]=1+distance[temp]
print(distance)
