def undirected():
    n,e=int(input("Enter Number Of Nodes : ")),int(input("Enter Number Of Edges : "))
    edges=[input(f"Enter Edge {i+1} : ").split() for i in range(e)]
    edges_con=[(int(i)-1,int(j)-1) for i,j in edges]
    matrix=[[0]*(n) for i in range(n)]
    for i,j in edges_con:
        matrix[i][j]=1
        matrix[j][i]=1
    print(*matrix,sep="\n")

def directed():
    n,e=int(input("Enter Number Of Nodes : ")),int(input("Enter Number Of Edges : "))
    edges=[input(f"Enter Edge {i+1} : ").split() for i in range(e)]
    edges_con=[(int(i)-1,int(j)-1) for i,j in edges]
    matrix=[[0]*(n) for i in range(n)]
    for i,j in edges_con:
        matrix[i][j]=1
    print(*matrix,sep="\n")

def undirected_weighted():
    n,e=int(input("Enter Number Of Nodes : ")),int(input("Enter Number Of Edges : "))
    edges=[input(f"Enter Edge {i+1} : ").split() for i in range(e)]
    edges_con=[(int(i)-1,int(j)-1,int(w)) for i,j,w in edges]
    matrix=[[0]*(n) for i in range(n)]
    for i,j,w in edges_con:
        matrix[i][j]=w
        matrix[j][i]=w
    print(*matrix,sep="\n")

def directed_weighted():
    n,e=int(input("Enter Number Of Nodes : ")),int(input("Enter Number Of Edges : "))
    edges=[input(f"Enter Edge {i+1} : ").split() for i in range(e)]
    edges_con=[(int(i)-1,int(j)-1,int(w)) for i,j,w in edges]
    matrix=[[0]*(n) for i in range(n)]
    for i,j,w in edges_con:
        matrix[i][j]=w
    print(*matrix,sep="\n")

#undirected
#directed()
directed_weighted()
#undirected_weighted()
    
