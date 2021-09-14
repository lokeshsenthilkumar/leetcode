class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        def find(x):
            return x if x not in parent else find(parent[x])
        
        def union(i,j):
            fi = find(i) ; fj = find(j)
            if fi!=fj:
                parent[fj] = fi
        
        parent = {}
        
        for i in equations:
            if i[1] == '=':
                union(i[0],i[-1])
                
        
        for i in equations:
            if i[1] == '!':
                if find(i[0]) == find(i[-1]):
                    return False
        
        return True