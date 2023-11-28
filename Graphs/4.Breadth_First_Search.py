def iterative():
    n=int(input("Enter number of nodes : "))
    e=int(input("Enter number of edges : "))
    edges=[input().split() for i in range(e)]
    edges_converted=[(ord(i)-ord('A')+1,ord(j)-ord('A')+1) for i,j in edges]
    graph={i:set() for i in range(1,n+1)}
    for i,j in edges_converted:
        graph[i].add(j)
        graph[j].add(i)
    visited={i:False for i in range(1,n+1)}
    for node in range(1,n+1):
        if(not visited[node])
            visited[1]=True
            queue=[1]
            final=[]
            while queue:
                temp=queue.pop(0)
                final.append(temp)
                for i in graph[temp]:
                    if(not visited[i]):
                        queue.append(i)
                        visited[i]=True
    print(final)

iterative()
    
    
