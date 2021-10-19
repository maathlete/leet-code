class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        
        def dfs(node, graph, visited): 
            
            if node == end:
                return(True)
            
            else:
                
                visited[node] = True
                
                neighbors = graph[node]
                
                while neighbors:
                    
                    neighbor = neighbors.pop(0)
                    
                    if not visited[neighbor]:
                        
                        valid_path = dfs(neighbor, graph, visited)
                
                        if valid_path:
                            
                            return(True)
                
                return(False)
                
        graph = {i:[] for i in range(n)}
        
        for e in edges:
            
            u = e[0]
            v = e[1]
            
            graph[u] = graph[u] + [v]
            graph[v] = graph[v] + [u]
            
        visited = [False for _ in range(n)]
        
        return(dfs(start, graph, visited))
