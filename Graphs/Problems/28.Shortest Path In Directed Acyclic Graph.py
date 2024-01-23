n,e=list(map(int,input().split()))
edges=[input().split() for i in range(e)]
edges_con=[(int(i),int(j),int(w)) for i,j,w in edges]
graph={i:dict() for i in range(n)}
for i,j,w in edges_con:
    graph[i][j]=w
indegree={i:0 for i in range(n)}
for i,j,w in edges_con:
    indegree[j]+=1
queue=[]
for i in range(n):
    if(indegree[i]==0):
        queue.append(i)
topo=[]
while queue:
    temp=queue.pop()
    topo.append(temp)
    for i in graph[temp]:
        indegree[i]-=1
        if(indegree[i]==0):
            queue.append(i)
distance={i:float('inf') for i in range(n)}
distance[0]=0
while topo:
    temp=topo.pop(0)
    for i in graph[temp]:
        if(graph[temp][i]+distance[temp] < distance[i]):
            distance[i]=graph[temp][i]+distance[temp]
print(distance)


