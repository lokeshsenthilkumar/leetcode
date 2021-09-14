class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        if len(connections) < n-1:
            return -1
        
        def find(x):
            return x if x==parent[x] else find(parent[x])
    
        parent = [i for i in range(n)]
        extraEdge = 0
        components = 0
        
        for i,j in connections:
            
            fi = find(i)
            fj = find(j)
            
            if fi!=fj:
                parent[fj] = fi
            else:
                extraEdge += 1
                
        for i in range(n):
            if parent[i] == i:
                components += 1
        
        if extraEdge < components-1:
            retun -1
        
        return  components-1