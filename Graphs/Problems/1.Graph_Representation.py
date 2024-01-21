class Graph:
    def __init__(self,nodes,vertices):
        self.nodes=nodes
        self.vertices=vertices

        if(str(self.nodes[0]).isalpha()):
            for i,v in enumerate(self.nodes):
                self.nodes[i]=ord(v)-ord('A')+1
            for i,edge in enumerate(self.vertices):
                edge=list(edge)
                edge[0]=ord(edge[0])-ord('A')+1
                edge[1]=ord(edge[1])-ord('A')+1
                self.vertices[i]=edge
        print(self.nodes,self.vertices)
                

    def get_adjacency_matrix(self):
        matrix=[[0 for i in range(len(self.nodes)+1)] for i in range(len(self.nodes)+1)]
        for i,j in self.vertices:
            matrix[i][j]=1
            matrix[j][i]=1
        return matrix
    
    def get_adjacency_matrix_ordered(self):
        matrix=[[0 for i in range(len(self.nodes)+1)] for i in range(len(self.nodes)+1)]
        for i,j in self.vertices:
            matrix[i][j]=1
        return matrix

    def get_adjacency_matrix_weighted(self):
        matrix=[[0 for i in range(len(self.nodes)+1)] for i in range(len(self.nodes)+1)]
        for i,j,w in self.vertices:
            matrix[i][j]=w
            matrix[j][i]=w
        return matrix
    
    def get_adjacency_matrix_ordered_weighted(self):
        matrix=[[0 for i in range(len(self.nodes)+1)] for i in range(len(self.nodes)+1)]
        for i,j,w in self.vertices:
            matrix[i][j]=w
        return matrix

    def print_adjacency_matrix(self):
        matrix=self.get_adjacency_matrix()
        for row in matrix:
            print(*row,sep=" ",end="\n")
            
    def print_adjacency_matrix_ordered(self):
        matrix=self.get_adjacency_matrix_ordered()
        for row in matrix:
            print(*row,sep=" ",end="\n")

    def print_adjacency_matrix_weighted(self):
        matrix=self.get_adjacency_matrix_weighted()
        for row in matrix:
            print(*row,sep=" ",end="\n")
            
    def print_adjacency_matrix_ordered_weighted(self):
        matrix=self.get_adjacency_matrix_ordered_weighted()
        for row in matrix:
            print(*row,sep=" ",end="\n")

    def get_adjacency_list_weighted(self):
        adj_list={}
        for i,j,w in self.vertices:
            if i in adj_list:
                adj_list[i].append(w)
            else:
                adj_list[i]=[w]

            if j in adj_list:
                adj_list[j].append(w)
            else:
                adj_list[j]=[w]
        return adj_list

    def get_adjacency_list_ordered_weighted(self):
        adj_list={}
        for i,j,w in self.vertices:
            if i in adj_list:
                adj_list[i].append(w)
            else:
                adj_list[i]=[w]
        return adj_list

    def get_adjacency_list(self):
        adj_list={}
        for i,j in self.vertices:
            if i in adj_list:
                adj_list[i].append(j)
            else:
                adj_list[i]=[j]

            if j in adj_list:
                adj_list[j].append(i)
            else:
                adj_list[j]=[i]
        return adj_list

    def get_adjacency_list_ordered(self):
        adj_list={}
        for i,j in self.vertices:
            if i in adj_list:
                adj_list[i].append(j)
            else:
                adj_list[i]=[j]
        return adj_list

    def print_adjacency_list(self):
        adj_list=self.get_adjacency_list()
        for i,v in adj_list.items():
            print(i,"->",v,end="\n")
            
    def print_adjacency_list_ordered(self):
        adj_list=self.get_adjacency_list_ordered()
        for i,v in adj_list.items():
            print(i,"->",v,end="\n")
            
    def print_adjacency_list_weighted(self):
        adj_list=self.get_adjacency_list_weighted()
        for i,v in adj_list.items():
            print(i,"->",v,end="\n")
            
    def print_adjacency_list_ordered_weighted(self):
        adj_list=self.get_adjacency_list_ordered_weighted()
        for i,v in adj_list.items():
            print(i,"->",v,end="\n")


print("Unordered Graph")
vertices=['A','B','C','D','E']
edges=[('A','B'),('A','C'),('A','D'),('B','D'),('B','E'),('C','D'),('D','D'),('D','E')]
graph=Graph(vertices,edges)
graph.print_adjacency_matrix()
graph=Graph(vertices,edges)
graph.print_adjacency_list()
print("Unordered Graph with weights")
vertices=['A','B','C','D','E']
edges=[('A','B',2),('A','C',4),('A','D',5),('B','D',7),('B','E',9),('C','D',10),('D','D',4),('D','E',3)]
graph=Graph(vertices,edges)
graph.print_adjacency_matrix_weighted()
graph=Graph(vertices,edges)
graph.print_adjacency_list_weighted()
print("Ordered Graph")
vertices=['A','B','C','D','E']
edges=[('A','B'),('A','C'),('B','D'),('B','E'),('C','D'),('D','D'),('D','E')]
graph=Graph(vertices,edges)
graph.print_adjacency_matrix_ordered()
graph=Graph(vertices,edges)
graph.print_adjacency_list_ordered()
print("Ordered Graph with weights")
vertices=['A','B','C','D','E']
edges=[('A','B',2),('A','C',3),('B','D',4),('B','E',5),('C','D',6),('D','D',7),('D','E',8)]
graph=Graph(vertices,edges)
graph.print_adjacency_matrix_ordered_weighted()
graph=Graph(vertices,edges)
graph.print_adjacency_list_ordered_weighted()



            
        
    
        
        
    
