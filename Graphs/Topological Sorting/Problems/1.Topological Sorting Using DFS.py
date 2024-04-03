def dfs(node,graph,visited,stack):
    visited[node]=True
    for adj in graph[node]:
        if(not visited[adj]):
            dfs(adj,graph,visited,stack)
    stack.append(node)
nodes,edge=list(map(int,input().split()))
edges=[input().split() for i in range(edge)]
edges_converted=[(int(i),int(j)) for i,j in edges]
graph={i:set() for i in range(nodes)}
visited={i:False for i in range(nodes)}
stack=[]
for i,j in edges_converted:
    graph[i].add(j)
for i in range(nodes):
    if(not visited[i]):
        dfs(i,graph,visited,stack)
print(*stack[::-1])
