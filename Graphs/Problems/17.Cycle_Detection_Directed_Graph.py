def dfs(graph,node):
    global path,visited
    visited[node]=True
    path[node]=True
    for i in graph[node]:
        if(not visited[i]):
            temp=dfs(graph,i)
            if(temp):
                return True
        elif(path[node]):
            return True
    path[node]=False
    return False
n,e=list(map(int,input().split()))
edges=[input().split() for i in range(e)]
edges_con=[(int(i),int(j)) for i,j in edges]
graph={i:set() for i in range(1,n+1)}
for i,j in edges_con:
    graph[i].add(j)
visited={i:False for i in range(1,n+1)}
path={i:False for i in range(1,n+1)}
for i in range(1,n+1):
    k=dfs(graph,i)
    if(k):
        print("True")
        break
else:
    print("False")
