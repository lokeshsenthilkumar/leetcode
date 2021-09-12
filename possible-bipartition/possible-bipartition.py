class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        color = [-1]*(n+1)
        
        adj = [[] for _ in range(n+1)]
        
        for i,j in dislikes:
            adj[i].append(j)
            adj[j].append(i)
            
            
        for i in range(1,n+1):
            
            if color[i] != -1:
                continue
            
            q = [i]
            color[i] = 0
        
            while q!=[]:
                
                u = q[0]; q.pop(0)
        
                for v in adj[u]:
                    
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        q.append(v)
                        
                    if color[u] == color[v]:
                        return 0

                    
        return 1