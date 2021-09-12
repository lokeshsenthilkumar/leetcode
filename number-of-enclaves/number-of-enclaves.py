class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        r = len(grid) ; c = len(grid[0])
        
        def dfs(i,j):
            
            if i<0 or i==r or j<0 or j==c or grid[i][j]==0:
                return 0
            
            grid[i][j] = 0
            
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1) 
            
        res = 0
        
        for i in range(r):
            for j in range(c):
                if i*j==0 or i==r-1 or j==c-1:
                    dfs(i,j)
                    
        for i in grid:
            res += sum(i) 
        
        return res
        