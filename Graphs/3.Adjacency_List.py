def adjacencyList():
    n=int(input("Enter Number Of Nodes : "))
    e=int(input("Enter Number of Edges : "))
    edges=[tuple(input().split()) for i in range(e)]
    edges_converted=[(ord(i)-ord('A')+1,ord(j)-ord('A')+1) for i,j in edges]
    graph={i:set() for i in range(1,n+1)}
    for i,j in edges_converted:
        graph[i].add(j)
        graph[j].add(i)
    print(*graph.items(),sep="\n")

def adjacencyList_weighted():
    n=int(input("Enter Number Of Nodes : "))
    e=int(input("Enter Number of Edges : "))
    edges=[tuple(input().split()) for i in range(e)]
    edges_converted=[(ord(i)-ord('A')+1,ord(j)-ord('A')+1,w) for i,j,w in edges]
    graph={i:dict() for i in range(1,n+1)}
    for i,j,w in edges_converted:
        graph[i][j]=w
        graph[j][i]=w
    print(*graph.items(),sep="\n")

def adjacencyList_ordered():
    n=int(input("Enter Number Of Nodes : "))
    e=int(input("Enter Number of Edges : "))
    edges=[tuple(input().split()) for i in range(e)]
    edges_converted=[(ord(i)-ord('A')+1,ord(j)-ord('A')+1) for i,j in edges]
    graph={i:set() for i in range(1,n+1)}
    for i,j in edges_converted:
        graph[i].add(j)
    print(*graph.items(),sep="\n")

def adjacencyList_ordered_weighted():
    n=int(input("Enter Number Of Nodes : "))
    e=int(input("Enter Number of Edges : "))
    edges=[tuple(input().split()) for i in range(e)]
    edges_converted=[(ord(i)-ord('A')+1,ord(j)-ord('A')+1,w) for i,j,w in edges]
    graph={i:dict() for i in range(1,n+1)}
    for i,j,w in edges_converted:
        graph[i][j]=w
    print(*graph.items(),sep="\n")
#adjacenyList()
adjacencyList_ordered()
#adjacencyList_weighted()
