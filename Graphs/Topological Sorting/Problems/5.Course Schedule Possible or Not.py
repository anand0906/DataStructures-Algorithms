tasks,dependencies=list(map(int,input().split()))
nodes=tasks
edges=[list(map(int,input().split())) for i in range(dependencies)]
edges_converted=[(int(i),int(j)) for i,j in edges]
graph={i:set() for i in range(nodes)}
indegree={i:0 for i in range(nodes)}
for i,j in edges_converted:
    graph[i].add(j)
    indegree[j]+=1
queue=[]
for i in range(nodes):
    if(indegree[i]==0):
        queue.append(i)
topoSort=[]
while queue:
    currentNode=queue.pop(0)
    topoSort.append(currentNode)
    for adj in graph[currentNode]:
        indegree[adj]-=1
        if(indegree[adj]==0):
            queue.append(adj)
if(len(topoSort)==tasks):
    print("Yes")
else:
    print("No")

