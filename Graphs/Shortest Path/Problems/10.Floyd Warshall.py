nodes,edge=list(map(int,input().split()))
edges=[input().split() for i in range(edge)]
edges_converted=[(int(i)-1,int(j)-1,int(w)) for i,j,w in edges]
src,dest=list(map(int,input().split()))
graph=[[float('inf')]*nodes for i in range(nodes)]
for i,j,w in edges_converted:
    graph[i][j]=w
for i in range(nodes):
    graph[i][i]=0
for k in range(nodes):
    for i in range(nodes):
        for j in range(nodes):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
print(graph[src-1][dest-1])

            
