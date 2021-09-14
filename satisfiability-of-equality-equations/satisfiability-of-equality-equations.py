class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        def find(x):
            return x if parent[x] == x else find(parent[x])
        
        def union(i,j):
            if find(i) != find(j):
                parent[find(j)] = find(i)
        
        parent = [i for i in range(256)]
        
        f = 0 
        
        for i in equations:
            
            if i[1] == '=':
                union(ord(i[0]),ord(i[-1]))
                f = 1
                
        
        for i in equations:
            
            if i[1] == '!':
                if i[0]==i[-1] or find(ord(i[0])) == find(ord(i[-1])):
                    return False
                
        
                
        return True