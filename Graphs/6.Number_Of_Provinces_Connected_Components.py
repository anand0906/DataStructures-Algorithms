def bfs(graph,i):
    global visited
    queue=[i]
    visited[i]=False
    while queue:
        temp=queue.pop(0)
        for j in graph[temp]:
            if(not visited[j]):
                visited[j]=True
                queue.append(j)

n,e=int(input("Enter number of nodes : ")),int(input("Enter number of edges : "))
edges=[input().split() for i in range(e)]
edges_converted=[(int(i),int(j)) for i,j in edges]
graph={i:set() for i in range(1,n+1)}
for i,j in edges_converted:
    graph[i].add(j)
    graph[j].add(i)
visited={i:False for i in range(1,n+1)}
count=0
for i in range(1,n+1):
    if(not visited[i]):
        count+=1
        bfs(graph,i)
        
print(count)
