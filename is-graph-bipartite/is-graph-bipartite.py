class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph) 
        
        color = [-1]*(n)
        
        for i in range(n):
            
            if color[i] != -1:
                continue
            
            color[i] = 1
            q = [i]
            
            while q!=[]:
                
                print(q,color)
                curr = q.pop(0)
                

                for e in graph[curr]:
                    
                    print(curr,e)
                    print(color[curr],color[e])
                    
                    if color[e] == -1:
                        color[e] = 1 - color[curr]
                        q.append(e)
                    elif color[e] == color[curr]:
                        return False
                    
                
                        
        return True
                    
            
        