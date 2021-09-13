class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        
        def dfs(u):
            
            if vis[u] != 0:
                return vis[u] == 1
            
            vis[u] = -1
            
            for v in graph[u]:
                if dfs(v) == False:
                    return False
                
            vis[u] = 1
            
            return True
        
        
        res = []
        
        r = len(graph) ; c = len(graph[0])
        
        vis = [0]*(r)
        
        for i in range(r):
            if dfs(i):
                res.append(i)
        
        return res