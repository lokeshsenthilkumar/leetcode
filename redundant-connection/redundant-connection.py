class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        v = len(edges)
        
        parent = [i for i in range(v+1)]
        
        def find(x):
            return x if parent[x]==x else find(parent[x])
        
        res = []
        
        for i,j in edges:
            
            fi = find(i)
            fj = find(j)
            
            if fi == fj:
                res =  [i,j]
            
            parent[fj] = fi
        
        return res
        
        