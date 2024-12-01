class Graph:
    def __init__(self,n):
        self.n = n
        self.adj = [[]*n for i in range(n)]
        
    def create_edge(self,x,y):
        self.adj[x-1].append(y-1)
        self.adj[y-1].append(x-1)
        
    def BFS(self,source):   
        visited = [False]*self.n
        res = []

        queue =  []
        queue.append(source)
        visited[source] = True
        
        while len(queue) > 0:
            s = queue.pop(0)
            res.append(s)
            for node in self.adj[s]:
                if visited[node] == False:
                    queue.append(node)
                    visited[node] = True
        return res

graph = Graph(4)
graph.create_edge(1,2)
graph.create_edge(1,3)
graph.create_edge(2,4) 

print(graph.BFS(1))