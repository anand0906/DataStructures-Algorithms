n,e=list(map(int,input().split()))
edges=[input().split() for i in range(e)]
edges_con=[(int(i),int(j),int(w)) for i,j,w in edges]
graph={i:dict() for i in range(n)}
for i,j,w in edges_con:
    graph[i][j]=w
distance={i:float('inf') for i in range(n)}
distance[0]=0
for i in range(n-1):
    for i,j,w in edges_con:
        new_dist=w+distance[i]
        if(new_dist < distance[j]):
            distance[j]=new_dist

for i,j,w in edges_con:
    if(distance[j]!=float('inf') and w+distance[i] < distance[j]):
        print(-1)
        break
else:
    print(distance)
