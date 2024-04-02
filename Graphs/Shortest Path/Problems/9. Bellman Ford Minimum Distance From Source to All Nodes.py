n,e=list(map(int,input().split()))
edges=[list(map(int,input().split())) for i in range(e)]
edges_converted=[(int(i),int(j),int(w)) for i,j,w in edges]
source=int(input())
distance={i:float('inf') for i in range(n)}
distance[source]=0
for _ in range(n-1):
    for i,j,w in edges_converted:
        if(distance[i]+w<distance[j]):
            distance[j]=distance[i]+w
for i,j,w in edges_converted:
    if(distance[i]+w<distance[j]):
        print("Negative Cycle")
        break
else:
    print(distance)
    
